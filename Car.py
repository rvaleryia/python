class Car:
    def __init__(self, brend, model, year):
        self.brend = brend
        self.model = model
        self.year = year

    def print_car_info(self):
        print("Car:", self.brend, self.model + ",", "year:", self.year)

car1 = Car('Toyota', 'Camry', 1999)
car2 = Car('BMW', 'X5', 2022)
car3 = Car('Audi', 'A5', 2011)

car1.print_car_info()
car2.print_car_info()
car3.print_car_info()

