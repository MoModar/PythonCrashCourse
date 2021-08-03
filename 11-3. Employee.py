""""First module"""
class Employee:
    """Simple attempts to create an 'Employee' class"""

    def __init__(self, first_name, lastname, annual_salary):
        """Initialize the class 'Employee' attributes"""

        self.firstname = first_name
        self.lastname = lastname
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Adds a rise in $5000 to a certain employee"""

        self.annual_salary += amount
        return self.annual_salary

    def show_employee_salary(self):
        """Shows an certain employee info"""

        print("This employee has " + str(self.annual_salary) + " annual salary.")

""""Second module"""
import unittest
from empl import Employee


class TestEmployee(unittest.TestCase):
    """Tests for Employee class"""

    def test_default_raise(self):
        """Tests that single raise works correctly"""

        self.new_employee = Employee('modar', 'moalla', 15000)
        self.new_employee.give_raise()

        self.assertEqual(self.new_employee.annual_salary, 20000)

    def test_custom_raise(self):
        """Tests that custom raise works correctly"""

        self.new_employee = Employee('kheder', 'assaad', 15000)
        self.new_employee.give_raise(2000)

        self.assertEqual(self.new_employee.annual_salary, 17000)


if __name__ == '__main__':
    unittest.main()
    
 """Test Results"""   
Ran 2 tests in 0.002s

OK

"""Third module"""
import unittest

from empl import Employee


class TestEmployee(unittest.TestCase):
    """Tests for Employee module"""

    def setUp(self):
        """Make instance for testing case"""
        self.new_employee = Employee('modar', 'moalla', 15000)

    def test_default_raise(self):
        """Tests that single raise works correctly"""

        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.annual_salary, 20000)

    def test_custom_raise(self):
        """Tests that custom raise works correctly"""

        self.new_employee.give_raise(2000)
        self.assertEqual(self.new_employee.annual_salary, 17000)


if __name__ == '__main__':
    unittest.main()
    
 """Test Results"""   
Ran 2 tests in 0.002s

OK
