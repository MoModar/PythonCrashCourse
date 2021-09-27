prompt = "\nPlease, enter the name of a city you have visited:"
prompt += "\n(Type 'quit' when you are finished) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I would like to visit " + city.title() + ".")
