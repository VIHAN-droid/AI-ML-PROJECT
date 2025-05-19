
class dog:  # dog class is defined
    def __init__(self,name,weight): # init method to initialize object attributes
        self.name = name
        self.weight = weight

    def __str__(self):  # when printing the obj str method is used to return the string
        return f"name is {self.name} and his weight is {self.weight}"

dog1 = dog("buddy",20)
print(dog1)
