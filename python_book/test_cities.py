import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Test the 'city_country.py' fucntion"""

    # Start tests
    def test_caps(self):
        """Are the city and country names capitalized and separated bya comma?"""
        output = city_country('santiago', 'chile')
        self.assertEqual(output, 'Santiago, Chile')

    def test_pop(self):
        """does the function work when a population is specified?"""
        output = city_country('santiago', 'chile', population=500000)
        self.assertEqual(output, 'Santiago, Chile - population 500000')

unittest.main()
