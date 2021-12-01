print("Welcome!" '\n' + "This program will tell you how many years, days and months you have lived in your life.\n")

age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

msg = f"You have {days_remaining} day, {weeks_remaining} weeks, and {months_remaining} months left."

print(msg)

#I year = 365 days
#I year = 52 weeks
#I year = 12 months