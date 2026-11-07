#Quotes Inside Quotes
print("Hello")
print("I am")
print('John')
#Output
"""
Hello
I am
John
"""

#Assign String to a Variable
a = "Hello"
print(a)
#Output
"""
Hello
"""

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Note: Single Quotes or Double Quotes are the same
#Output
"""
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

#String are Arrays
a = "Hello"
print(a[1])
#Note: The output with the length of 1 character from H to O
#Output
"""
e 
"""

#Looping Through a String 
for x in "Apple":
    print(x)
#Output
"""
A
p
p
l
e
"""

#String Length 
a = "Hello"
print(len(a))
#Note: It count the str character
#Output
"""
5
"""

#Check String
txt = "Hello, World"
print("world" in txt)
#Note: because the (in) operator in Python is used to check whether a specific substring exists inside a larger string.
#Output
"""
True
"""

#Check String (if)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#Output
"""
Yes, 'free' is present.
"""

#Check if Not
txt = "The best things in life are free!"
print("expensive" not in txt)
#Note: Check if "expensive" is NOT present in the following text
#Output
"""
True
"""

#Slicing
b = "Hello world"
print(b[2:5])
#Output
"""
llo
"""

#Slice from the start
b = "Hello world"
print(b[:5])
#Output
"""
Hello
"""

#Slice to the end
b = "Hello world"
print(b[2:])
#Output
"""
llo world
"""

#Negative Indexing
b = "Hello world"
print(b[-5:-2])
#Output
"""
wor
"""

#Modify Strings
a = "hello world"
print(a.upper())
#Output
"""
HELLO WORLD
"""

#Lower Case
a = "HELLO WORLD"
print(a.lower())
#Output
"""
hello world
"""

#Remove Whitespace
a = " Hello world "
print(a.strip())
#Note: The strip() method removes any whitespace from the beginning or the end
#Output
"""
Hello world
"""

#Replace String
a = "Hello world"
print(a.replace("H", "J"))
#Output
"""
Jello world
"""

#Split String
a = "Hello, world"
print(a.split(","))
#Output
"""
['Hello', ' world']
"""

#String Concatenation
a = "Hello"
b = "world"
c = a + " " + b
print(c)
#Output
"""
Hello world
"""

#F-String
age = 10
txt = f"My name is John, I am {age}"
print(txt)
#Output
"""
My name is John, I am 10
"""

#Placeholders and Modifiers
price = 10
txt = f"The price is {price} dollars"
print(txt)
#Output
"""
The price is 10 dollars
"""

#Placeholders and Modifiers(2 decimals)
price = 10
txt = f"The price is {price:.2f} dollars"
print(txt)
#Output
"""
The price is 10.00 dollars
"""

#Placeholders and Modifiers(operation)
txt = f"The price is {10 * 10} dollars"
print(txt)
#Output
"""
The price is 100 dollars
"""

#Escape Character
"""
\' Single Quotes
\" Double Quotes
\\ Backlash
\n New line
\r Carriage Return
\t Tab
\b Backspace
\f Form Feed
\ooo Octal value
\xhh Hex value
"""

#Escape Character (Sample)
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#Output
"""
We are the so-called "Vikings" from the north.
"""

#String Methods
"""
capitalize() Convert the first character to upper case
casefold() Coverts string into lower case
center() Returns a centred string
count() Returns the number of times a specified value occurs in a string
encode() Returns an encoded version of the string
endswith() Returns true if the string ends with the specified value
expendtabs() sets the tab size of the string
find() Searchs the string for a specified value and return the position of where it was found
format() Formats specified value in a string
format_map() Formats specified value in a string
index() Seacrhes the string for a specified value and return the position of where it was found
isalnum() Returns true if all characters in the string are alphanumberic
isalpha() Returns true if all character in the string are in the alhabet
isacii() Returns true if all character in the string are ascii characters
isdecimal() Returns true if all character in the string are decimals
isdigit() Returns true if all character in the string are digits
isidentifier() Returns true if the string is an identifier
islower() Returns true if all charecter in the string are lower case
isnumeric() Returns tue if all character in the string are numeric
isprintable() Returns true if all character in the string are printable
isspace() Returns true if all all character in the string are whitespaces
istitle() Returns true if all character in the string are title
isupper() Returns true if all character in the string are upper case
join() Joins the elements of an iterable to the end of the string
ljust() Returns a left justified version of the string
lower() Converts a string into lower case 
lstrip() Returns a left trim version of the string
maketrans() Returns a translation table to be a used in translations
partition() Returns a tuple where the string is parted into three parts
repalce() Returns a string where a specified value is replaced with a specificed value
rfind() Searches the string for a specified value and returns the last position of where it was found
rindex() Searches the string for a specificed value and returns the last position of where it was found
rjust() Returns a right justified version of the string 
rpartition() Returns a tuple where the string is parted in the three parts
rsplit() Splits the string at the specified separator, and returns a list
rstrip() Returns a right trim version of the string
split() Splits the string at the specified separator, and returns a list
splitlines() Returns true if the string starts with the specified value
srtip() Returns a trimmed version of the string
swapcase() Swaps case, lower case becomes upper case and vice versa
title() Converts the first character of each word to upper case
translate() Returns a translates string
upper() Converts a string into upper case
zfill() Fills the string with a specified number of 0 value at the beginning
"""