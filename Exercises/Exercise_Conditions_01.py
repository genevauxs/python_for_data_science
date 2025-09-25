########################
# TASK 1: if, else, elif
########################

"""
Write a program that asks for a number between 1 and 7. The number serves as a
substitute for a day:
1 = Monday, 2 = Tuesday, ........, 7 = Sunday

The program should display a message (depending on the input!) on the screen:
a) "You have to work ...! (for Monday to Friday)
b) "Enjoy your weekend...! (for Saturday and Sunday)
c) "Wrong input...!" (for wrong number)

e = Exception
while e != None:
    try:
        number = int(input("Enter a number between 1 and 7: "))
        e = None
    except e:
        print("Not a number \nPlease try again.")
if number < 1  or number > 7:
    print("Wrong input...!")
elif number < 6:
    print("You have to work ...!")
else:
    print("Enjoy your weekend...!")
"""
########################
# TASK 2: if, else, elif
########################

"""
You have to divide your adult customers into 4 categories depending on their age.
Currently the following rules apply:

If: 18 <= customer_age < 25, category is: 'Youth'.
If: 25 <= customer_age  < 35, category is: 'YoungAdult'.
If: 35 <= customer_age < 60, category is: 'MiddleAged'.
If: 60 <= customer_age, category is: 'Senior'.

As an example, the following output is to be generated after the user has entered the age of the
customer (e.g. 22 year ) via 'input()':

"The customer belongs to the 'Youth' category!"


age = int(input("Please enter your age:"))
category = None
if 18 <= age < 25:
    category = 'Youth'
elif 25 <= age < 35:
    category = "YoungAdult"
elif 35 <= age < 60:
    category = 'MiddleAge'
else:
    category = 'Senior'
print(f"The customer belongs to the '{category}' category!")
"""
########################
# TASK 3: if, else, elif
########################


"""
Your goal is to convert temperatures between the scales °Celsius and °Fahrenheit.

The centigrade scale, which is also called the Celsius scale, was developed by Swedish astronomer
Andres Celsius. In the centigrade scale, water freezes at 0 degrees and boils at 100 degrees.
The Fahrenheit scale was developed by the German physicist Daniel Gabriel Fahrenheit. In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.

Equation relating the scales:

 T_C = (5/9) * (T_F - 32)

where T_C is the temperature in °Celsius and T_F is the temperature in °Fahrenheit.

Write two programs that will allow you to convert temperatures
a) from celsius to fahrenheit and
b) from fahrenheit to celsius.

Think about how you can combine the two programs in one program using a special input, e.g. F45
(for fahrenheit) or C23 (celsius)
"""
temperature = input("Add a F or C to the start to signify what scale it is.\nPlease enter your temperature:")
if temperature[0] == "C":
    temperature = temperature[1:]
    fahrenheit = int(temperature) * 9 / 5 + 32
    print(f"{temperature} Celsius in Fahrenheit is: {fahrenheit}")
else:
    temperature = temperature[1:]
    celsius = 5/9 * (int(temperature) - 32)
    print(f"{temperature} Fahrenheit in Celsius is: {celsius}")