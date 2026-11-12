#For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#Output:
"""
apple
banana
cherry
"""

#Looping Through a String
for x in "banana":
    print(x)
#Output:
"""
b
a
n
a
n
a
"""

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
#Output:
"""
apple
banana
"""

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#Output:
"""
apple
cherry
"""

#The range() Function
for x in range(6):
    print(x)
#Output:
"""
0
1
2
3
4
5
"""

#Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finnished!")
#Output:
"""
0
1
2
3
4
5
Finally finnished!
"""

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
#Output:
"""
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""

#The pass Statement
for x in [0, 1, 2]:
    pass
#Output:
"""

# having an empty for loop like this, would raise an error without the pass statement.
"""