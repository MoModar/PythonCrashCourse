#TRY IT YOURSELF
# 9-7, Admin:

class User:
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


class Admin(User):
    """Simple attempt to build a son class of 'USER'"""

    def __init__(self, first_name, last_name):
        """Initialize the parent class attributes"""

        super().__init__(first_name, last_name)
        """Initialize the son class attributes"""

        self.privileges = ['add post', 'delete post']

    def show_privileges(self):
        """Print privileges value"""

        print("This user has permission which allows him to:")
        for privilege in self.privileges:
            print(" - " + privilege)


my_admin = Admin('modar', 'moalla')
my_admin.show_privileges()