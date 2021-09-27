# TRY IT YOURSELF:
# 7-10, Dream Vacation:

responses = {}
active_polling = True
while active_polling:

    name = input("Hello, what is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    responses[name] = place

    repeat = input("\nWould you like to pass the poll to someone else? (Yes/No) ")
    if repeat == "no":
        active_polling = False

print("---Poll Results---")
for name, place in responses.items():
    print(name.title() + "'s favorite vacation would be in " + place.title() + ".")