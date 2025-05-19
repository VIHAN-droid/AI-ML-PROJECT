class remote:
    def __init__(self, brand):
        self.name = brand
        self.battery = self.Battery()
    
    def show(self):
        print(f"Name: {self.name}")

    class Battery:
        def __init__(self):
            self.b_name = "duracell"
            self.status = "rechargable"
        
        def display(self):
            print(f"Name: {self.b_name}\nStatus: {self.status}")


r1 = remote("samsung")
r1.show()

# create an inner class object 
b1 = r1.battery
b1.display()
