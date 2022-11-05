#Task 1
my_guests = ["Paul","Peter","Larry","Laura"]
#print(my_guests)
for i in my_guests:
    print(" Hi " + i.title() + ", you are invited for a dinner")


#Task 2
print(my_guests)
my_guests.remove('Larry')
print(my_guests)

my_guests.insert(1,'Lilian')
print(my_guests)

for i in my_guests:
    print(" Hi " + i.title() + ", you are invited for a dinner")

#Task 3
for i in my_guests:
    print(" Hi " + i.title() + ", just to let you know that we managed to have big table and want to add three more people")

my_guests.insert(0,'Jack')
my_guests.insert(1,'Jones')
my_guests.append("Lewis")

print(my_guests)

for i in my_guests:
    print(" Hi " + i.title() + ", you are invited for a dinner")


#Task 4
for i in my_guests:
    print(" Hi " + i.title() + ", Sorry for the short notice, we will on be able to host 2 people")

popped1 = my_guests.pop()
print('Hi ' + popped1 + ' We are sorry to inform you that your invitation for dinner has been canceled')
popped2 = my_guests.pop()
print('Hi ' + popped2 + ' We are sorry to inform you that your invitation for dinner has been canceled')
popped3 = my_guests.pop()
print('Hi ' + popped3 + ' We are sorry to inform you that your invitation for dinner has been canceled')
popped4 = my_guests.pop()
print('Hi ' + popped4 + ' We are sorry to inform you that your invitation for dinner has been canceled')
popped5 = my_guests.pop()
print('Hi ' + popped5 + ' We are sorry to inform you that your invitation for dinner has been canceled')

print(my_guests)
for i in my_guests:
    print(" Hi " + i.title() + ", you are still invited for a dinner")


print(my_guests)
del my_guests[-1]
del my_guests[0]
print(my_guests)




