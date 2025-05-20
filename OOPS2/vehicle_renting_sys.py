vehicles = {"mini":[], "suv":[], "bike":[]}

class vehicle:
    def __init__(self,capacity,brand,rent,years):
        self.brand = brand
        self.__rent = rent
        self.capacity = capacity
        self.years = years
    def write_new_vehicle(self,lst):
        with open("OOPS\\data.txt","a") as f:
            if lst[0] == "car" :
                if lst[1] == "mini":
                    f.write(f"car mini 5 {lst[2]} {lst[3]} {lst[4]} {lst[5]}\n")
                    c1 = mini(lst[3],int(lst[4]),int(lst[5])) # mini
                    vehicles["mini"].append(c1)
                elif lst[1] == "suv":
                    f.write(f"car suv 7 {lst[2]} {lst[3]} {lst[4]} {lst[5]}\n")
                    c2 = suv(lst[3],int(lst[4]),int(lst[5])) # suv
                    vehicles["suv"].append(c2)
            else:
                f.write(f"bike 2 {lst[2]} {lst[3]} {lst[4]}\n")
                b1 = bike(lst[2],int(lst[3]),int(lst[4])) # bike
                vehicles["bike"].append(b1)
    def get_rent(self):
        return "undefined"

class car(vehicle):
    def __init__(self,capacity,brand,rent,years):
        super().__init__(capacity,brand,rent,years)
    def get_rent(self):
        return "undefined"

class bike(vehicle):
    def __init__(self,brand,rent,years):
        super().__init__(2,brand,rent,years)
    def get_rent(self):
        print(self.__rent)

class mini(car):
    def __init__(self,brand,rent,years):
        super().__init__(5,brand,rent,years)
    def get_rent(self):
        print(self.__rent)

class suv(car):
    def __init__(self,brand,rent,years):
        super().__init__(7,brand,rent,years)
    def get_rent(self):
        print(self.__rent)

with open("OOPS\\data.txt","r") as f:
    for line in f:
        line = line.split()
        if line[0] == "car" :
            if line[1] == "mini":
                c1 = mini(line[3],int(line[4]),int(line[5])) # mini
                vehicles["mini"].append(c1)
            else :
                c2 = suv(line[3],int(line[4]),int(line[5])) # suv
                vehicles["suv"].append(c2)
        else:
            b1 = bike(line[2],int(line[3]),int(line[4])) # bike
            vehicles["bike"].append(b1)

choice = 0
while choice != 3 :
    print("1) View all vehicles\n2) Add new vehicle\n3) Exit")
    choice = int(input())
    if choice == 1:
        with open("OOPS\\data.txt","r") as f:
            for line in f:
                print(line)
    elif choice == 2:
        type = str(input("Vehicle type: "))
        if(type == "car"):
            type2 = str(input("mini or suv? "))
            cap = str(input("Capacity of car: "))
            br = str(input("Brand name: "))
            rt = str(input("Rent per day(inr): "))
            yrs = str(input("How old the vehicle is? "))
            x = [type,type2,cap,br,rt,yrs]
            veh = vehicle(cap,br,rt,yrs)
            veh.write_new_vehicle(x)
        else:
            cap = str(input("Capacity of car: "))
            br = str(input("Brand name: "))
            rt = str(input("Rent per day(inr): "))
            yrs = str(input("How old the vehicle is? "))
            x = [type,cap,br,rt,yrs]
            veh = vehicle(cap,br,rt,yrs)
            veh.write_new_vehicle(x)
