#Tuple
"""
Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Output:
"""
('apple', 'banana', 'cherry')
"""

#Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#Output:
"""
('apple', 'banana', 'cherry', 'apple', 'cherry')
"""

#Tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#Output:
"""
3
"""

#Create Tuple With One item
thistuple = ("apple",)
print(type(thistuple))
#Not a tuple
thistuple = ("apple")
print(type(thistuple))
#Output:
"""
<class 'tuple'>
<class 'str'>
"""

#Create an Empty Tuple
thistuple = ()
print(type(thistuple))
#Output:
"""
<class 'tuple'>
"""

#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
#Output:
"""
('apple', 'banana', 'cherry')
(1, 5, 7, 9, 3)
(True, False, False)
"""

#The tuple() Constructor
#Note: the double round brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
#Output:
"""
('apple', 'banana', 'cherry')
"""

#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Output:
"""
banana
"""
#Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#Output:
"""
cherry
"""

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Output:
"""
('cherry', 'orange', 'kiwi')
"""

#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Output:
"""
('orange', 'kiwi', 'melon')
"""

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
#Output:
"""
Yes, 'apple' is in the fruits tuple
"""

#Update Tuples (change Tuple Values)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Output:
"""
('apple', 'kiwi', 'cherry')
"""

#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#Output:
"""
('apple', 'banana', 'cherry', 'orange')
"""

#Add Items(+=)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#Output:
"""
('apple', 'banana', 'cherry', 'orange')
"""

#Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
#Output:
"""
('banana', 'cherry')
"""

#Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#Output:
"""
apple
banana
cherry
"""

#Using Asterisk(*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#Output:
"""
apple
banana
['cherry', 'strawberry', 'raspberry']
"""

#Loop Tuples(Loop Through a Tuple)
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
#Output:
"""
apple
banana
cherry
"""

#Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range (len(thistuple)):
    print(thistuple[i])
#Output:
"""
apple
banana
cherry
"""

#Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0 
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
#Output:
"""
apple
banana
cherry
"""

#Join Tuples (Join Two Tuples)
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#Output:
"""
('a', 'b', 'c', 1, 2, 3)
"""

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#Output:
"""
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
"""

#Tuple Methods
"""
Method----------Description
count()         Returns the number of times a specified value occurs in a tuple
index()         Searches the tuple for a specified value and returns the position of where it was found
"""