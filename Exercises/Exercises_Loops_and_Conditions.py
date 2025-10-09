###################
# Exercise 1
###################
"""
Write a python program that constructs the following pattern using a nested for loop:

*
**
***
****
*****
****
***
**
*

HINT: print(yourstring, end="") -> the end parameter allows you to force python to stay on current line, compared to the default value of '\n'.
"""
print("Exercise 1:")
counter = 2
for i in range(10):
    if i > 5:
        i -= counter
        counter += 2
    for j in range(i):
        print("*", end="")
    print("")


###################
# Exercise 2
###################
"""
Write a python program to count the number of even and odd numbers contained in a sequence of numbers.
Example:
numbers = (1,2,3,4,5,6,7,8,9,10)
Output:
Number of even numbers: 5
Number of odd numbers: 5
"""
print("\nExercise 2:")
numbers = list(range(13))
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    if number % 2 == 1:
        odd += 1

print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")

###################
# Exercise 3
###################
"""
Write a Python program which takes two digits m (row) and n (column) as input and
generates a two-dimensional structure (e.g. nested list). The value in the i-th row and j-th column 
should be i*j.
Note :
i = 0, 1, … , m-1
j = 0, 1, … , n-1
Input Test Data - Rows = 3
Input Test Data - Columns = 4
Expected Result: [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""
print("\nExercise 3:")
row = 4
column = 4
for i in range(row):
    for j in range(column):
        print(i*j, end = " ")
    print("")

###################
# Exercise 4
###################
"""
Write a Python program to find all numbers between 200 and 500 (limits included) only containing even digits.
Correct solution: 
200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,26
8,280,282,284,286,288,400,402,404,406,408,420,422,424,426,428,440,442,444,446,
448,460,462,464,466,468,480,482,484,486,488
"""
print("\nExercise 4:")
MAXNUMBER = 500
MINNUMBER = 200
numbers = list(range(MINNUMBER, MAXNUMBER +1))
print(numbers[::2])

###################
# Exercise 5
###################
"""
Write a Python program to guess a number between 1 to 10.
First: Use the predefined code block to create a random number
Second:
The user is prompted to enter a guess. If the guess is wrong a message
"to big" or "to small" is printed to the console and the prompt (user
input) appears again until the guess is correct. If the guess is correct, "Well guessed!" will be printed and the program ends.
Extension:
The number of trials should be prompted as well: "Well done - you have tried it 4 times!"
"""
print("\nExercise 5:")
# Code block to create a random number
from random import randint
random_number = randint(1,10)
# End code block to create a random number

wrong_guess = True
counter = 0

while wrong_guess:
    guess = int(input("Guess a number between 1 and 10: "))
    counter += 1
    if guess == random_number:
        print("Well guessed!")
        print(f"Well done - you have tried it {counter} times!")
        wrong_guess = False
    if guess > random_number:
        print("to big")
    if guess < random_number:
        print("to small")

###################
# Exercise 6
###################
"""
Suppose we wish to draw a Christmas tree.
Example tree - desired height: 8
The result looks like:
     x
    xxx
   xxxxx
  xxxxxxx
 xxxxxxxxx
xxxxxxxxxxx
    xxx
    xxx

Create a program that asks the user for the height of the Christmas tree (trunk included)
and then draws the tree. The height of the trunk is always 2 and the width is 3 in case the entire height is > 5 and 1 in case the tree is smaller.
"""
print("\nExercise 6:")
total_height = int(input("How high should the tree be? "))
for i in range(total_height):
    print("")
    if total_height < 3:
        print("Christmas tree to small")
        break
    width = total_height - 3
    #printing the actual tree
    if i < total_height -2:
        for j in range(width - i):
            print(" ", end="")
        for j in range(2*i +1):
            print("*", end="")
        for j in range(width - i):
            print(" ", end="")
        continue
    else:
        if total_height > 5:
            trunk_width = 1
        else:
            trunk_width = 0
        for j in range(width - trunk_width):
            print(" ", end="")
        for j in range(2 * trunk_width + 1):
            print("*", end="")
        for j in range(width - trunk_width):
            print(" ", end="")

