class animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "sound"

# creating a sub class dog that inherits animal
class dog(animal):
    def __init__(self, name, weight):
        super().__init__(name)  # initializing parent class with its name
        self.weight = weight
    def speak(self):
        return "woof"

dog1 = dog("buddy")
print(dog1.speak())
