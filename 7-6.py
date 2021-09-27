# TRY IT YOURSELF:
# 7-6. Three Exits:

prompt = "\nPlease enter your pizza toppings :)"
prompt += "\n(Please type 'quit' when you're finished!) "

# Using a flag to exit the while loop:

#active = True
#while active:
#    topping = input(prompt)
#    if topping != 'quit':
#        print("I will add " + topping.title() + " to your pizza!")
#
#    else:
#        active = False
#        print("Thank you for your order")




# Using a conditional test to stop the loop:

topping = ""

while True:
    topping = input(prompt)
    if topping == "quit":
        print("\nYour pizza will be ready in ten minutes")
        print("Thank you for your order")
    else:
        print("\nI will add " + topping.title() + " to your pizza.")

# Using a break statement to stop the while loop:
# PS: Best results:

#while True:
#    topping = input(prompt)
#    if topping == "quit":
#        print("\nYour pizza will be ready in ten minutes")
#        print("\nThank you for your order")
#        break
#    else:
#        print("\nI will add " + topping.title() + " to your pizza.")