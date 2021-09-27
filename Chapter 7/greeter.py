prompt = "If you tell us who are you, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("Congrats, you can vote!")
else:
    print("You can vote when you get a little bit older :)")

height = input("How tall are you, in cm? ")
height = int(height)
if height >= 150:
    print("Yes, you can bust a nut!")
