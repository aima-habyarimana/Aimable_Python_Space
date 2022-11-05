# Creating a file locally
'''
f = open("pi_digits.txt","w") #Note: the "w" method will open and overwrite the entire file.
print(f.write("test1\ntest2\ntest3"))  # to write in a file and at the same time display number of characters in a file.
# Reading the whole file
f = open("pi_digits.txt", "r")
print(f.read())

# Read the first 9 characters
f = open("pi_digits.txt", "r")
print(f.read(9))

# Read the 1st line
f = open("pi_digits.txt", "r")
print(f.readline())   # display "test1"

# Read 2 first lines
f = open("pi_digits.txt", "r")
print(f.readline())   # display "test1"
print(f.readline())   # display "test2"
f.close() # close the file


# append to an existing file
f = open("pi_digits.txt", "a")
f.write("\nNow the file has more content!")
f.close()

f = open("pi_digits.txt", "r")
for x in f:
  print(x)
f.close()

'''

'''
"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
'''

# import os
# os.remove("pi_digits.txt")

'''
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# remove an empty folder locally - relative path. 
import os
os.rmdir("test")
'''

# Exception Handling with try-except.
'''
Exceptions are handled with try-except blocks. A try-except block asks
Python to do something, but it also tells Python what to do if an exception is raised. When you use try-except blocks, your programs will continue
running even if things start to go wrong. Instead of tracebacks, which can
be confusing for users to read, users will see friendly error messages that
you write.
'''

#try:
# print(5/0)
#except ZeroDivisionError:
# print("You can't divide by zero!")

'''
# Using Exceptions to Prevent Crashes - ex: when a user type in wrong inputs.
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
        # answer = int(answer)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# Count the number of words in the text - use split() method.
# The split() method separates a string into parts wherever it finds a
# space and stores all the parts of the string in a list.
title = "Alice in Wonderland"
print(title.split())  # Displays ['Alice', 'in', 'Wonderland']
print(len(title))  # 19 as number of characters.

'''

'''
# Failing Silently - using Python pass statement.
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
        # answer = int(answer)
    except ZeroDivisionError:
        pass
    else:
        print(answer)


Well-written, properly tested code is not very prone to internal errors,
such as syntax or logical errors. But every time your program depends on
something external, such as user input, the existence of a file, 
or the availability of a network connection, there is a possibility of an exception being
raised.
'''



'''
The json module allows you to dump simple Python data structures into a
file and load the data from that file the next time the program runs. You can
also use json to share data between different Python programs.

# Using json.dump() and json.load()

Let’s write a short program that stores a set of numbers and another program 
that reads these numbers back into memory. The first program will
use json.dump() to store the set of numbers, and the second program will use json.load().

The json.dump() function takes two arguments: a piece of data to
store and a file object it can use to store the data. 



# 1. Program to store data in JSON file
import json
numbers = [2, 3, 5, 7, 11, 13]

f = open("'numbers.json","w")
json.dump(numbers, f)



# 2. Program to read the JSON file above.
import json
f = open("'numbers.json","r")
numbers = json.load(f)
print(numbers)
'''

# return None : it returns a null function.
'''
This is good practice: a function should either return
the value you’re expecting, or it should return None

In other situations, however, you can rely on Python's default behavior: 
If your function performs actions but doesn't have a clear and useful return value, then you can omit 
returning None because doing that would just be superfluous and confusing.

'''
