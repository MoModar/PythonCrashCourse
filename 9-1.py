# TRY IT YOURSELF
# 9 - 1 Restaurant:

class Restaurant():
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


restaurant = Restaurant('thai restaurant', 'thai')
"""Making an instance of the Restaurant class"""

restaurant.describe_restaurant()
restaurant.open_restaurant()


indian = Restaurant('indian restaurant', 'indian')
"""Making an instance of the Restaurant class"""
indian.describe_restaurant()

syrian = Restaurant('syrian restaurant', 'syrian')
"""Making an instance of the Restaurant class"""
syrian.describe_restaurant()

fast_food = Restaurant('burger restaurant', 'fast food')
"""Making an instance of the Restaurant class"""
fast_food.describe_restaurant()