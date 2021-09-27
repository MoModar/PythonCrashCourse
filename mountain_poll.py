responses ={}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb? ")

    responses[name] = response

    repeat = input("\nWould you like to ask somebody else to take the poll? ")

    if repeat == "no":
        polling_active = False
        print("\n----Poll results----")
        for name, response in responses.items():
            print(name.title() + " would like to climb the " + response.title() + " mountain.")