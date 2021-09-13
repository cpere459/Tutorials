"""
Title: For and While Loops with Random Numbers
Date: 09/14/2021
Author: Cindy

loops.py
"""

"""
Random Numbers:
A random number generator, really good for programmers to use to simulate luck, chance, percentages, computer choices or
to simulate probabilities/statistics
"""
from random import randint, choice  # usually these go at the top of the file below the explanation of the code

# getting a random int from a range of values
x = randint(0, 10)
print(x)

# getting a random choice from a list
x = ['apple', 'banana', 'cherries']
y = choice(x)
print(y)

"""
For loops:
    1. Iterate over a sequence (like a list, set, tuple, string or dictionary)
    2. break statement
    3. continue statement
    4. iterating over the range method
    5. else with for loop
    6. nested loops
    7. pass statement
"""

# #1 ex:
for fruit in x:  # fruit is the single item in x (the for loop will go through all the stuff in the list)
    print(fruit)

# #2 ex:
for fruit in x:
    print(fruit)
    if fruit == "banana":  # if the item in the list is banana
        break  # stop going through the loop, should stop printing at banana

# #3 ex:
for fruit in x:
    if fruit == "banana":
        continue  # continue back to the top of the loop, do not print banana
    print(fruit)

# #4 ex:
for x in range(6):  # iterate over 0 to 5
    print(x)

# #5 ex:
for x in range(6):
    print(x)
else:  # when the for loop is finished
    print("Finally finished!")

# #6 ex:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:  # a nested loop, it will loop through all the options in y first, then all the options in x
        print(x, y)

# #7 ex:
for x in [0, 1, 2]:
    pass  # you can use this to keep a loop or block empty and not get any errors!

"""
While loops:
Executes a set of statements as long as the condition is true (almost all the things you can do with a for loop,
you can do with a while statement)
"""

i = 1
while i < 6:  # while i is less than 6, and not equal to 6, so from 1 to 5
    print(i)
    i += 1  # always affect the while condition towards the end of the block or else you'll have an infinite loop!

i = True
while i:  # while i is True
    print(1 + 1)
    user = input('Would you like to try again? (yes or no) ')  # ask for the user input to affect the while condition
    if user != 'yes':
        i = False

######################################
#             Homework               #
######################################
'''
Create a Random Lottery Number Generator.
Requirements:
    1. Ask a user how many lottery number's they want to generate, with a limitation of 10 numbers.
       ex: if they ask for 10 numbers, generate 10 random numbers
    2. Randomly generate the amount of numbers requested
    3. Print these random numbers generated separated with a space
    4. Ask the user if they would like to generate more numbers (Hint: use a big while loop ;) )
'''

######################################
#         Homework Answer            #
######################################
