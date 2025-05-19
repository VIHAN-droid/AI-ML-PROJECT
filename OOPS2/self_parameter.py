
class dog:  # dog class is defined
    def __init__(self,name,weight): # init method to initialize object attributes
        self.name = name
        self.weight = weight

    def bark(self):  # whenever you want to use the parameters of an object include self 
        print(f"{self.name} is barking")

dog1 = dog("buddy",20)
dog1.bark()
