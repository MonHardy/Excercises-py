rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

trio = [rock, paper, scissors]

#user
choice = int(input("What's your choice? (0 for rock, 1 for paper and 2 ffor scissors) "))
print(trio[choice])

#computer
randompc = random.randint(0, 2)
print(trio[randompc])

#user x computer
#0 = pedra
#1 = papel
#2 = tesoura
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choice == 0 and randompc == 2:
  print("You win!")
elif randompc == 0 and choice == 2:
  print("You lose")
elif randompc > choice:
  print("You lose")
elif choice > randompc:
  print("You win!")
elif randompc == choice:
  print("It's a draw")