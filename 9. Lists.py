#List
thislist = ["apple", "banana", "cherry"]
print(thislist)
#Output:
""" 
['apple', 'banana', 'cherry']  
"""

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#Output:
"""
['apple', 'banana', 'cherry', 'apple', 'cherry']  
"""

#List Length
thislist =["apple", "banana", "cherry"]
print(len(thislist))
#Output:
"""
3
"""

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
#Output:
"""
['apple', 'banana', 'cherry']
[1, 5, 7, 9, 3]
[True, False, False]
"""

#Type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#Output:
"""
<class 'list'>
"""

#List() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)
#Output:
"""
['apple', 'banana', 'cherry']
"""

#Acess List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Output
"""
banana
"""

#Acess List Items (Negative Indexing)
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#Output
"""
cherry
"""

#Acess List Items (Range of Indexes)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Output:
"""
['cherry', 'orange', 'kiwi']
"""

#Acess List Items (Range of Negative Indexes)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Output:
"""
['orange', 'kiwi', 'melon']
"""

#Check if Items Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruit lsit")
#Output:
"""
Yes, 'apple' is in the fruit lsit
"""

#Change List Items (Change Item Value)
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Output
"""
['apple', 'blackcurrant', 'cherry']
"""

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrent", "watermelon"]
print(thislist)
#Output:
"""
['apple', 'blackcurrent', 'watermelon', 'orange', 'kiwi', 'mango']
"""

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#Output:
"""
['apple', 'banana', 'watermelon', 'cherry']
"""

#Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Output:
"""
['apple', 'banana', 'cherry', 'orange']
"""

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Output:
"""
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
"""

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ["kiwi", "orange"]
thislist.extend(thistuple)
print(thislist)
#Output:
"""
['apple', 'banana', 'cherry', 'kiwi', 'orange']
"""

#Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Output:
"""
['apple', 'cherry']
"""

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Output:
"""
['apple', 'cherry']
"""

#Remove Specified Index(Del)
thislist = ["apple", "banana", "cherry"]
del thislist [0]
print(thislist)
#Output:
"""
['banana', 'cherry']
"""

#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#Output:
"""
[]
"""

#Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print (x)
#Output:
"""
apple
banana
cherry
"""

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range (len(thislist)):
    print(thislist[i])
#Note: Use the range() and len() functions to create a suitable iterable.
#Output:
"""
apple
banana
cherry
"""

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0 
while i < len(thislist):
    print(thislist[i])
    i = i + 1
#Output:
"""
apple
banana
cherry
"""

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#Output:
"""
apple
banana
cherry
"""

#List Comprehension
#Note: newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#Output:
"""
['apple', 'banana', 'mango']
"""

#Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#Output:
"""
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
"""

#Sort Lists(Example list numerically)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#Output:
"""
[23, 50, 65, 82, 100]
"""

#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#Output:
"""
['pineapple', 'orange', 'mango', 'kiwi', 'banana']
"""

#Sort Descending (Example list descending)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#Output:
"""
[100, 82, 65, 50, 23]
"""

#Customize Sort Function
def myfunc(n):
   return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#Output:
"""
[50, 65, 23, 82, 100]
"""

#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#Output:
"""
['Kiwi', 'Orange', 'banana', 'cherry']
"""

#Case Insensitive Sort (Perform a case-insensitive sort of the list)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#Output:
"""
['banana', 'cherry', 'Kiwi', 'Orange']
"""

#Revers Oder
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#Output:
"""
['cherry', 'Kiwi', 'Orange', 'banana']
"""

#Copy lists (copy() method)
thislist = ["apple", "banana", "cherry"]
mylsit = thislist.copy()
print(mylist)
#Output:
"""
['apple', 'banana', 'cherry']
"""

##Copy lists (list() Method)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#Output:
"""
['apple', 'banana', 'cherry']
"""

#Use the slice Operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#Output:
"""
['apple', 'banana', 'cherry']
"""

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#Output:
"""
['a', 'b', 'c', 1, 2, 3]
"""

#List Methods
"""
Method--------------Description
append()            Adds an element at the end of the list
clear()             Removes all the elements from the list
copy()              Returns a copy of the list
count()             Returns thr number of elements with the specified value
extend()            Add the elements of a list (or any iterable), to the end of the current list
index()             Returns the index of the first element with the specified value
insert()            Adds an element at the specified position
pop()               Removes the element at the specified position
remove()            Removes the item with the specified value
reverse()           Reverse the order of the list
sort()              Sorts the list
"""