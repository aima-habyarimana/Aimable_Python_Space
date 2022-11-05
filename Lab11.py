cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


cars = ['audi', 'bmw', 'subaru', 'toyota']
print("audi" in cars)

cars = ['audi', 'bmw', 'subaru', 'toyota']
print("Mercedes" not in cars)
print(1!=1)

a = 3
b = 4
print(a>2 and b<5)
print(a>2 or b<5)

a = "Man u"
print(a != "Chelsea")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

#Python does not require an else block at the end of an if-elif chain.
age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 5
elif age < 65:
 price = 10
elif age >= 65:
 price = 5
print("Your admission cost is $" + str(price) + ".")

#### test if a list is empty or not.
cars = ['audi', 'bmw', 'subaru', 'toyota']
if cars:
    print("not empty") #this message will be printed
else:
    print("the list is empty")

cars = []
if cars:
    print("not empty") #this message will be printed
else:
    print("the list is empty")

