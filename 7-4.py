# TRY IT YOURSELF:
# 7-4. Pizza toppings:
prompt = "\nPlease enter your pizza toppings :)"
prompt += "\n(Please type 'quit' when you're finished!) "

# Stopping the while loop by using a break:
#topping = ""
#while topping != 'quit':
#    topping = input(prompt)
#    print("I will add " + topping.title() + " to your pizza!")
#    if topping == 'quit':
#        print("Thank you for your order")
#        break

# Stopping the while loop by using a flag:

active = True
while active:
    topping = input(prompt)
    if topping != 'quit':
        print("I will add " + topping.title() + " to your pizza!")

    else:
        active = False
        print("Thank you for your order")

