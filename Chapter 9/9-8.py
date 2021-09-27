# TRY IT YOURSELF
# 9-7, Privileges:

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

        self.privileges = Privileges()


class Privileges:
    """Creating Privileges-instance class"""

    def __init__(self, admin_privileges=[]):
        """Initialize the instance class attributes"""

        self.admin_privileges = ['add post', 'delete post']

    def show_privileges(self):
        """Print privileges value"""

        print("This user has permission which allows him to:")
        for privilege in self.admin_privileges:
            print(" - " + privilege)


n_admin = Admin('kheder', 'assaad')
n_admin.privileges.show_privileges()
