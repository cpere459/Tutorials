"""
Title: New Content
Date: 09/07/2021
Author: Cindy

try_again.py
"""

"""
Using GitHub:
    1. Create a GitHub account
    2. Join the repository for the tutorial
    3. Pull the files from GitHub onto Pycharms
"""

"""
Arithmetic Operators:

"""

"""
Bitwise Operators:

"""

"""
Assignment Operators:

"""

"""
Identity Operators:

"""

"""
Membership Operators:

"""

"""
Type Casting:

"""

"""
Getting the Type:

"""

"""
Assigning Multiple Variables in the Same Line:

"""

"""
Assigning Multiple Variables one Value in the Same Line:

"""

"""
String Functions:

"""

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
    7. Print the user's input with the result
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
