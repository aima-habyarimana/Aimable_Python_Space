my_fav_cars = ['Range Rover SVR', 'Rolls Royce Phantom', 'Mercedes Maybach']
print(my_fav_cars[0])

my_fav_cars.insert(1,'Bentley')
print(my_fav_cars)

del my_fav_cars[0]
print(my_fav_cars)

del my_fav_cars[-1]
print(my_fav_cars)

#removes an item from the end of the list if you don't specify the index number (like my_fav_car.pop(2)) to be popped of. you can do a = my_fav_cars.pop() to store the popped name
my_fav_cars.pop()
print(my_fav_cars)

my_fav_cars.remove('Bentley')
print(my_fav_cars)