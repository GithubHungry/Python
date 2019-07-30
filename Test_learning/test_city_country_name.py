from unittest import TestCase
from Test_learning.city_function import city_country_name


class TestCity_country_name(TestCase):
    def test_city_country_name(self):
        formatted_name = city_country_name('minsk', 'belarus')
        self.assertEqual(formatted_name, 'Minsk, Belarus')

    def test_name_wirh_population(self):
        formatted_name = city_country_name('minsk', 'belarus', 2000000)
        self.assertEqual(formatted_name, 'Minsk, Belarus, population: 2000000')
