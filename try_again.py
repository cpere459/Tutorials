"""
Title: Using GitHub and Operators
Date: 09/07/2021
Author: Cindy

try_again.py
"""

"""
Using GitHub:
    1. Create a GitHub account
    2. Join the repository for the tutorial from the link
    3. Pull the files from GitHub onto Pycharms
"""

"""
Arithmetic Operators:
    1. + -> simple addition (ex: 1 + 1 will return 2, this also works with strings)
    2. - -> simple subtraction (ex: 1 - 1 wil return 0)
    3. * -> simple multiplication (ex: 3 * 2 will return 6, this also works with strings)
    4. / -> simple division (ex: 4 / 2 will return 2)
    5. % -> modulus, gives the remainder of division (ex: 5 % 2 will return 1)
    6. ** -> exponent (ex: 2 ** 3 will return 8)
    7. // -> floor division, rounds result down to the nearest whole number (ex: 1.0 // 1 will return 1)
"""

"""
Assignment Operators:
    1. = -> ex: x = 5 same as x = 5
    2. += -> ex: x += 5 same as x = x + 5
    3. -= -> ex: x -= 5 same as x = x - 5
    4. *= -> ex: x *= 5 same as x = x * 5
    5. /= -> ex: x /= 5 same as x = x / 5
    6. %= -> ex: x %= 5 same as x = x % 5
    7. // -> ex: x //= 5 same as x = x // 5
    8. **= -> ex: x **= 5 same as x = x ** 5
"""

"""
Identity Operators:
    1. is -> returns True if both objects (explained later) are the exact same
    2. is not -> returns True if both objects are different
"""

# #1 ex:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is y)  # returns False because x and y are not the same object even if their contents are the same
print(x is z)  # returns True because z is an exact copy of the x object
print(x == y)  # returns True because x and ys contents are the same

# #2 ex
print(x is not y)  # returns True because x and y are not the same object
print(x is not z)  # returns False because x and y are the same exact object
print(x != y)  # returns False because x and ys contents are the same

"""
Membership Operators:
    1. in -> returns True if the sequence is in the variable
    2. not in -> returns True if the sequence is not in the variable
"""

# #1 ex:
x = 'hi'
print(x in 'hi world')  # returns True since hi appears in hi world

# #2 ex:
print(x not in 'hi world')  # returns False since hi appears in hi world

"""
Type Casting:
If you want to force cast a data type in Python you can use the type casting methods
    1. str() -> str(x) forces the variable to be a string
    2. int() -> int(x) forces the variable to be a int
    3. float() -> float(x) forces the variable to be a float
    4. list() -> list(x) forces the variable to be a list
    5. tuple() -> tuple(x) forces the variable to be a tuple
    6. dict() -> dict(x) forces the variable to be a dict
    7. set() -> set(x) forces the variable to be a set
    8. bool() -> bool(x) forces the variable to be a bool
    9. range() -> this one is a special type casting, this one is the range of numbers within the () inclusive
"""

# #1 - 8 ex:
x = str(5)
print(x)  # returns the 5, but as a string, not as an int

# #9 ex:
z = range(0, 6)
print(z)  # returns range(0, 6)

x = 1
y = 6
print(x in z)  # returns True as x is in the range
print(y in z)  # returns False as range is inclusive

"""
Getting the Type:
You can use the python method type() to get any data type.
"""

# ex:
x = 'hi'
print(type(x))  # returns <class 'str'> which means the variable is a string

"""
Assigning Multiple Variables in the Same Line:
If you want to assign multiple variables with different values in one line, you have to separate each variable
with a comma
"""
x, y, z = 1, 2, 3
print(x, y, z)  # returns 1 2 3

"""
Assigning Multiple Variables one Value in the Same Line:
If you want to assign multiple variables the same value, you can use one line and separate each variable with an =
"""

# ex:
x = y = z = 1
print(x, y, z)  # returns 1 1 1

"""
String Functions:
    1. Slicing -> slices the string (as if it were a list) to return the characters specified
    2. upper() -> returns the string in all uppercase letters
    3. lower() -> returns the string is all lowercase letters
    4. strip() -> removes any leading or trailing whitespaces (spaces)
    5. replace() -> returns the string replaced with the variable you specify
    6. split() -> returns the string as a list separated by the specified character
    7. format() -> formats the string with variables and allows for decimal specification
    8. escape characters -> if you want to put quotes or a backslash in a string, you must use / first
    9. len() -> returns the length of the string (also works for many other data types)
"""

# #1 ex:
x = 'hello world'
print(x[:4])  # returns hell

# #2 ex:
y = x.upper()
print(y)  # returns HELLO WORLD

# #3 ex:
print(y.lower())  # returns hello world

# #4 ex:
x = '           hello there! its dangerous to go alone take this!         '
y = x.strip()
print(y)

# #5 ex:
print(x.replace('h', 'j'))  # returns jello tjere! its dangerous to go alone take tjis

# #6 ex:
x = 'hello there'
print(x.split())  # returns a list with hello there

x = 'hi,there,how,are,you'
print(x.split())  # returns the whole string in a list
print(x.split(','))  # returns the string separated by a , in a list

# #7 ex:
x = 1
y = 1.00
z = 'Item @ {}, Total: {:.2f}'  # the :.2f tells the code to get 2 decimal places
print(z.format(x, y))  # returns Item @ 1, Total: 1.00

# #8 ex:
print('\'Hello world!\'')  # \' is for a quote or \" is for a double quote
print('\\Hello World\\')  # \\ is for a backslash
print('Hello World\n')  # \n is for a new line
print('\tHello world')  # \t is for a tab
print('Hello \bWorld')  # \b is for a backspace

# #9 ex:
x = 'hello world'
print(len(x))  # returns 11 because the space character is counted in the length

######################################
#             Homework               #
######################################
'''
Create a Calculator.
Requirements:
    1. Ask a user for some sort of number, and make it an int (Hint: Type cast it!)
    3. List the different arithmetic operators that can be done on floats/ints and ask for a number
       (ex: 1 -> +, 2 -> -, 3 -> *, 4 -> /, 5 -> %, 6 -> **, 7 -> //)
    4. Check to make sure the user's second input is within this range (1 - 7)
    5. Ask a user for the second number
    6. Check to make sure the user's third input either an int or a float
    7. Print the user's input with the result all in one print statement
       (ex: 1 * 1 = 1 or 1 + 3 = 4)
'''

######################################
#         Homework Answer            #
######################################
num1 = int(input('What is the first number? '))

num2 = int(input('What is the second number? '))

operator = int(input('Which operation would you like? (1 -> +, 2 -> -, 3 -> *, 4 -> /, 5 -> %, 6 -> **, 7 -> //) '))
if operator not in range(1, 8):
    print('Incorrect input. Try again.')
    quit()

if operator == 1:
    result = num1 + num2
    operatorString = '+'
elif operator == 2:
    result = num1 - num2
    operatorString = '-'
elif operator == 3:
    result = num1 * num2
    operatorString = '*'
elif operator == 4:
    result = num1 / num2
    operatorString = '/'
elif operator == 5:
    result = num1 % num2
    operatorString = '%'
elif operator == 6:
    result = num1 ** num2
    operatorString = '**'
else:
    result = num1 // num2
    operatorString = '//'

print(str(num1) + ' ' + operatorString + ' ' + str(num2) + ' = ' + str(result))
