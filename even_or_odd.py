prompt = "Give me a number, and i tell you if it is even or odd."
prompt += "\nThe number is: "
number = input(prompt)
number = int(number)

if number % 2 == 0:
    print("The number is even :)")
else:
    print("The number is odd :)")