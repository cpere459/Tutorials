"""
Title: For and While Loops with Random Numbers
Date: 09/13/2021
Author: Cindy

loops.py
"""

"""
Random Numbers:
A random number generator, really good for programmers to use to simulate luck, chance, percentages, computer choices or
to simulate probabilities
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

"""
While loops:
    1. Executes a set of statements as long as the condition is true
    2. break statement
    3. continue statement
    4. else with while loops
    
"""

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
