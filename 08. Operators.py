#Operators
print(10 + 5)
sum1 = 10 + 5
sum2 = sum1 + 25
sum3 = sum2 + sum2
print(sum1)
print(sum2)
print(sum3)
#Output
"""
15
15
40
80
"""

#Arithmetic Operators
"""
+ Addition x + y
- Subtraction x - y
* Multiplication x * y
/ Division x / y
% Modulus x % y
** Exponentiation x ** y
// Floor division x // y
"""
#Example
x = 15
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
#Output
"""
20
10
75
3.0
0
759375
3
"""

#Assignment Operators
"""
= (x = 1) (x = 1)
+= (x += 1) (x = x + 1)
-= (x -= 1) (x = x - 1)
*= (x *= 1) (x = x * 1)
/= (x /= 1) (x = x / 1)
%= (x %= 1) (x = x % 1)
//= (x //= 1) (x = x // 1)
**= (x **= 1) (x = x ** 1)
&= (x &= 1) (x = x & 1)
|= (x |= 1) (x = x | 1)
^= (x ^= 1) (x = x ^ 1)
>>= (x >>= 1) (x = x >> 1)
<<= (x <<= 1) (x = x << 1)
:= print(x := 1) (x = 1)
                 print(x)#output = 1
"""

#Walrus Operator
numbers = [1,2,3,4,5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
#Output
"""
List has 5 elements
"""

#Ternary Operator
num = 6 
x = "WEEKEND!" if num > 5 else "Workday"
print(x)
#Output
"""
WEEKEND!
"""

#Instead of Elif
num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)
#Note:Assign:
# "Fri" if num is 5
# "Sat" if num is 6
# "Sun" if num is 7
# otherwise assign "weekday":
#Output
"""
Sat
"""

#Comparison Operators
"""
== Equal x==y
!= Not Equal x != y
> Greater than x > y
< less than x < y
>= Greater than or equal to x >= y
<= Less than or equal to x <= y
"""
x = 1
y = 2
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
#Output
"""
False
True
False
True
False
True
"""

#Chaining Comparison Operators
x = 5
print(1 < x < 10)
print(1 < x and x <10)
#Output
"""
True
True
"""

#Logical Operators (Less than)
x = 5
print(x > 0 and x < 10)
#Output
"""
True
"""

#Logical Operators (Greater than)
x = 5
print(x < 5 and x > 10)
#Output
"""
False
"""

#Logical Operators (Not)
x = 5
print(not(x > 3 and x <10))
#Output
"""
False
"""

#Identify Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) 
print(x is y)
print(x == y)
#Output
"""
True
False
True
"""

#Identify Operators (Not)
x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)
#Output
"""
True
"""

#Identify Operators ((is)and(==))
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)
#Output
"""
True
False
"""

#Membership Operators
"""
(in) Return True if a sequence with the specified value is present in the object
(not in) Returns True if a sequence with the specified value is not present in the object
"""

#Membership Operators (in)
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
#Output
"""
True
"""

#Membership Operators(Not in)
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
#Output
"""
True
"""

#Membership in strings
text = "Hello world"
print("H" in text)
print("hello" in text)
print("z" not in text)
#Output
"""
True
False
True
"""

#Bitwise Operators
"""
(Operator)--(Name)--(Description)-------------------------------------------------------------------------------------------------------(Example)
    &        AND     Sets each bit to 1 if both bits are 1                                                                                x & y
    |        OR      Sets each bit to 1 if one of two bits is 1                                                                           x | y
    ^        XOR     Sets each bit to 1 if only one of two bits is 1                                                                      x ^ y
    ~        NOT     Inverts all the bits                                                                                                 ~ x
    <<  ZERO fill left shift    Shifts left by pushing zeros in from the right and left the leftmost bits fall off                        x << 2
    >>  Signed right shift      Shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off  x >> 2
"""
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
#Output
"""
2
7
5
"""

#Operator Precedence
"""
(Operator)------------------------------------(Description)
()                                             Parentheses
**                                             Exponentiation
+x -x ~x                                       Unary plus, unary minus, and bitwise NOT
* / // %                                       Multiplication, division, floor division, and modulus
+ -                                            Addition and subtraction
<< >>                                          Bitwise left and right shifts
&                                              Bitwise AND
^                                              Bitwise XOR
|                                              Bitwise OR
== != > >= < <= (is) (is not) (in) (not in)    Comparisions, identity, and membership operators
(not)                                          Logical NOT
(and)                                          AND
(or)                                           OR
"""
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
#Output
"""
0
115
"""

#Left-to-right Evaluation
print(5 + 4 - 7 + 3)
#Output
"""
5
"""