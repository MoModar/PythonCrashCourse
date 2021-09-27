# TRY IT YOURSELF
# 9-6 Ice Cream Stand:

class Restaurant:
    """Attempt to build a restaurant class"""

    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a description"""
        print("This is a " + self.restaurant_type + " and it serves " + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        """Prints a msg whether the restaurant is open"""

        print(self.restaurant_type.title() + " is open right now!")


class IceCreamStand(Restaurant):
    """A simple attempt to create an inheritance class for the Restaurant class"""

    def __init__(self, restaurant_type, cuisine_type):
        """Initialize the parent class attributes"""

        super().__init__(restaurant_type, cuisine_type)
        """Initialize the inheritance attribute"""

        self.flavours = [ 'milk', 'strawberry', 'mango', 'chocolate' ]

    def get_flavour(self):
        """Outputs flavour dictionary"""

        print("Flavours: ")
        for flavour in self.flavours:
            print(" - " + flavour)


soft_ice = IceCreamStand('Ice Cream Shop', 'Ice Cream')
soft_ice.get_flavour()