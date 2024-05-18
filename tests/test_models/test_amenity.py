#!/usr/bin/python3
"""Unittest for Amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_name_attribute(self):
        """Test if Amenity has name attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertIsInstance(amenity.name, str)

    def test_name_initial_value(self):
        """Test if Amenity name attribute is initially empty"""
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_name_assignment(self):
        """Test if Amenity name attribute can be assigned"""
        amenity = Amenity()
        amenity.name = 'Swimming Pool'
        self.assertEqual(amenity.name, 'Swimming Pool')


if __name__ == '__main__':
    unittest.main()
