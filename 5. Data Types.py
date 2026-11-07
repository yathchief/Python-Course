#Setting the Data Type
x = "Hello World" #str
x = 20 #int
x = 20.5 #float
x = 1j #complex
x = ["Apple", "Banana", "Cherry"] #list
x = ("Apple", "Banana", "Cherry") #tuple
x = range(1) #range
x = {"Name" : "John", "Age" : "1"} #dict
x = {"Apple", "Banana", "Cherry"} #set
x = frozenset({"Apple", "Banana", "Cherry"}) #frozenset
x = True #bool
x = b"Hello" #bytes
x = bytearray(1) #bytearray
x = memoryview(bytes(1)) #memoryview
x = None #NoneType

#Setting the Specific Data Type
x = str("Hello World") #str
x = int(20) #int
x = float(20.5) #float
x = complex(1j) #complex
x = list(("Apple", "Banana", "Cherry")) #list
x = tuple(("Apple", "Banana", "Cherry")) #tuple
x = range(1) #range
x = dict(name="John", age="1") #dict
x = set(("Apple", "Banana", "Cherry")) #set
x = frozenset(("Apple", "Banana", "Cherry")) #frozenset
x = bool(5) #bool
x = bytes(5) #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview

#Random Number
import random
print(random.randrange(1, 10))
#Output
"""
#The result is random number from 1 to 9
"""