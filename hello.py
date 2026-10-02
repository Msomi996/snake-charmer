"""
#print("Hello, World!")
if 5 > 2:
  print("Five is greater than two!")
x = 5
#y = "Hello, World!"
#This is a comment.
#print("Hello, World!")
print("Python is fun!")
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")
#New chapter
print("Hello World!", end=" ")
print("I will print on the same line.")
#numbers
print(3)
print(358)
print(50000)
#maths
print(3 + 3)
print(2 * 5)
# combination of text and numbers
print("I am", 30, "years old.")
"""
#This is a comment
#written in
#more than just one line
#New chapter - creating variables
x = 5
y = "John"
print(x)
print(y)
"""
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
x = 5
y = "John"
print(type(x))
print(type(y))
x = "John"
# is the same as
x = 'John'
a = 4
A = "Sally"
#A will not overwrite a
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
"""
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = 5
y = 10
print(x + y)
x = "awesome"

#functions
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#global function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)

#numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
"""
# Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  txt = "The best things in life are free!"
print("expensive" not in txt)
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
