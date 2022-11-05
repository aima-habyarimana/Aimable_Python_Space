# Creating a Dog class. Creating your own data type basing on real world living things/objects and
# their behaviours. Hence the name Object Oriented Programming.
class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):   #self parametter refers to the same class.
        # the leading 2 underscores and the trailing 2 underscores is a naming convention for the
        # first method be run/called in every class (instantiator).
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# Creating Class Instances
my_dog = Dog('willie', 6)   #my_dog is an instance (user-defined data type) created using Dog class.
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

'''When Python reads this line, it calls the __init__() method
in Dog with the arguments 'willie' and 6. The __init__() method creates an
instance representing this particular dog and sets the name and age attributes
using the values we provided. The __init__() method has no explicit return
statement, but Python automatically returns an instance representing this
dog.'''

'''We store that instance in the variable my_dog. The naming convention is
helpful here: we can usually assume that a capitalized name like Dog refers
to a class, and a lowercase name like my_dog refers to a single instance created from a class.'''

#We use dot notation to access an attribute of an instance and to call a method defined in a class.
my_dog.sit()
my_dog.roll_over()

#creating another instance of the same class (Dog class)
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()

