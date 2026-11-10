#Dictionaries
"""
Dictionary: is a collection which is ordered * and changeable. No duplicate members.
"""
#Dictionary Methods
"""
Method----------Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()   	Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()  	    Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()        	Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""

#Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000
}
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2000}
"""

#Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000
}
print(thisdict["brand"])
#Output:
"""
Ford
"""

#Duplicate Not Allowed
#Note: Duplicate values will overwrite existing values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000,
    "year": 2001
}
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2001}
"""

#Dictionary Length
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000,
    "year": 2001
}
print(len(thisdict))
#Output:
"""
3
"""

#Dictionary Items - Data Types
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 2000,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'electric': False, 'year': 2000, 'colors': ['red', 'white', 'blue']}
"""

#Type()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000,
    "colors": ["red", "white", "blue"]
}
print(type(thisdict))
#Ouput:
"""
<class 'dict'>
"""

#The dict() Constructor
thisdict = dict(name = "John", age = 20, country = "New York")
print(thisdict)
#Output:
"""
{'name': 'John', 'age': 20, 'country': 'New York'}
"""

#Accessing Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000
}
x = thisdict["model"]
print(x)
#Note: Get the value of the "model" key: x = thisdict.get("model")
#Ouput:
"""
Mustang
"""

#Get Keys
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000
}
x = thisdict.keys()
print(x)
#Output:
"""
dict_keys(['brand', 'model', 'year'])
"""

#Get Values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000
}
x = thisdict.values()
print(x)
#Output:
"""
dict_values(['Ford', 'Mustang', 2000])
"""

#Get Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000
}
x = thisdict.items()
print(x)
#Output:
"""
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2000)])
"""

#Check if key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Output:
"""
Yes, 'model' is one of the keys in the thisdict dictionary
"""

#Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
thisdict["year"] = 2020
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
"""

#Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
thisdict.update({"year": 2020})
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
"""

#Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
thisdict["color"] = "red"
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2000, 'color': 'red'}
"""

#Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
thisdict.update({"color": "red"})
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2000, 'color': 'red'}
"""

#Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
thisdict.pop("model")
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'year': 2000}
"""

#Removing Items (popitem())
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
thisdict.pop("model")
print(thisdict)
#Output:
"""
{'brand': 'Ford', 'year': 2000}
"""

#Removing Items (del)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
del thisdict["model"]
print(thisdict)
#Note: #this will cause an error because "thisdict" no longer exists.
#Output:
"""
{'brand': 'Ford', 'year': 2000}
"""

#Removing Items (clear())
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
thisdict.clear()
print(thisdict)
#Output:
"""
{}
"""

#Loop Through a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
for x in thisdict:
  print(x)
#Note: Print all values in the dictionary, one by one: print(thisdict[x])
#Note: You can also use the values() method to return values of a dictionary: for x in thisdict.values():
#Note: You can use the keys() method to return the keys of a dictionary: for x in thisdict.keys():
#Note: Loop through both keys and values, by using the items() method: for x, y in thisdict.items(): print(x, y)
#Output:
"""
brand
model
year
"""

#Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
mydict = thisdict.copy()
print(mydict)
#Note: Make a copy of a dictionary with the dict() function: mydict = dict(thisdict)
#Output:
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2000}
"""

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Adam",
    "year" : 2000
  },
  "child2" : {
    "name" : "Ben",
    "year" : 2001
  },
  "child3" : {
    "name" : "Colie",
    "year" : 2002
  }
}
print(myfamily)
#Note: contain the other three dictionaries: myfamily = {"child1" : child1,"child2" : child2,"child3" : child3}
#Output:
"""
{'child1': {'name': 'Adam', 'year': 2000}, 'child2': {'name': 'Ben', 'year': 2001}, 'child3': {'name': 'Colie', 'year': 2002}}
"""

#Access Items in Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Adam",
    "year" : 2000
  },
  "child2" : {
    "name" : "Ben",
    "year" : 2001
  },
  "child3" : {
    "name" : "Colie",
    "year" : 2002
  }
}
print(myfamily["child2"]["name"])
#Output:
"""
Ben
"""

#Loop Through Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Adam",
    "year" : 2000
  },
  "child2" : {
    "name" : "Ben",
    "year" : 2001
  },
  "child3" : {
    "name" : "Colie",
    "year" : 2002
  }
}
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
#Output:
"""
child1
name: Adam
year: 2000
child2
name: Ben
year: 2001
child3
name: Colie
year: 2002
"""