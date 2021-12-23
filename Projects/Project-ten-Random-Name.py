
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

number = len(names)
random = random.randint(0, number -1)
name = names[random]
print(name + " is going to pay the bill")
