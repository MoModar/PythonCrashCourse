# Try It Yourself
# 9-14. Die:

from random import randint


class Die:
    """A simple attempt to create a Die class"""

    def __init__(self, sides = 6):
        """Initialize the class Die attribute"""

        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


my_dict = Die(6)

for number in range(1,11):
    my_dict.roll_die()


for number in range(1,21):
    my_dict.roll_die()

