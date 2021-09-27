# TRY IT YOURSELF
# 7-8. Deli:

sandwich_orders = ['fajita', 'taco', 'falafel', 'shawerma', 'kebab']
finished_sandwiches = []

while sandwich_orders:
    current_orders = sandwich_orders.pop()
    print("Your " + current_orders.title() + " sandwich has just been made")
    finished_sandwiches.append(current_orders)


print("\nFollowing sandwiches are ready for takeaway :)")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())