# TRY It YOURSELF
# 11-1. City, Country:
"""First file 'city_function.py"""

def get_formatted_name(city, country):
    """Generate neatly formatted City-country names"""

    city_country = city.title() + ", " + country.title() + "."
    return city_country
  
  
  """Second file 'test_cities.py"""
  
  import unittest
from city_functions import get_formatted_name


class TestCityCase(unittest.TestCase):
    """Tests if city_functions.py works"""

    def test_city_country(self):
        """Is get formatted works?"""

        formatted_values = get_formatted_name('damascus', 'syria')
        self.assertEqual(formatted_values, 'Damascus, Syria.')


unittest.main
