# TRY IT YOURSELF
# 9-5. Login Attempts.

class User:
    """Defining  a class called User"""

    def __init__(self, first_name, last_name):
        """initialize first and last name  attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self, amount):
        """Adds the given amount to the login_attempts"""

        self.login_attempts += amount

    def reset_login_amount(self):
        """Resets the login_amount"""

        self.login_attempts = 0
        return self.login_attempts

    def describe_user(self):
        """Summarize User's Info"""

        print("User's first name is: " + self.first_name.title() + ".")
        print("User's last name is: " + self.last_name.title() + ".")

    def greet_user(self):
        """Prints personalized greeting to the user"""

        print("Hello " + self.first_name.title() + " " + self.last_name.title() + ".")



#Making an instance of the class User:
new_user = User('modar', 'moalla')
print("Login attempts: " + str(new_user.login_attempts))
new_user.increment_login_attempts(10)
print("Login attempts: " + str(new_user.login_attempts))
new_user.increment_login_attempts(5)
print("Login attempts: " + str(new_user.login_attempts))
new_user.reset_login_amount()
print("Login attempts: " + str(new_user.login_attempts))
