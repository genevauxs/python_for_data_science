class Car:

    car_nr = 0

    def __init__(self, brand, color):
        print("Hello, I'm a car")
        self.brand = brand
        self.color = color
        Car.car_nr += 1


print(Car.car_nr)
my_car = Car("Ferrari", "red")
not_my_car = Car("Lambo", "white")
print(my_car)


print(my_car.brand, my_car.color)