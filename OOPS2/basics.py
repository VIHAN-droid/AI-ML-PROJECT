# basic class

class dog:  # dog class is defined
    def __init__(self,name,weight): # init method to initialize object attributes
        self.name = name
        self.weight = weight

dog1 = dog("dog", "buddy") # dog1 is an object of animal class
print(dog1.species)  # to get the species of dog1
print('\n',dog1.name) # to get the name of dog1


# --------------------------------------------------------------------------------------

# MODIFYING CLASS VAR AND INSTANCE VAR

class dog:  # dog class is defined

    species = "bull dog" # class variable  --> shared by all objects of this class

    def __init__(self,name,weight): # init method to initialize object attributes
        self.name = name
        self.weight = weight

    def __str__(self):  # when printing the obj str method is used to return the string
        return f"name is {self.name} and his weight is {self.weight}"

dog1 = dog("buddy",20)


# modify class variable
dog.species = "Canine"

# modify instance variable
dog1.name = "rowdy"
dog1.weight = "15"

# -----------------------------------------------------------------------------------------------

# Making PRIVATE ATTRIBUTES 

class bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # using __ to make an attribute private
    
    def deposit(self,amt):
        if amt > 0:
            self.__balance += amt
    
    def withdraw(self,amt):
        if 0 <= amt <= self.__balance:
            self.__balance -= amt

    def display_balance(self):
        print(f"Balalnce = {self.__balance} inr")


b1 = bank("rohit", 10000)
b1.display_balance()

b1.deposit(5000)
b1.display_balance()

b1.withdraw(7000)
b1.display_balance()


# --------------------------------------------------------------------------------------------------------

# USING OPERATONS ON OBJECTS

# __add__(self, other)
# __sub__(self, other)
# __mul__(self, other)  similarly for or,and,xor,gt(greater than),lt(less than),ge(greater than equal to),le(less than equal to),etc.
