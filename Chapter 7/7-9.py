# TRY IT YOURSELF.
# 7-9. No Pastrami:

sandwich_orders = ['fajita', 'taco', 'pastrami', 'falafel', 'pastrami', 'shawerma', 'pastrami', 'kebab']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("The Deli has run out from Pastrami.")
while sandwich_orders:
    current_orders = sandwich_orders.pop()
    print("We have just made your " + current_orders + " sandwich.")
    finished_sandwiches.append(current_orders)

print("\nFollowing sandwiches are ready for pick up.")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())


print("---Thank you for order---")
