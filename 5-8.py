usernames=['zein', 'modar', 'kheder', 'admin']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello " + username + " would you like some status report?")
        else:
            print("Welcome back, " + username + "! Thank you for logging in again :)")
else:
    print("We have to get users first!")