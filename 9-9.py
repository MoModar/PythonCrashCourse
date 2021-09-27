# TRY IT YOURSELF
# 9 - 1 Battery_upgrade:

class Car:
    """An attempt to create a car"""

    def __init__(self, mark, model, year):
        """Initialize marek, model and year attributes"""

        self.mark = mark
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly descriptive name"""

        long_name = str(self.year) + " " + self.mark + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""

        print("This car has " + str(self.odometer_reading) + " mile on it.")

    def update_odometer(self, mileage):
        """Sett the odometer to the given value
        Reject the change if it attempts to roll the odometer back
        """
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer")

    def increment_odometer(self, miles):
        """Add given amount to the odometer reading"""

        self.odometer_reading += miles

    def fill_gas_thank(self):
        """Electric cars do not have gas thanks."""

        print("You do not have/need a gas thank!")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, mark, model, year):
        """Initialize attributes of the parent class"""

        super().__init__(mark, model, year)
        self.battery = Battery()


class Battery:
    """A simple attempt to model a battery"""

    def __init__(self, battery_size=70):
        """Initialize the battery attributes"""
        self.battery_size = battery_size

    def get_range(self):
        """Print a statement about the range this battery provides"""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def update_battery(self):
        """Updates capacity to 85 if it isn't"""

        if self.battery_size != 85:
            self.battery_size = 85

    def describe_battery(self):
        """Print a statement describing the battery size."""

        print("This car has a " + str(self.battery_size) + "-kwh battery.")


new_electCar = ElectricCar('audi', 'a8-e', 2022)
print(new_electCar.get_descriptive_name())
new_electCar.battery.describe_battery()
new_electCar.battery.update_battery()
new_electCar.battery.describe_battery()
