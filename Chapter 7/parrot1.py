prompt = "Tell me somthing, and i will repeat it for you."
prompt += "\nTo end the program type 'quit'. "

active = True
while active == True:
    message = input(prompt)
    print(message)
    if message == "quit":
        active = False
