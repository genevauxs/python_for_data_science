'''
Exercise Animals:
Use the file animals.txt to read information about animals.

Part a)
For each animal, print "Hi, I'm a {animal_type} and my name is {name}!"
Solve the exercise by writing a class 'Animal' and adding a method allowing to print the requested string. Note that it is not necessary for this task, to differentiate between animal types!
'''

print("Part a): \n\n")

class Animal:

    def __init__(self, animal_type, name, age, weight, legs):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs

    def __repr__(self):
        return f"Hi, I'm a {self.animal_type} and my name is {self.name}!"



with open('../animals.csv') as f:
    for line in f.readlines()[1:]:
        animal_type = line.split(", ")[0]
        name = line.split(", ")[1]
        age = int(line.split(", ")[2])
        weight = int(line.split(", ")[3])
        legs = int(line.split(", ")[4])
        #create objects
        obj = Animal(animal_type, name, age, weight, legs)
        print(obj)

'''
Part b)
Now we are interested in the various sounds the animal types make.
Write a separate class for each animal type. Provide a method "speak", which depending on the animal type prints different sounds.
'''

print("\n\nPart b): \n\n")
class Dog(Animal):

    def __init__(self, name, age, weight, legs, animal_type = "dog"):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print(f"{super().__str__()} And I go Woof!")

class Cat(Animal):
    def __init__(self, name, age, weight, legs, animal_type = "cat"):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print(f"{super().__str__()} And I go Meow!")
class Snake(Animal):

    def __init__(self, name, age, weight, legs, animal_type = "snake"):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print(f"{super().__str__()} And I go Hiss!")

#%% solution with file loop
obj_list = []
with open('../animals.csv') as f:
    for line in f.readlines()[1:]:
        animal_type = line.split(", ")[0]
        name = line.split(", ")[1]
        age = int(line.split(", ")[2])
        weight = int(line.split(", ")[3])
        legs = int(line.split(", ")[4])
        #create objects
        if animal_type == 'dog':
            obj = Dog(name, age, weight, legs)
            obj_list.append(obj)
        if animal_type == 'cat':
            obj = Cat(name, age, weight, legs)
            obj_list.append(obj)
        if animal_type == 'snake':
            obj = Snake(name, age, weight, legs)
            obj_list.append(obj)

for elem in obj_list:
    elem.speak()
