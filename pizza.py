#Store info about pizza been ordered:
pizza = {'crust' : 'thick',
         'toppings' : ['mushrooms', 'extra chees'],}

#Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)