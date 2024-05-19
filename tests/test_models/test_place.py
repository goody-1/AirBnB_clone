#!/usr/bin/python3
"""
Test module for the Place class.
"""

import unittest
from models.place import Place
from models import place


class TestPlace(unittest.TestCase):
    """
    Test case for the Place class.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.place = Place()

    def test_city_id(self):
        """
        Test the city_id attribute of the Place class.
        """
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """
        Test the user_id attribute of the Place class.
        """
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """
        Test the name attribute of the Place class.
        """
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """
        Test the description attribute of the Place class.
        """
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """
        Test the number_rooms attribute of the Place class.
        """
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """
        Test the number_bathrooms attribute of the Place class.
        """
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """
        Test the max_guest attribute of the Place class.
        """
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """
        Test the price_by_night attribute of the Place class.
        """
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """
        Test the latitude attribute of the Place class.
        """
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """
        Test the longitude attribute of the Place class.
        """
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """
        Test the amenity_ids attribute of the Place class.
        """
        self.assertEqual(self.place.amenity_ids, [])

    def test_str_representation(self):
        """
        Test the __str__ method of the Place class.
        """
        expected_str = "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)


# test all docs
class TestPlaceModelDocs(unittest.TestCase):
    """
    Tests for the Place class documentation
    """
    def test_doc_file(self):
        """
        Test for the documentation in the module
        """
        self.assertTrue(len(place.__doc__) > 10)

    def test_doc_class(self):
        """
        Test for the class documentation
        """
        self.assertTrue(len(Place.__doc__) > 10)

    def test_docs_methods(self):
        """
        Test for the methods documentation
        """
        for method in dir(Place):
            self.assertTrue(len(method.__doc__) > 10)


if __name__ == "__main__":
    unittest.main()
