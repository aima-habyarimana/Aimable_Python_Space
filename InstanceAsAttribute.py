'''
When modeling something from the real world in code, you may find that
you’re adding more and more detail to a class. You’ll find that you have a
growing list of attributes and methods and that your files are becoming
lengthy. In these situations, you might recognize that part of one class can
be written as a separate class. You can break your large class into smaller
classes that work together.

For example, if we continue adding detail to the ElectricCar class, we
might notice that we’re adding many attributes and methods specific to
the car’s battery. When we see this happening, we can stop and move those
attributes and methods to a separate class called Battery. Then we can use a
Battery instance as an attribute in the ElectricCar class:'''

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car): # (Car)
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery() # Instance as attribute.


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()   # Instead of being my_tesla.describe_battery()
