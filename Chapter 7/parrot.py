prompt = "Tell me something, and i repeat it for you"
prompt += "\nTell me 'quit' to end the program. "

# Using while loop to end the program.

#message = ""
#while message != "quit":
#    message = input(prompt)
#    print(message)

# Using a "flag" to end the program.

message = ""
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
