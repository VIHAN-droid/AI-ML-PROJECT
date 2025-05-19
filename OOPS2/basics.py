# basic class

class dog:  # dog class is defined
    def __init__(self,name,weight): # init method to initialize object attributes
        self.name = name
        self.weight = weight

dog1 = dog("dog", "buddy") # dog1 is an object of animal class
print(dog1.species)  # to get the species of dog1
print('\n',dog1.name) # to get the name of dog1
