#!/usr/bin/python3
"""
Test module for the City class.
"""

import unittest
from models.city import City
from models import city


class TestCity(unittest.TestCase):
    """
    This class contains unit tests for the City class.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.city = City()

    def test_city_instance(self):
        """
        Test if the city object is an instance of the City class.
        """
        self.assertIsInstance(self.city, City)

    def test_city_attributes(self):
        """
        Test the initial values of city attributes.
        """
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_city_attribute_types(self):
        """
        Test the types of city attributes.
        """
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_city_attribute_default_values(self):
        """
        Test the default values of city attributes.
        """
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_city_attribute_assignment(self):
        """
        Test the assignment of city attributes.
        """
        self.city.name = "New York"
        self.city.state_id = "NY"
        self.assertEqual(self.city.name, "New York")
        self.assertEqual(self.city.state_id, "NY")

    def test_city_to_dict(self):
        """
        Test the conversion of city object to a dictionary.
        """
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)

        for att in ["id", "created_at", "updated_at", "__class__"]:
            self.assertIn(att, city_dict.keys())
            self.assertTrue(type(city_dict[att]) is str)
        self.assertEqual(city_dict["__class__"], "City")

    def test_city_str_representation(self):
        """
        Test the string representation of the city object.
        """
        city_str = str(self.city)
        self.assertCountEqual(city_str, "[City] ({} {})"
                              .format(self.city.id, self.city.__dict__))


# test all docs
class TestCityModelDocs(unittest.TestCase):
    """
    Tests for the City class documentation
    """
    def test_doc_file(self):
        """
        Test for the documentation in the module
        """
        self.assertTrue(len(city.__doc__) > 10)

    def test_doc_class(self):
        """
        Test for the class documentation
        """
        self.assertTrue(len(City.__doc__) > 10)

    def test_docs_methods(self):
        """
        Test for the methods documentation
        """
        for method in dir(City):
            self.assertTrue(len(method.__doc__) > 10)


if __name__ == '__main__':
    unittest.main()
