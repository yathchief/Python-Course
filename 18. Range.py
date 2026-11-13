#Creating ranges
#The range() function can be called with 1, 2, or 3 arguments, using this syntax:
"""
range(start, stop, step) 
"""

#Call range() With One Argumen
x = range(10)
print(x)
print(list(x))
#Output:
"""
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

#Call range() With Two Arguments
x = range(3, 10)
print(x)
print(list(x))
#Output:
"""
range(3, 10)
[3, 4, 5, 6, 7, 8, 9]
"""

#Call range() With Three Arguments
x = range(3, 10, 2)
print(x)
print(list(x))
#Output:
"""
range(3, 10, 2)
[3, 5, 7, 9]
"""

#Using ranges
for x in range(10):
  print(x) 
#Output:
"""
0
1
2
3
4
5
6
7
8
9
"""

#Using List to Display Ranges
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))
#Output:
"""
[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[5, 8, 11, 14, 17]
"""

#Slicing Ranges
r = range(10)
print(r[2])
print(r[:3])
#Output:
"""
2
range(0, 3)
"""

#Membership Testing
r = range(0, 10, 2)
print(list(r))
print(6 in r)
print(7 in r)
#Output:
"""
[0, 2, 4, 6, 8]
True
False
"""

#Length
r = range(0, 10, 2)
print(list(r))
print(len(r))
#Output:
"""
[0, 2, 4, 6, 8]
5
"""