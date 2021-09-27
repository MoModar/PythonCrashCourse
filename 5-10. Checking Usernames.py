#5-10. Checking Usernames:
current_users=['abdul', 'samuel', 'dani', 'tom', 'mike']
new_users=['sami', 'fadi', 'alaa', 'Tom', 'samuel']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry, this username: " + new_user + " is unavailable!")
    else:
        print("The username is available :)")
#5-11. Ordinal Numbers:
for value in range(1,10):
    if value == 1:
        print(str(value) + "st")
    elif value == 2:
        print(str(value) + "nd")
    elif value == 3:
        print(str(value) + "rd")
    else:
        print(str(value) + "th")