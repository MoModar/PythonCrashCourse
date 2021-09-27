class User():
    """Defining  a class called User"""

    def __init__(self, first_name, last_name):
        """initialize first and last name  attributes"""

        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Summarize User's Info"""

        print("User's first name is: " + self.first_name.title() + ".")
        print("User's last name is: " + self.last_name.title() + ".")

    def greet_user(self):
        """Prints personalized greeting to the user"""

        print("Hello " + self.first_name.title() + " " + self.last_name.title() + ".")


user1 = User('modar', 'moalla')
"""Making an instance of User"""

user1.describe_user()
user1.greet_user()

user2 = User('zein', 'moalla')
"""Making an instance of User"""

user2.describe_user()
user2.greet_user()

user3 = User('alice', 'moalla')
"""Making an instance of User"""

user3.describe_user()
user3.greet_user()
