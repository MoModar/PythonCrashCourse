# Try it yourself:
# 7-2. Restaurant seating:

prompt = "Hello sir, how many people are you?"
prompt += "\nType number of guests: "

number = input(prompt)
number = int(number)

if number > 8:
    print("Sorry sir, you have to wait a little bit before your table gets ready!")
else:
    print("Yor table is ready, have a good dinner sir :)")
