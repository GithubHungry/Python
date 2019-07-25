from Car.car import ElectricCar

my_new_electric_car = ElectricCar('tesla', 'model s', 2020)
print(my_new_electric_car.get_description())
my_new_electric_car.battery.describe_battary()
my_new_electric_car.battery.get_range()
