class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting")


class Motorcycle(Vehicle):
    def ride(self):
        print(f"{self.brand} is moving on two wheels")


bike = Motorcycle("Yamaha")

bike.start()
bike.ride()
