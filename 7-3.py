# Try it yourself:
#7-3. Multiples of ten:

prompt = "Give me a number, and i tell you if it is a multiple of ten or not :)"
prompt += "\nType the number: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print("Yes sir, the number is a multiple of ten :)")
else:
    print("No sir, the number is not a multiple of ten :)")