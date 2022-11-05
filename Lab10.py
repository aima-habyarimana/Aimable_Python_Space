'''top_pizza = ['Margherita', 'Cheese', 'Veggie']
print(top_pizza[0:2]) #it will print margherita and cheese. same as print(top_pizza[:2])
print(top_pizza[0:3]) #it will print all 3 items
print(top_pizza[2:]) #it will only print Veggie

for pizzas in (top_pizza[2:]):
    print(pizzas)  #only print veggies
#a ngle brackets are used for list, round brackets are used for tuples.
top_pizza = ('Margherita', 'Cheese', 'Veggie')
# unlike a list, a tuple is immutable. it can't be changed throughout the program run. ex: you can't append, delete, ...

#But you can re-assign values to a tuple. the following example is possible:
top_pizza = ('Margherita', 'JUST-been-ADDED', 'Veggie')'''

top_pizza = ['Margherita', 'Cheese', 'Veggie']
otherlist = top_pizza # this is like pointing at the same memory reference address. any change to one list will be mirrored to another list

print(top_pizza)
print(otherlist)
otherlist.append("otherpizza")
print(top_pizza)
print(otherlist)

#...........
top_pizza = ['Margherita', 'Cheese', 'Veggie']
otherlist = top_pizza[:] # adding a colon in square brakets will stop using same memory reference address. change on one list will not affect the other list.

print(top_pizza)
print(otherlist)
otherlist.append("otherpizza")
print(top_pizza)
print(otherlist)


