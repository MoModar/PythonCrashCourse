#4-10.Slices:
foods=['falafel', 'pizza', 'burger', 'shawerma', 'sushi', 'fastfood']
foods.append('taco')
print(foods)
print("The first three items in the list are:")
print(foods[:3])
print("\nThree items from the middel of the list are:")
print(foods[3:])
#4-11.My Pizzas, Your Pizzas:
pizzas=['pepperoni','margarita', 'kebab']
friend_pizzas=pizzas[:]
pizzas.append('makaroni')
friend_pizzas.append('dempironi')
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("\nMy friends favorite pizzas are:")
for pizza1 in friend_pizzas:
    print(pizza1.title())
