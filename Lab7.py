#Task 1
import Lab3
import Lab5

my_places = ["New York","Miami","Port Louis","Santorino"]
print(my_places)
#print(sorted(my_places))  #sorted is used for temporary sort, alphabetical order without modifying the actual list.
print(sorted(my_places))
print(my_places)

print(sorted(my_places, reverse=True))
print(my_places)

my_places.reverse()
print(my_places)


my_places.reverse()
print(my_places)

my_places.sort()
print(my_places)

my_places.sort(reverse=True)
print(my_places)

#Total number of my guest - From Lab5.py
my_guests = len(Lab5.my_guests)
print(my_guests)

