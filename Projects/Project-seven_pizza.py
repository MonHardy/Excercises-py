#build a automatic pizza order program.
print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want?\nThe sizes are S, M, or L. Please, chose one: ")
add_pepperoni = input("Do you want pepperoni?\nPlease, answer Y (Yes) or N (No): ")
extra_cheese = input("Do you want extra cheese?\nPlease, answer Y (Yes) or N (No): ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
