#Creating Variables
x = 1 #Variables in number
y = "Hello, World" #Variables in str
print(x) #Execute (X)
print(y) #Execute (Y)
#Output
"""
1
Hello, World
"""

#Duplicate type
x = 1
x = "Sally"
print(x)
#Note: Veriable will declared only last type
#Output
"""
Sally
"""

#Casting
x = str(1) #x = '1'
y = int(1) #y = 1
z = float(1) #z = 1.0
#Output
"""
1
1
1.0
"""

#Get the Type
x = 1
y = "John"
print(type(x))
print(type(y))
#Note: type() use to show types of Variable
#Output
"""
<class 'int'>
<class 'str'>
"""

#Case Sensitive
a = 1
A = "Sally"
#Output
"""
1
Sally
"""

#Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
#Output
"""
John
John
John
John
John
John
"""

 #Camel Case
myVariableName = "John" #Camel Case
print(myVariableName)
#Output
"""
John
"""

#Pascal Case
MyVariableName = "John" #Pascal Case
print(MyVariableName)
#Output
"""
John
"""

#Snake Case
my_variable_name = "John" #Snake Case
print(my_variable_name)
#Output
"""
John
"""

#Many Values to Multiple Variables
x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Output
"""
Apple
Banana
Cherry
"""

#One Value to Multiple variables
x = y = z = "Apple" 
print(x)
print(y)
print(z)
#Output
"""
Apple
Apple
Apple
"""

#Unpack a Collection
fruits = ["Apple", "Banana", "Cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
#Output
"""
Apple
Banana
Cherry
"""

#Output Variables
x = "Python is awesome"
print(x)
#Output
"""
Python is awesome
"""

#Output Variables (Multiple variables(comma))
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)
#Output
"""
Python is awesome
"""

#Output Variables (Multiple variables(Operator))
x = "Python"
y = "is"
z = "awesome"
print(x+y+z)
#Output
"""
Python is awesome
"""

#Global Variables
x = "awesome" # OUTSIDE: Global variable declaration
def myfunc(): #OUTSIDE: Function header (defines the function name)
    print("Python is" + x) #INSIDE: Function body (indented code executed when called)
    myfunc() #OUTSIDE: Function call
#Output
"""
Python is awesome
"""

#Global Variables (the same name as the global variable)
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
#Output
"""
Python is fantastic
Python is awesome
"""

#The Global Keyword (variable belongs to the global scope)
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)
#Output
"""
Python is fantastic
"""

#The Global Keyword
x ="awesome" #Global is create only local veriable (This one not show)
def myfunc():
    global x
    x = "fantastic" #Local Veriable
myfunc()
print("Python is " + x)
#Output
"""
Python is fantastic
"""
