# from Car.car import Car, ElectricCar
import Car.car
# from Car.car import *

my_beetle = Car.car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_description())

my_tesla = Car.car.ElectricCar('tesla', 'model t', 2018)
print(my_tesla.get_description())
