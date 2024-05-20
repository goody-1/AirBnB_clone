#!/usr/bin/python3
"""
Test module for the User class.
"""

import unittest
from models.user import User
from models import user
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class contains unit tests for the User class.
    """

    def test_inheritance(self):
        """
        Test if User class inherits from BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_email_attribute(self):
        """
        Test the email attribute of the User class.
        """
        user = User()
        self.assertEqual(user.email, "")

        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_password_attribute(self):
        """
        Test the password attribute of the User class.
        """
        user = User()
        self.assertEqual(user.password, "")

        user.password = "password123"
        self.assertEqual(user.password, "password123")

    def test_first_name_attribute(self):
        """
        Test the first_name attribute of the User class.
        """
        user = User()
        self.assertEqual(user.first_name, "")

        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_last_name_attribute(self):
        """
        Test the last_name attribute of the User class.
        """
        user = User()
        self.assertEqual(user.last_name, "")

        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")


# test all docs
class TestUserModelDocs(unittest.TestCase):
    """
    Tests for the User class documentation
    """
    def test_doc_file(self):
        """
        Test for the documentation in the module
        """
        self.assertTrue(len(user.__doc__) > 10)

    def test_doc_class(self):
        """
        Test for the class documentation
        """
        self.assertTrue(len(User.__doc__) > 10)

    def test_docs_methods(self):
        """
        Test for the methods documentation
        """
        for method in dir(User):
            self.assertTrue(len(method.__doc__) > 10)


if __name__ == '__main__':
    unittest.main()
