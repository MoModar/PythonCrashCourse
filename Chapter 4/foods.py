foods=['falafel', 'pizza', 'burger']
friend_foods=foods[:]

print("My favorite foods ar:")
for food in foods:
    print(food)

print("\nMy friend's favorite foods are:")
for ffood in friend_foods:
    print(ffood)

foods.append('shawerma')
friend_foods.append('taco')
print(foods)
print(friend_foods)
