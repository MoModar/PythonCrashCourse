available_toppings=['mushrooms' , 'pepperoni' , 'mozzarella' , 'extra_chees' , 'olives' , 'kebab_meat']
requested_toppings=['mushrooms' , 'fries' , 'olives']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we do not have " + requested_topping + ".")
print("\nYour Pizza is ready :)")
