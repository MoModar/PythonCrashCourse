# TRY IT YOURSELF
# 7-5. Movie Tickets:

prompt = "\nPlease enter your age :) "

age = input(prompt)
age = int(age)

if age < 3:
    print("The ticket is free :)")
elif 3 <= age <= 12:
    print("The ticket costs 10$")
else:
    print("The ticket costs 15$")
