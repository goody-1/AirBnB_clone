#!/usr/bin/python3
"""
Unit tests for the base_model module
"""
import unittest
import json
import logging
import os

from models import storage
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


class TestFileStorageAttributes(unittest.TestCase):
    """
    Test the attributes of the FileStorage class
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the resources for the tests
        """

    def setUp(self) -> None:
        """
        Set up the resources for the tests
        """
        current_dir = os.getcwd()

        # Find the project root
        project_root = find_project_root(current_dir)

        if os.path.isfile("file.json"):
            os.remove("file.json")

        self.test_storage = storage

    def tearDown(self):
        """
        Tear down the resources that were set up in the setUpClass method
        """
        current_dir = os.getcwd()

        # Find the project root
        project_root = find_project_root(current_dir)

        if os.path.isfile("file.json"):
            os.remove("file.json")

        del self.test_storage

    def test_file_json(self):
        """Test that the file "file.json" does not exists
        the first time the program is run"""

        self.assertFalse(os.path.isfile("file.json"))

    def test_file_path(self):
        """
        Test the file_path attribute of the FileStorage class
        """

        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_all_method(self):
        """
        Test the all() method of the FileStorage class
        """
        # Add some objects to the storage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.test_storage.new(obj1)
        self.test_storage.new(obj2)
        self.test_storage.save()

        # Retrieve all objects from the storage
        all_objects = self.test_storage.all()

        # Check if the objects are retrieved correctly
        self.assertEqual(len(all_objects), 2)
        self.assertIn(obj1.__class__.__name__ + "." + obj1.id, all_objects)
        self.assertIn(obj2.__class__.__name__ + "." + obj2.id, all_objects)

    def test_new_method(self):
        """
        Test the new() method of the FileStorage class
        """
        obj = BaseModel()
        self.test_storage.new(obj)
        self.assertIn(
            obj.__class__.__name__ + "." +
            obj.id, self.test_storage._FileStorage__objects
            )

    def test_save_method(self):
        """
        Test the save() method of the FileStorage class
        """
        obj = BaseModel()

        self.test_storage.new(obj)

        self.test_storage.save()

        with open(self.test_storage._FileStorage__file_path, "r") as file:
            data = json.load(file)
            self.assertIn(obj.__class__.__name__ + "." + obj.id, data)

    def test_reload_method(self):
        """
        Test the reload() method of the FileStorage class
        """
        obj = BaseModel()
        self.test_storage.new(obj)
        self.test_storage.save()
        self.test_storage._FileStorage__objects = {}

        self.test_storage.reload()

        # Check if the object is reloaded correctly
        self.assertIn(
            obj.__class__.__name__ + "." +
            obj.id, self.test_storage._FileStorage__objects
            )


# test all docs
class TestFileStorageModelDocs(unittest.TestCase):
    """
    Tests for the BaseModel class documentation
    """
    def test_doc_file(self):
        """
        Test for the documentation in the module
        """
        self.assertTrue(len(file_storage.__doc__) > 10)

    def test_doc_class(self):
        """
        Test for the class documentation
        """
        self.assertTrue(len(FileStorage.__doc__) > 10)

    def test_docs_methods(self):
        """
        Test for the methods documentation
        """
        for method in dir(FileStorage):
            self.assertTrue(len(method.__doc__) > 10)


# Helper function to find the project root
def find_project_root(
    current_path,
        targets=["README.md", "setup.py", ".git", "console.py"]):
    while current_path != os.path.dirname(current_path):
        if any(target in os.listdir(current_path) for target in targets):
            return current_path
        current_path = os.path.dirname(current_path)
    return None
