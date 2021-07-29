# TRY It YOURSELF
# 11-2. Population:
"""First module 'city_function.py"""

# Modyfied with a new 'population' parameter.

def get_formatted_name(city, country, population):
    """Generate neatly formatted City-country names"""

    city_country = city.title() + ", " + country.title() + "-population" + population + "."
    return city_country


  """Second module 'test_cities.py"""

import unittest
from city_functions import get_formatted_name


class TestCityCase(unittest.TestCase):
    """Tests if city_functions.py works"""

    def test_city_country(self):
        """Is get formatted works?"""

        formatted_values = get_formatted_name('damascus', 'syria')
        self.assertEqual(formatted_values, 'Damascus, Syria.')


unittest.main
# The test fails.

# Modyfing th parameter 'population' to be an optional parameeter.
def get_formatted_name(city, country, population=0):
# The test passes after the new modification, as required.

"""First module 'city_function.py"""

def get_formatted_name(city, country, population=0):
    """Generate neatly formatted City-country names"""
    if population:
        city_country = city.title() + ", " + country.title() + "- population " + str(population) + "."
        return city_country
    else:
        city_country = city.title() + ", " + country.title() + "."
        return city_country

      
"""Second module 'test.cities.py'"""

import unittest
from city_functions import get_formatted_name


class TestCityCase(unittest.TestCase):
    """Tests if city_functions.py works"""

    def test_city_country(self):
        """Is get formatted works?"""

        formatted_values = get_formatted_name('damascus', 'syria')
        self.assertEqual(formatted_values, 'Damascus, Syria.')

    def test_city_country_population(self):
        """Tests the new 'population' parameter"""

        formatted_values = get_formatted_name('damascus', 'syria', 25000000)
        self.assertEqual(formatted_values, 'Damascus, Syria- population 25000000.')
  

  
  unittest.main
  
  # Two tests pass successfully
  
  
  
