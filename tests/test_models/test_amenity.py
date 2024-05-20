#!/usr/bin/python3
"""Unittest for Amenity"""

import unittest
from models.amenity import Amenity
from models import amenity
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


# test all docs
class TestAmenityModelDocs(unittest.TestCase):
    """
    Tests for the Amenity class documentation
    """
    def test_doc_file(self):
        """
        Test for the documentation in the module
        """
        self.assertTrue(len(amenity.__doc__) > 10)

    def test_doc_class(self):
        """
        Test for the class documentation
        """
        self.assertTrue(len(Amenity.__doc__) > 10)

    def test_docs_methods(self):
        """
        Test for the methods documentation
        """
        for method in dir(Amenity):
            self.assertTrue(len(method.__doc__) > 10)


if __name__ == '__main__':
    unittest.main()
