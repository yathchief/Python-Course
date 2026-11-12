#Python Functions
def my_function():
    print("Hello from a function")
my_function()
#Output:
"""
Hello from a function
"""

#Calling a Function (multiple times)
def my_function():
    print("Hello from a function")
my_function()
my_function()
my_function()
my_function()
#Output:
"""
Hello from a function
Hello from a function
Hello from a function
Hello from a function
Hello from a function
"""

#Return Values
def get_greeting():
    return "Hello I'm a function"
message = get_greeting()
print(message)
#Output:
"""
Hello I'm a function
"""

#The pass Statement
def my_function():
    pass
#Note:The pass statement is often used when developing, allowing you to define the structure first and implement details later.
#Output:
"""

"""

#Arguments
def my_function(fname):
    print(fname + " Refsnes")
my_function("Adam")
my_function("Bob")
my_function("Cane")
#Output:
"""
Adam Refsnes
Bob Refsnes
Cane Refsnes
"""

#Parameters vs Arguments
def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument
"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called.
"""

#Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Adam", "Refsnes")
#Output:
"""
Adam Refsnes
""" 

#Default Parameter Values
def my_function(name = "friend"):
    print("Hello", name)
my_function('Adam')
my_function('Bob')
my_function()
my_function('Dave')
#Output:
"""
Hello Adam
Hello Bob
Hello friend
Hello Dave
"""

#Keyword Arguments
def my_function(animal, name):
    print("I have a ", animal)
    print("My", animal + "'s name is", name)
my_function(animal  = "dog",  name  =  "Kiki")
#Output:
"""
My dog's name is Kiki
"""

#Positional Arguments
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function("dog", "Cate")
#Output:
"""
I have a dog
My dog's name is Cate
"""

#Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
my_function("Dog", name = "Meow",  age  = 500 )
#Output:
"""
I have a 500 year old Dog named Meow
"""

#Passing Different Data Types
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
#Output:
"""
apple
banana
cherry
"""

#Return Values
def my_function(x, y):
    return x + y
result = my_function(5, 3)
print(result)
#Output:
"""
8
"""

#Returning Different Data Types
def my_function():
    return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
#Output:
"""
apple
banana
cherry
"""

#Positional-Only Arguments
def my_function(name, /):
    print("Hello", name)
my_function("Adam")
#Output:
"""
Hello Adam
"""

#Keyword-Only Arguments
def my_function(*, name):
    print("Hello", name)
my_function(name = "Bob")
#Output:
"""
Hello Bob
"""

#Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d ):
    return a + b  + c + d
result = my_function(5, 10, c  = 15, d = 20)
print(result)
#Output:
"""
50
"""

#Arbitrary Arguments - *args
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Adam", "Bob", "Cate")
#Output:
"""
The youngest child is Cate
"""

#Using *args with Regular Arguments
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
my_function("Hello", "Adam", "Bob", "Cane") 
#Output:
"""
Hello Adam
Hello Bob
Hello Cane
"""

#Practical Example with *args
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
#Output:
"""
6
100
5
"""

#Arbitrary Keyword Arguments - **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Adam", lname = "Refsnes")
#Output:
"""
His last name is Refsnes
"""

#Using **kwargs with Regular Arguments
def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + " : ", value)
my_function("Adam123", age = 25, city = "New York", hobby = "coding")
#Output:
"""
Username: Adam123
Additional details:
  age :  25
  city :  New York
  hobby :  coding
"""

#Combining *args and **kwargs
def my_function(tittle, *args, **kwargs):
    print("Tittle:", tittle)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
my_function("User info", "Adam", "Bob", age = 20, city = "New York")
#Output:
"""
Tittle: User info
Positional arguments: ('Adam', 'Bob')
Keyword arguments: {'age': 20, 'city': 'New York'}
"""

#Unpacking Arguments
def my_function(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers)
print(result)
#Output:
"""
6
"""

#Unpacking Dictionaries with **
def my_function(fname, lname):
    print("Hello", fname, lname)
person = {"fname": "Adam", "lname": "Refsnes"}
my_function(**person)
#Output:
"""
Hello Adam Refsnes
"""

                                                #Scope
#Local Scope
def myfunc():
    x = 100
    print(x)
myfunc()
#Output:
"""
100
"""

#Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
#Output:
"""
300
"""

#Global Scope
x = 150
def myfunc():
    print(x)
myfunc()
print(x)
#Output:
"""
150
150
"""

#Naming Variables
x = 300
def myfunc():
    x = 200 
    print(x)
myfunc()
print(x)
#Output:
"""
200
300
"""

#Global Keyword
def myfunc():
    global x
    x = 100
myfunc()
print(x)
#Output:
"""
100
"""

#Nonlocal Keyword
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "Hello"
    myfunc2()
    return x
print(myfunc1())
#Output:
"""
Hello
"""

#The LEGB Rule
x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)
outer()
print("Global:", x)
#Output:
"""
Inner: local
Outer: enclosing
Global: global
"""

#Basic Decorator
