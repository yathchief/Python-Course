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

#Python Decorators

#Basic Decorator
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Hello Adam"
print(myfunction())
#Output:
"""
HELLO ADAM
"""

#Multiple Decorator Calls
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Hello Bob"
@changecase 
def otherfunction():
    return "I am spped!"
print(myfunction())
print(otherfunction())
#Output:
"""
HELLO BOB
I AM SPPED!
"""

#Arguments in the Decorated Function
def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner
@changecase
def myfuction(nam):
    return "Hello " + nam
print(myfuction("John"))
#Output:
"""
HELLO JOHN
"""

#*args and **kwargs
def changecase(func):
    def  myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner 
@changecase
def myfunction(nam):
    return "Hello " + nam
print(myfunction("Adam"))
#Ouput:
"""
HELLO ADAM
"""

#Decorator With Arguments
def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a 
        return myinner
    return changecase 
@changecase(1)
def myfunction():
    return "Hello Bob"
print(myfunction())
#Output:
"""
hello bob
"""

#Multiple Decorators
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
def addgreeting(func):
    def myinner():
        return "Hello " +func()  + "Hve a good day!"
    return myinner
@changecase
@addgreeting
def myfunction():
    return "Cane"
print(myfunction())
#Output:
"""
HELLO CANEHVE A GOOD DAY!
"""

#HELLO CANEHVE A GOOD DAY!
def myfunction():
    return"Have a good day!"
print(myfunction.__name__)
#Output:
"""
myfunction
"""

#Python Lambda

#Lambda Functions
x = lambda a : a +10
print(x(5))
#Output:
"""
15
"""

#Lambda with Built-in Functions (with map())
numbers =  [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)
#Output:
"""
[2, 4, 6, 8, 10]
"""

#Lambda with Built-in Functions (with filter())
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
#Output:
"""
[1, 3, 5, 7]
"""

#Lambda with Built-in Functions (with sorted())
students = [("Adam", 25), ("Bob", 22), ("Cane", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#Ouput:
"""
[('Bob', 22), ('Adam', 25), ('Cane', 28)]
"""

#Python Recursion
"""
A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument
"""

#Recursion
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)
countdown(5)
#Output:
"""
5
4
3
2
1
Done!
"""

#Base Case and Recursive Case
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))
#Output:
"""
120
"""

#Fibonacci Sequence
def fibonacci(n):
    if n  <= 1:
        return n
    else:
        return fibonacci(n -  1) + fibonacci(n - 2)
print(fibonacci(7))
#Output:
"""
13
"""

#Recursion with Lists
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
#Output:
"""
15
"""

#Recursion Depth Limit
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
#Output:
"""
2000
"""

#Python Generators

#Generators
def  my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)
#Output:
"""
1
2
3
"""

#The yield Keyword
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1
for num in count_up_to(5):
  print(num)
  #Output:
  """
  1
2
3
4
5
"""

#Generators Saves Memory
def large_sequence(n):
  for i in range(n):
    yield i
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
#Output:
"""
0
1
2
"""

#Using next() with Generators
def simple_gen():
  yield "Adam"
  yield "Bob"
  yield "Cane"
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
#Output:
"""
Adam
Bob
Cane
"""

#Generator Expressions
list_comp = [x * x for x in range(5)]
print(list_comp)
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))
#Output:
"""
[0, 1, 4, 9, 16]
<generator object <genexpr> at 0x0000022C2EF1E6C0>
[0, 1, 4, 9, 16]
"""

#Fibonacci Sequence Generator
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b
gen = fibonacci()
for _ in range(10):
  print(next(gen))
#Output:
"""
0
1
1
2
3
5
8
13
21
34
"""

#Generator Methods
def echo_generator():
  while True:
    received = yield
    print("Received:", received)
gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")
#Output:
"""
Received: Hello
Received: World
"""

##Generator Methods (close() Method)
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")
gen = my_gen()
print(next(gen))
gen.close()
#Output:
"""
1
Generator closed
"""