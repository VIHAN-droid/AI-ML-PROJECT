from dotenv import load_dotenv
import os
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, SystemMessage
from operator import add as add_messages
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0.2)
embeddings = HuggingFaceEmbeddings(model_name="intfloat/e5-small-v2")

pdf_path = "D:\\Py_Projects\\Agentic AI\\Stock_Market_Performance_2024.pdf"

pdf_loader = PyPDFLoader(pdf_path)
pages = pdf_loader.load()

# chunking -> create a text splitter and apply it on the document
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
pages_split = text_splitter.split_documents(pages)

# make a directory and file name for the vector store
persist_directory = "D:\\Py_Projects\\Agentic AI\\vector_store"
collection_name = "stock_market_performance_2024"

if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

# create a vector store using chroma -> docs , embeddings , persist_directory , collection_name
vector_store = Chroma.from_documents(
    documents=pages_split,
    embedding=embeddings,
    persist_directory=persist_directory,
    collection_name=collection_name
)

# retriever -> to retrieve relevant documents based on the query
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}  # number of documents to retrieve
)

# make a retriever tool 
@tool
def retrieve_tools(query: str) -> str:
    """
    This tools searches and returns the information from the Stock Market Performance 2024 PDF.
    """
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant information found in the document."
    
    results = []
    for i,doc in enumerate(docs):
        results.append(f"Document {i+1}:\n{doc.page_content}\n")
    
    return "\n".join(results)

# make a tools list and bind that to llm
tools = [retrieve_tools]
llm_with_tools = llm.bind_tools(tools)

# define the state of the graph
class State(TypedDict):
    messages : Annotated[Sequence[BaseMessage], add_messages]

def should_continue(state: State):
    """ check if last message contains tool calls"""
    result = state["messages"][-1]
    return hasattr(result, "tool_calls") and len(result.tool_calls) > 0

# give the system prompt 
system_prompt = """You are an intelligent assistant helping users understand the Stock Market Performance 2024.
Use the retriever tool to find relevant parts of the document. Always cite the source page.
Don't guess if you're unsure — you can make multiple tool calls if needed."""

# tools dictionary for easy access
tools_dict = {tool.name: tool for tool in tools}

# make the llm chatbot
def llm_chatbot(state: State) -> State:
    message = list(state["messages"]) # converstaion history
    message = message + [SystemMessage(content=system_prompt)] # guide to the llm for conversation
    response = llm_with_tools.invoke(message)
    return {"messages": [response]}


def take_action(state: State):
    """ Execute tool calls from the LLM's response."""
    tool_calls = state['messages'][-1].tool_calls
    results = []
    for tool_call in tool_calls:
        name = tool_call['name']
        query = tool_call['args'].get("query", "")
        print(f"[TOOL CALL] {name} -> {query}")
        result = tools_dict[name].invoke(query)
        print(f"[RESULT] Length: {len(result)}")
        results.append(
            ToolMessage(tool_call_id=tool_call['id'], name=name, content=str(result))
        )
    return {"messages": results}

graph_builder = StateGraph(State)
graph_builder.add_node("llmchatbot", llm_chatbot)
graph_builder.add_node("retriever_agent",take_action)

graph_builder.add_edge(START, "llmchatbot")
graph_builder.add_conditional_edges(
    "llmchatbot",
    should_continue,
    {True: "retriever_agent", False: END}
)

graph = graph_builder.compile(checkpointer=MemorySaver())

config = {"configurable": {"thread_id":"1"}}

def running_agent():
    print("\n=== Stock Market RAG Agent ===")
    while True:
        user_input = input("\nQuestion: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        messages = [HumanMessage(content=user_input)]
        result = graph.invoke({"messages": messages}, config=config)
        print("\n=== Answer ===")
        print(result['messages'][-1].content)

running_agent()