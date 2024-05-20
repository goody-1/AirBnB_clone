#!/usr/bin/python3
"""
Unit tests for the base_model module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import base_model
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# test the class instantiation and attributes
class TestBaseModelInstantiation(unittest.TestCase):
    """
    Test the class instantiation and attributes
    """

    def setUp(self) -> None:
        """
        set up the resources for the tests
        """
        self.test_model1 = BaseModel()
        self.test_model2 = BaseModel()

    def tearDown(self) -> None:
        """"
        tear down the resources that were set up in the setUpClass method
        """
        del self.test_model1
        del self.test_model2

    def test_attributes(self):
        """"Test each attribute of the BaseModel class"""
        self.assertTrue(hasattr(self.test_model1, "id"))
        self.assertIs(type(self.test_model1.id), str)
        self.assertTrue(hasattr(self.test_model1, "created_at"))
        self.assertIs(type(self.test_model1.created_at), datetime)
        self.assertTrue(hasattr(self.test_model1, "updated_at"))
        self.assertIs(type(self.test_model1.updated_at), datetime)
        self.assertNotEqual(self.test_model1.id, self.test_model2.id)

        self.test_model1.save()
        timenow = datetime.now()

    # test the class's methods
    def test_init_method(self):
        """
        Test the __init__ method of the BaseModel class
        """
        self.assertTrue(hasattr(self.test_model1, "id"))
        self.assertTrue(hasattr(self.test_model1, "created_at"))
        self.assertTrue(hasattr(self.test_model1, "updated_at"))
        self.assertTrue(hasattr(self.test_model1, "save"))
        self.assertTrue(hasattr(self.test_model1, "to_dict"))

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel class
        """
        self.assertEqual(
            str(self.test_model1),
            f"[BaseModel] ({self.test_model1.id}) {self.test_model1.__dict__}"
        )

    def test_save_method(self):
        """
        Test the save method of the BaseModel class
        """
        self.test_model1.save()
        self.assertNotEqual(self.test_model1.created_at,
                            self.test_model1.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel class
        """
        dict_rep = self.test_model1.to_dict()
        self.assertTrue(type(dict_rep) is dict)
        self.assertTrue(dict_rep["__class__"] == "BaseModel")
        self.assertTrue(
            dict_rep["updated_at"] == self.test_model1.updated_at.isoformat())
        self.assertTrue(
            dict_rep["created_at"] == self.test_model1.created_at.isoformat())
        self.assertTrue(
            dict_rep["id"] == self.test_model1.id)


# test all docs
class TestBaseModelDocs(unittest.TestCase):
    """
    Tests for the BaseModel class documentation
    """
    def test_doc_file(self):
        """
        Test for the documentation in the module
        """
        self.assertTrue(len(base_model.__doc__) > 10)

    def test_doc_class(self):
        """
        Test for the class documentation
        """
        self.assertTrue(len(BaseModel.__doc__) > 10)

    def test_docs_methods(self):
        """
        Test for the methods documentation
        """
        for method in dir(BaseModel):
            self.assertTrue(len(method.__doc__) > 10)
