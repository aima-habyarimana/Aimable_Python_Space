'''You don’t always have to start from scratch when writing a class. If the class
you’re writing is a specialized version of another class you wrote, you can
use inheritance. When one class inherits from another, it automatically takes
on all the attributes and methods of the first class. The original class is
called the parent class, and the new class is the child class.

Creating an instance from a child class is to
assign values to all attributes in the parent class. To do this, the __init__()
method for a child class needs help from its parent class. 

As an example, let’s model an electric car. An electric car is just a specific kind of car, so we can base our new ElectricCar class on the Car class
we wrote earlier. '''




class Car():
    """A simple attempt to represent a car."""
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

class ElectricCar(Car): # (Car)
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) # This line tells Python to call the __init__() method
                                            # from ElectricCar’s parent class, which gives an ElectricCar instance all the attributes
                                            # of its parent class.

    # Defining Attributes and Methods for the Child Class -  to differentiate the child class from the parent class.
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Overriding Methods from the Parent Class
''' 
You can override any method from the parent class that doesn’t fit what
you’re trying to model with the child class. To do this, you define a method
in the child class with the same name as the method you want to override
in the parent class. Python will disregard the parent class method and only
pay attention to the method you define in the child class.
Say the class Car had a method called fill_gas_tank(). This method is
meaningless for an all-electric vehicle, so you might want to override this
method. Here’s one way to do that: 

def ElectricCar(Car):
 --snip--
    def fill_gas_tank():   # You simply need to define it with the same name as in parent class. 
    """Electric cars don't have gas tanks."""
     print("This car doesn't need a gas tank!") '''



