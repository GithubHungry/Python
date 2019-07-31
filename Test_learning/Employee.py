class Employee():
    """Employee class"""

    def __init__(self, first_name, last_name, money):
        """Initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.money = money

    def give_raise(self, more_money=5000):
        """Raise function"""
        self.money += more_money
