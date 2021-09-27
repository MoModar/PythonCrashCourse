# TRY IT YOURSELF
# Number Served:

class Restaurant():
    """Attempt to build a restaurant class"""

    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, customer_ns):
        """Pass value to the number_served attribute"""

        self.number_served = customer_ns

    def increment_number_served(self, amount):
        """Adds the given amount to the served number"""

        self.number_served += amount

    def describe_restaurant(self):
        """Prints a description"""

        print("This is a " + self.restaurant_type + " and it serves " + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        """Prints a msg whether the restaurant is open"""

        print(self.restaurant_type.title() + " is open right now!")


restaurant = Restaurant('syrian restaurant', 'eastern food')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(25)
print(restaurant.number_served)
restaurant.increment_number_served(50)
print(restaurant.number_served)
