class Human:
    def __init__(self,name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        count_passengers = 0
        if self.passengers != []:
            print(f"Name of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
                count_passengers +=1
            print(f"Кількість пасажирів {count_passengers}")

        else:
            print(f"There are no passenger in {self.brand}")


nick1 = Human("Vergilius")
nick2 = Human("Dante")
nick3 = Human("Charon")
car = Auto("Mephistoteles")

car.add_passenger(nick1,nick2,nick3)


car.print_passengers_names()