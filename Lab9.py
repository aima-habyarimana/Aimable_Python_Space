animals = []

for i in range (0,3):
    print("Please enter the name of animal: ")
    animal = input()
    animals.append(animal)

for i in animals:
    print(i)

for i in range (1,10):
    print(i)

for i in range (1,10,2): #2 is the interval
    print(i) #1 3 5 7 9

mylist = list(range(1,10))
print(mylist)

for i in mylist:
    print(i)

print(min(mylist))
print(max(mylist))
print(sum(mylist))

for i in range (1,21):
    print (i)

million = list (range (1,1000000))
for i in million:
    print(i)
print(min(million))
print(max(million))
print(sum(million))

for i in range (1,20,2):
    print (i)


for i in range (3,30,3):
    print (i)
#A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the cube value of eache
for i in range (1,11):
    print (i**3)

comprehensive_list = []
for i in range (1,11):
    comprehensive_list.append(i**3)
    print (comprehensive_list)