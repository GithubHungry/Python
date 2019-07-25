"""Class for introduce car fuel and electricity"""


class Car():
    """Simple car model"""

    def __init__(self, mark, model, year):
        """Initializing car atr"""
        self.mark = mark
        self.model = model
        self.year = year
        self.odometer = 0

    def get_description(self):
        """Return pretty description"""
        pretty_description = self.mark + ", " + self.model + ", " + str(self.year)
        return pretty_description.title()

    def read_odometer(self):
        """Print value of odometer"""
        print("This car has " + str(self.odometer) + " miles on it")

    def update_odometer(self, mile):
        """Update value of odometer for new [mile] miles"""
        if mile >= self.odometer:
            self.odometer = mile
        else:
            print("You can`t roll back an odometer!")

    def increment_odometer(self, value):
        """Increment an odometer"""
        if value >= 0:
            self.odometer += value
        else:
            print("Error, you can`t!")


class Battery():
    def __init__(self, battery_size=70):
        """Initializing battery"""
        self.battery = battery_size

    def describe_battary(self):
        """Print description of a battery"""
        print("This car has a " + str(self.battery) + "-kWh battery.")

    def get_range(self):
        """Print range"""
        if self.battery == 70:
            range = 240
        elif self.battery == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " miles on full charge."
        print(message)


class ElectricCar(Car):
    """All about electric car"""

    def __init__(self, mark, model, year):
        """Initializing electric car parameters"""
        super().__init__(mark, model, year)
        self.battery = Battery()
