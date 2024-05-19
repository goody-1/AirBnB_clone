#!/usr/bin/python3
"""
Test module for the Review class.
"""

import unittest
from models.review import Review
from models import review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test case for the Review class.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.review = Review()

    def test_place_id(self):
        """
        Test the place_id attribute of the Review class.
        """
        self.assertEqual(self.review.place_id, "")

        self.review.place_id = "123"
        self.assertEqual(self.review.place_id, "123")

    def test_user_id(self):
        """
        Test the user_id attribute of the Review class.
        """
        self.assertEqual(self.review.user_id, "")

        self.review.user_id = "456"
        self.assertEqual(self.review.user_id, "456")

    def test_text(self):
        """
        Test the text attribute of the Review class.
        """
        self.assertEqual(self.review.text, "")

        self.review.text = "Great place!"
        self.assertEqual(self.review.text, "Great place!")

    def test_inheritance(self):
        """
        Test if the Review class inherits from the BaseModel class.
        """
        self.assertIsInstance(self.review, BaseModel)

    def test_str_representation(self):
        """
        Test the string representation of the Review class.
        """
        self.assertEqual(str(self.review), "<Review>")

# test all docs
class TestReviewModelDocs(unittest.TestCase):
    """
    Tests for the Review class documentation
    """
    def test_doc_file(self):
        """
        Test for the documentation in the module
        """
        self.assertTrue(len(review.__doc__) > 10)

    def test_doc_class(self):
        """
        Test for the class documentation
        """
        self.assertTrue(len(Review.__doc__) > 10)

    def test_docs_methods(self):
        """
        Test for the methods documentation
        """
        for method in dir(Review):
            self.assertTrue(len(method.__doc__) > 10)

if __name__ == '__main__':
    unittest.main()
