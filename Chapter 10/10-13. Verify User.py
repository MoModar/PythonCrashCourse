# TRY IT YOURSELF:
# 10-13. Verify User:
# This solution was found at: https://ehmatthes.github.io/pcc_2e/solutions/chapter_10/
import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


# Here i was trying to solve this problem by using an 'if in' statement,
# but then two output would appear asking for the username!


def greet_user():
    """Greet the user by name."""

    username = get_stored_username()
    if username:
        checkout = input("Is this your name? " + username.title() + " (yes/no) ")
        if checkout == 'yes':
            print("Welcome back," + username.title() + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
