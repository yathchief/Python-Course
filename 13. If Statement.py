#Python Conditions and If statements
a = 100
b = 200
if b  > a :
    print ("B is greater than A")
#Output:
""" 
B is greater than A
"""

#Multiple Statements in If Block
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")
#Output:
"""
You are an adult
You can vote
You have full legal rights
"""

#Using Variables in Conditions
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
#Output:
"""
Welcome back!
"""

#Elif Statement
a = 33
b = 33
if b > a:
    print("B is greater than A")
elif a == b:
    print("A and B are equal")
#Output:
"""
A and B are equal
"""

#Multiple Elif Statements
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
     print("Grade: C")
elif score >= 60:
     print("Grade: D")
elif score >= 50:
     print("Grade: E")
#Output:
"""
Grade: C
"""

#Else Statementx
a = 200
b = 100
if b > a:
    print("B is greater than A")
elif a == b:
    print("S and B are equal")
else:
    print("A is greater than B")
#Output:
"""
A is greater than B
"""

#Else Without Elif
a = 200 
b = 100
if b > a:
    print("B is greater than A")
else:
    print("B is not greater than A")
#Ouput:
"""
B is not greater than A
"""

#Complete If-Elif-Else Chain
temperature = 22
if temperature > 30:
    print("It's hot ounside")
elif temperature >20:
    print("It's warm outside")
elif temperature >10:
    print("It's cool outside")
else:
    print("It's frozen outside")
#Output:
"""
It's warm outside
"""

#Else as Fallback
username = "Emil"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
#Output:
"""
Welcome, Emil!
"""

#Short Hand If
a = 5
b = 2
if a > b: 
    print("A is greater than B")
#Output:
"""
A is greater than B
"""

#Short Hand If Else
a = 2
b = 300
print("A") if a > b else print("B")
#Output:
"""
B
"""

#Assign a Value With If Else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
#Output:
"""
Bigger is 20
"""
#Multiple Conditions on One Line
a = 300
b = 300
print("A") if a > b else print("=") if a == b else print("B")
#Output:
"""
=
"""

#Practical Examples
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value", max_value)
#Output:
"""
Maximum value 20
"""

# Logical Operators (The and Operator)
a = 200
b = 30
c = 500
if a > b and c > a:
    print("Both condition are True")
#Output:
"""
Both condition are True
"""

# Logical Operators (The or Operator)
a = 200
b = 30
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
#Output:
"""
At least one of the conditions is True
"""

# Logical Operators (The not Operator)
a = 30
b = 200
if not a > b:
    print("A is not greater than B")
#Output:
"""
A is not greater than B
"""

#Combining Multiple Operators
age = 20
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")
#Output:
"""
Discount applies!
"""

#Truth Tables
#and Operator Truth Table
"""
Condition 1	---Condition 2---Result
True	                   True	             True
True	                   False	        False
False	                  True	            False
False	                  False	           False
"""
#or Operator Truth Table
"""
Condition 1---Condition 2---Result
True	                True	            True
True	                False	            True
False	               True	                True
False	               False	            False
"""

#Using Parentheses for Clarity
temperature = 20
is_raining = False
is_weekend = True
if (temperature > 15 and not is_raining) or is_weekend:
    print("Greater day for outdoor activities!")
#Output:
"""
Greater day for outdoor activities!
"""

#Using Parentheses for Clarity + Else
username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
#Output:
"""
Login successful
"""

#Nested If Statements
x = 40 
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also abvoe 20!")
    else:
        print("but not above 20.")
#Output:
"""
Above ten,
and also abvoe 20!
"""

#How Nested If Works
age = 20
has_license  = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
#Output:
"""
You can drive
"""

#Multiple Levels of Nesting
score = 80
attendance = 90
submitted = True
if score >= 60:
    if attendance >= 75:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendence")
else:
    print("Fail")
#Output:
"""
Pass with good standing
"""

#Nested If vs Logical Operators
temperature = 20
is_sunny = True
if temperature > 15:
    if is_sunny:
        print("Perfect weather!")
#Output:
"""
Perfect weather!
"""

#Nested If vs Logical Operators (and)
temperature = 25
is_sunny = True
if temperature > 20 and is_sunny:
  print("Perfect weather!")
#Output:
"""
Perfect weather!
"""

#The pass Statement
age = 20
if age < 18:
  pass #Add underage logic later
else:
  print("Access granted")
#Output:
"""
Access granted
"""

#pass with Multiple Conditions
value = 50 
if value < 0:
    print("Negative value")
elif value == 0:
    pass
else:
    print("Positive value")
#Output:
"""
Positive value
"""