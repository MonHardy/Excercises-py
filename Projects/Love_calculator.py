print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

sacodoinferno = name1.lower()
love_name1 = (sacodoinferno.count('l') + sacodoinferno.count('o') + sacodoinferno.count('v') + sacodoinferno.count('e') )
true_name1 = (sacodoinferno.count('t') + sacodoinferno.count('r') + sacodoinferno.count('u') + sacodoinferno.count('e') )


sacodoinferno2 = name2.lower()
love_name2 = (sacodoinferno2.count('l') + sacodoinferno2.count('o') + sacodoinferno2.count('v') + sacodoinferno2.count('e') )
true_name2 = (sacodoinferno2.count('t') + sacodoinferno2.count('r') + sacodoinferno2.count('u') + sacodoinferno2.count('e') )

some1 = int(true_name1 + true_name2)
some2 = int(love_name1 + love_name2)


some3 = int(str(some1) + str(some2))
print(f"Sua afinidade é {some3}")


if some3 < 10 or some3 > 90:
  print(f"Your score is {some3}, you go together like coke and mentos.")
elif some3 >= 40 and some3 <= 50:
  print(f"Your score is {some3}, you are alright together.")
else:
  print(f"Your score is {some3}")