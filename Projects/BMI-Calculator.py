print('Welcome! \n This is a BMI calculator, please let me know...\n')
print("\n ** Exemple: \n height: 1.8 \n weight: 60 **\n")
height = float(input("Your height in m: "))
weight = int(input("Your weight in kg: "))


bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
