#!/usr/bin/python3
"""
Test module for the State class.
"""

import unittest
from models.state import State
from models import state
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    TestState class to test the State model.
    """

    def test_inheritance(self):
        """
        Test that State inherits from BaseModel.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """
        Test that State has the expected attributes.
        """
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertIsInstance(state.name, str)

    def test_attribute_default_values(self):
        """
        Test that State attributes have the correct default values.
        """
        state = State()
        self.assertEqual(state.name, '')

    def test_attribute_assignment(self):
        """
        Test that State attributes can be assigned correctly.
        """
        state = State()
        state.name = 'California'
        self.assertEqual(state.name, 'California')


# test all docs
class TestStateModelDocs(unittest.TestCase):
    """
    Tests for the State class documentation
    """
    def test_doc_file(self):
        """
        Test for the documentation in the module
        """
        self.assertTrue(len(state.__doc__) > 10)

    def test_doc_class(self):
        """
        Test for the class documentation
        """
        self.assertTrue(len(State.__doc__) > 10)

    def test_docs_methods(self):
        """
        Test for the methods documentation
        """
        for method in dir(State):
            self.assertTrue(len(method.__doc__) > 10)


if __name__ == '__main__':
    unittest.main()
