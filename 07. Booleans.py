#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)
#Note: In programming you often need to know if an expression is True or False.
#Output
"""
True
False
False
"""
#Boolean Values
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
#Output
"""
b is greater than a
"""

#Evaluate Values and Veriables
x = "Hello"
y = 10
print(bool(x))
print(bool(y))
#Output
"""
True
True
"""

#Most Values are True
print(bool("abc"))
print(bool(123))
print(bool(["Apple", "Cherry", "Banana"]))
#Output
"""
True
True
True
True
True
"""

#Some Value are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
#Output
"""
False
False
False
False
False
False
False
"""

#Some Value are False
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
#Output
"""
False
"""

#Functions can Return a Boolean
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#Output
"""
YES!
"""