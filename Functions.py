import importablePizza


def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()
#########################################
def sum():
    print(7+9)
sum()
#######################################
def greet_user(username):
    print("Hello, " + username.title() + "!")
greet_user('jesse')
#############################################
def sum(a,b):
    print(a+b)
sum(5,5)
###########################################
def sum(a,b):
    print(a+b)
sum(a=5,b=5)  #this call can work as well.
###########################################
def sum2(a,b):     # a and b are parameters
    sum = a+b
    return sum
print(f"The sum of 9 plus 1 is: {sum2(9,1)}")   # 9 and 1 are arguments.
##############################################
# keyword argument: is a name-value pair that you pass to a function. setting your own default argument value.
def sum(a = 8, b=90):
    print(a+b)
sum()  # if called like sum(7,7), the new values will take precedence over default values and display 14.
#########################################################
def sum(a, b=90):   #you can simply pass default value for one parameter,
    print(a+b)
sum(a=0) # then only pass the argument for the other parameter
################################################
''' the following code will produce an error: SyntaxError: non-default argument follows default argument

Non default(ed) parameter should not follow the default(ed) parameter. 
def sum(a=3,b):   # the other way around works (a, b=90)
    print(a+b)
sum(b=10) # the other way around works (a=0)
################################################ '''
def sum(a, b=90):
    thesume = a+b
    return thesume

thesumoutside = sum(2,7)
print(thesumoutside)
#############################################
# Return a Dictionary  ######################
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('Aimable', 'Habyarimana')
print(musician)
#################################################

if 9 % 2:   #means if the remainder is a number (is not ZERO)
    print("even")   # Odd will be displayed because the remainder is 1 (is not zero).
else:
    print("odd")    #It could display Odd if we tested 8 % 2, because the remainder is Zero.

################################################
#Passing a list ################################
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['Aimable', 'Aimable', 'Habyarimana']
greet_users(usernames)

#Preventing a function from modifying a list. Make it unmutable (slice notation ofa  list) using the following statement:
# function_name(list_name[:])  in our case: greet_users(usernames[:])
################################################

#Passing an Arbitrary Number of Arguments using * . Number of argument is not known beforehand.
def make_pizza(*toppings):
 print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
########################################################

#Mixing Positional and Arbitrary Arguments
def make_pizza(size, * toppings):
 print(f"Size {size} , Toping {toppings}")

make_pizza(12,'pepperoni')
make_pizza(8, 'mushrooms', 'green peppers')
make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')
########################################################

'''The definition of build_profile() expects a first and last name, and
then it allows the user to pass in as many name-value pairs as they want. The
double asterisks before the parameter **user_info cause Python to create
an empty dictionary called user_info and pack whatever name-value pairs it
receives into this dictionary. Within the function, you can access the namevalue pairs in user_info 
just as you would for any dictionary.'''
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')

print(user_profile)

###################################################################
'''You can go a step further by
storing your functions in a separate file called a module and then importing
that module or a particular function into your main program.'''
importablePizza.make_pizza(20,'peperoni')

#######################################################
# Or use the following syntax:
from importablePizza import make_pizza
make_pizza(16, 'pepperoni')
############################################
#Using as to Give a Function an Alias
from importablePizza import make_pizza as mp
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#############################################

#Using as to Give a Module an Alias
import importablePizza as p
p.make_pizza(30, 'pepperoni')
################################

#Importing All Functions in a Module
from importablePizza import *
make_pizza(14, 'pepperoni',"cheese")
#######################################

