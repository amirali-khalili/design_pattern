class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class CarFactory:
    _instance = {}

    @classmethod
    def get_car(cls, name, color):
        key = (name, color)
        if key not in cls._instance:
            cls._instance[key] = Car(name, color)
        return cls._instance[key]


class ParkingLot:
    def __init__(self):
        self.cars = []

    def add_car(self, name, color, x, y):
        car = CarFactory.get_car(name, color)
        self.cars.append((car, (x, y)))
        print(self.cars)

    def show_parking(self):
        for car, (x, y) in self.cars:
            print(f"Car Model: {car.name}, Color: {car.color}, Spot: ({x},{y})")


a = ParkingLot()
a.add_car("Ford", "green", 1, 2)
a.add_car("Ford", "green", 2, 4)
a.show_parking()
