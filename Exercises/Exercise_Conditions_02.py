########################
# TASK 1: if, else, elif
########################

"""
Create a simple program in which three whole numbers (potentially negative!) are read in from
the keyboard and afterwards get displayed on the screen in ascending order. Use nested if-statementsfor order determination (i.e. no built-in- 'sort' function).

num1= int(input("Enter the first whole number: "))
num2= int(input("Enter the second whole number: "))
num3= int(input("Enter the third whole number: "))

if num1>num2 and num1>num3:
    if num2>num3:
        print(num3, num2, num1, sep='\n')
    else:
        print(num2, num3, num1, sep='\n')
elif num2>num1 and num2>num3:
    if num1>num3:
        print(num3, num1, num2, sep='\n')
    else:
        print(num1, num3, num2, sep='\n')
elif num3>num1 and num3>num2:
    if num1>num2:
        print(num2, num1, num3, sep='\n')
    else:
        print(num1, num2, num3, sep='\n')
elif num3==num1 or num3==num2:
    if num1>num2:
        print(num2, num3, num1, sep='\n')
    else:
        print(num1, num3, num2, sep='\n')
elif num2 == num1 or num2==num3:
    if num1>num3:
        print(num3, num2, num1, sep='\n')
    else:
        print(num1, num2, num3, sep='\n')
"""

########################
# Task 2a: if, and-Operator, or-Operator
########################

"""
Assumption: The int variables a, b and c are declared and initialized.

Define a conditional expression "EXPR" in such a way that the body of the expression

if EXPR:
    print("condition fulfilled")

is only carried out if:
a is greater than b OR a is less than half of b OR the sum of a and c is greater than b.


Check your result:
a=1, b=2, c=2 -> True
a=1, b=2, c=1 -> False
"""
a = 1
b = 2
c = 1

if a >= b or a < b/2 or a+c > b:
    print("condition fulfilled")
else:
    print("Task 2 False")

########################
# Task 2b: if, and-Operator, or-Operator
########################

"""
Assumption: The int variables a, b and c are declared and initialized.

Define a conditional expression "EXPR" in such a way that the body of the expression

if EXPR:
    print("condition fulfilled")

is only carried out if:
half of the number a is an odd number OR the subtraction of the numbers b and c results in an even number OR both a and b and also b and c have different values.

Check your result:
a=6, b=2, c=0 => True
a=5, b=2, c=1 => True
a=5, b=5, c=2 => False
"""
a, b, c = 5, 5, 2
print(a/2 % 2 == False)
print(not (b-c)%2 == True)
print((a!=b and b!=c) == True)
if (a/2) % 2 == 0 or (b-c)%2 == 0 or (a!=b and b!=c):
    print("condition fulfilled")
else:
    print("Task 3 False")