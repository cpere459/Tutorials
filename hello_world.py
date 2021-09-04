"""
Title: The Beginning
Date: 09/07/2021
Author: Cindy

hello_world.py
This file goes over the very beginning of the programming journey with Python.
"""

"""
How to print to the terminal in python:
print(x) -> where x can be anything, however anything in x must be the same type of variable (can be in '' or "")
"""

# ex:
print('hello world')
print("hello world again")

x = 1
print(x)

"""
Different variable types:
In python for all data types, you do not need to specify them. Python figures it out for you :)
    1. Strings -> "example" or 'example
    2. Tuples -> (example, example)
    3. Lists -> [example, example]
    4. Dictionaries -> {'key' : 'example'}
    5. Int -> 1
    6. Float -> 1.1
    7. Boolean -> True or False
    8. Sets -> {example, example}
    8. There are a few more but these are the beginner ones (the others are bytes and bytes arrays)
       ex: b'/x00'
"""

'''
Github and why you should use it:
    1. Repos can be public or private, very easy for anyone to see your projects
    2. Easy sharing among multiple users
    3. Easy merging code between different developers
    4. Git commands are built into Pycharm, meaning no command line commands!
    5. Easily able to track changes through the life of the project 
       (even able to go back to a previous version easily)
    6. Can use Github on any computer that has Git downloaded (or you can download it on that device)
       so you can have your project on any device
'''

"""
Different Types of Comments:
    1. """"""/'''''' This "triple quote" is called a docstring
    2. # <- This symbol is called an inline comment
"""

"""
#1 Docstring example:
This is a docstring and is usually at the top of all functions (explained later), at the top of a file
and it can be for multiple lines. Usually summarizes what the file might do, who made it, 
what arguments/parameters are needed and what is returned. There are different standards found in
settings usually.
"""

# #2 Inline example, this is only for a single line
print("hello world")  # any code after this symbol will not work, ex: print("hello world")

"""
Conditional Operators:
    1. > -> Greater than
    2. < -> Less than
    3. >= -> Greater than or equal to
    4. <= -> Less than or equal to
    5. == -> Equal to (can be used even for strings)
    6. != -> not equal to
"""

"""
Logical Operators:
    1. not -> inverse the value, ex: if the result was False, it is now True
    2. and -> returns True if both parts of the statement are true, ex: 1 < 0 or 1 > 0 will return False
    3. or -> returns True if even just one part of the statement is true, ex: 1 < 0 or 1 > 0 will return True
"""

# #1 ex:
print(not True)  # Returns False
print(not False)  # Returns True

# #2 ex:
print(True and True)  # Returns True
print(True and False)  # Returns False
print(False and False)  # Returns False

# #3 ex:
print(True or True)
print(True or False)
print(False or False)

"""
Conditional Statements:
    1. if statements -> checks to see what a statement could be. Python automatically assumes
       statements are True if not denoted, ex: if x means the same as if x == True
       The same happens on the False side, ex: if not x means the same as if x == False
    2. elif statements -> this is the same as else if in other languages. This is directly linked
       with the if statements
    3. else statements -> this statements is the exact opposite of the last if or elif statement, ex: if the if
       statement is that x is 1, if x is not 1, then the else statement will execute
"""

# #1 ex:
x = 1
if (x == 1):
    print('this is true')

if x == 1:
    print('this is also true')

# #2 ex:
if (x == 0):
    print('x is 0')
elif (x == 1):
    print('x is 1')

# #3 ex:
if (x == -1):
    print('x is -1')
elif (x == 0):
    print('x is 0')
else:
    print('x is 1')

x = True
if x:
    print('x is True')
if x == True:
    print('This is also True')

x = False
if not x:
    print('x is not True')
if x == False:
    print('This is also not True')

"""
Python's quit() method/function (explained later) forces the program to stop running, 
nothing after this method will run.
"""
quit()
print('hello world again')  # this will never run

"""
User Input:
Use the input method, works just like the print method but only on the terminal (add a space after the question 
you ask the user for a cleaner look in the terminal)
"""

# ex:
userInput = input('How are you feeling today? ')
print(userInput)

######################################
#             Homework               #
######################################
'''
Create a Rock Paper Scissors game.
Requirements:
    1. Ask a user for input from the terminal
    2. Check to make sure the user enters either rock or paper or scissors (quit out of python if it is not)
    3. Ask a second user for input from the terminal
    4. Check the second user's input (quit out of python if it is not)
    5. Check to see who won
'''

######################################
#         Homework Answer            #
######################################
user1 = input('Rock Paper or Scissors? (Case Sensitive) ')
if user1 != 'Rock' and user1 != 'Paper' and user1 != 'Scissors':
    print('Incorrect input. Try again.')
    quit()

user2 = input('User 2: Rock Paper or Scissors? (Case Sensitive) ')
if user2 != 'Rock' and user1 != 'Paper' and user1 != 'Scissors':
    print('Incorrect input. Try again.')
    quit()

if user1 == 'Rock' and user2 == 'Paper':
    print('User 2 won!')
elif user1 == 'Rock' and user2 == 'Rock':
    print('Tie!')
elif user1 == 'Rock' and user2 == 'Scissors':
    print('User 1 won!')
elif user1 == 'Paper' and user2 == 'Paper':
    print('Tie!')
elif user1 == 'Paper' and user2 == 'Rock':
    print('User 1 won!')
elif user1 == 'Paper' and user2 == 'Scissors':
    print('User 2 won!')
elif user1 == 'Scissors' and user2 == 'Paper':
    print('User 1 won!')
elif user1 == 'Scissors' and user2 == 'Rock':
    print('User 2 won!')
else:
    print('Tie!')
