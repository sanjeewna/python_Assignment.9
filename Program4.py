import random

class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.distance_traveled = 0

    def drive(self):
        self.distance_traveled += self.speed

    def __str__(self):
        return f"{self.brand} {self.model}: {self.distance_traveled} km"

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.speed += random.randint(-20, 20)  # Random change of speed
            car.drive()

    def print_status(self):
        print(f"Race: {self.name}")
        print("Current Status:")
        for car in self.cars:
            print(car)
        print("")

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False

# Main program
if __name__ == "__main__":
    cars = [
        Car("Toyota", "Corolla", 100),
        Car("Ford", "Fiesta", 110),
        Car("Honda", "Civic", 95),
        Car("Chevrolet", "Camaro", 120),
        Car("Tesla", "Model S", 130),
        Car("BMW", "M3", 125),
        Car("Audi", "A4", 115),
        Car("Mercedes-Benz", "C-Class", 105),
        Car("Subaru", "Impreza", 100),
        Car("Volkswagen", "Golf", 90)
    ]

    race = Race("Grand Demolition Derby", 8000, cars)

    hour = 1
    while not race.race_finished():
        race.hour_passes()
        if hour % 10 == 0:
            race.print_status()
        hour += 1
    print("Final Status:")
    race.print_status()