# basic class

class dog:  # dog class is defined
    def __init__(self,name,weight): # init method to initialize object attributes
        self.name = name
        self.weight = weight

dog1 = dog("dog", "buddy") # dog1 is an object of animal class
print(dog1.species)  # to get the species of dog1
print('\n',dog1.name) # to get the name of dog1


# ---------------------------------------------------------------------

# MODIFYING CLASS VAR AND INSTANCE VAR

class dog:  # dog class is defined

    species = "bull dog" # class variable

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
