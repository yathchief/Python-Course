#Set
"""
Set is a collection which is unorderd, unchangeable, and unindexed. No duplicate members.
"""
#Set Methods
"""
Method---------------------------Shortcut----Description
add()                                        Adds an element to the set
clear()                                      Removes all the elements from the set
copy()                                       Returns a copy of the set
difference()                         -       Returns a set contianing the difference between two or more sets
difference_update()                  -=      Removes the items in this set that are also included in another, specified set
discard()                                    Remove the specified item
intersection()                       &       Returns a set that is the intersection of two other sets
intersection_update()                &=      Removes the items in this set that are not present in other specified sets
isdisjoint()                                 Returns True if No items of this set is present in another set
issubset()                           <=      Returns True if all items if this set is present in another set 
                                     <       Returns True if all items of this set is present in another larger set
issuperset()                         >=      Returns True if all items of another set is present in this set
                                     >       Returns True if all items of another smaller set is present in this set
pop()                                        Removes the specified from the set
remove()                                     Removes the specified element
symmetric_difference()               ^       Returns a set with the symmetric difference of two sets 
symmetrice_difference_update()       ^=      Insets the symmetric differences from this set and another
union()                              |       Return a set containing the union of sets
update()                             |=      Update the set with the union of this set and others
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)
#Output:
"""
{'cherry', 'apple', 'banana'}
"""

#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#Output:
"""
{'banana', 'cherry', 'apple'}
"""

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#Output:
"""
3
"""

#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
#Output:
"""
{'cherry', 'apple', 'banana'}
{1, 3, 5, 7, 9}
{False, True}
"""

#Type()
myset = {"apple", "banana", "cherry"}
print(type(myset))
#Output:
"""
<class 'set'>
"""

#The Set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
#Output:
"""
{'cherry', 'banana', 'apple'}
"""

#Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#Output:
"""
apple
cherry
banana
"""

#Access Items (Present)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#Note: Is print("banana" not in thisset) it for Not present in set. Result (False)
#Output:
"""
True
"""

#Add Set Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#Output:
"""
{'apple', 'cherry', 'banana', 'orange'}
"""

#Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#Output:
"""
{'apple', 'banana', 'cherry', 'pineapple', 'mango', 'papaya'}
"""

#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#Output:
"""
{'banana', 'apple', 'cherry', 'kiwi', 'orange'}
"""

#Remove Set Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Output:
"""
{'apple', 'cherry'}
"""

#Discard Set Items
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#Output:
"""
{'apple', 'cherry'}
"""

#Pop Set Items
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Output:
"""
apple
{'banana', 'cherry'}
"""

#Clear Set Items
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#Output:
"""
set()
"""

#Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#Output:
"""
apple
cherry
banana
"""

#Join Sets
"""
union() and update()             methods joins all items from both sets.
intersection()                   method keep only the duplicates.
difference()                     method keep the items from the first set that are not in the other sets.
symmetric difference()           method keeps all items except the duplicates.
"""

#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Note: can use | to join two sets. Example: set3 = set1 | set2
#Output:
"""
{1, 2, 'c', 'b', 3, 'a'}
"""

#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
#Note: can use | to join two sets. example: myset = set1 | set2 | set3 |set4
#Output:
"""
{'John', 1, 2, 3, 'b', 'banana', 'Elena', 'cherry', 'apple', 'c', 'a'}
"""

#Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
#Output:
"""
{'a', 2, 1, 3, 'c', 'b'}
"""
#Update
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#Output:
"""
{1, 2, 'b', 3, 'a', 'c'}
"""

#Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
#Note: can use & to join two sets. Example: set3 = set1 & set2
#Output:
"""
{'apple'}
"""

#Differece
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
#Note: can use - to join two sets. Example: set3 = set1 - set2
#Output:
"""
{'banana', 'cherry'}
"""

#Differece (Update)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
#Output:
"""
{'banana', 'cherry'}
"""

#Symmetric Differnces
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
#Note: can use ^ to join two sets. Example: set3 = set1 ^ set2
#Output:
"""
{'cherry', 'google', 'microsoft', 'banana'}
"""

#Symmetric Differnces (update)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
#Ouput:
"""
{'cherry', 'google', 'banana', 'microsoft'}
"""

#frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#Output:
"""
frozenset({'apple', 'cherry', 'banana'})
<class 'frozenset'>
"""

#Frozenset Methods
"""
Method------------------------Shortcut--------Description
copy()                                        Returns a shallow copy
difference()                     -            Returns a new frozenset with the difference
intersection()                   &            Returns a new frozenset with the intersection
isdisjoint()                                  Returns True if there is No intersection between two frozensets
issubset()                  (<= and <)        Returns True if this frozenset is a (proper) subset of another
issuperset()                (>= and >)        Returns True if this frozenset is a (proper) superset of another
symmetric_difference()           ^            Returns a new frozenset with the symmetric difference
union()                          |            Returns a new frozenset containing the union
"""



