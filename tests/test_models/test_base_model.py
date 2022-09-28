#!/usr/bin/python3
""" Unittest for BaseModel class.

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup test examples as class attributes """
        cls.model1 = BaseModel()

    def test_id(self):
        """ Test attributes of BaseModel class """
        self.assertEqual(type(self.model1), BaseModel)
        self.assertEqual(type(self.model1.id), str)
        self.assertEqual(type(self.model1.created_at), datetime)
        self.assertEqual(type(self.model1.updated_at), datetime)

    def test_save(self):
        """ Test the save method of the BaseModel """
        temp = self.model1.updated_at
        self.model1.save()
        temp_1 = self.model1.updated_at
        self.assertNotEqual(temp, temp_1)

    def test_to_dict(self):
        """ Test the to_dict method """
        temp_dict = self.model1.to_dict()
        self.assertEqual(type(temp_dict), dict)
        self.assertDictEqual(temp_dict, self.model1.to_dict())
        self.assertEqual(type(temp_dict["created_at"]), str)
        self.assertEqual(type(temp_dict["updated_at"]), str)

    def test_constructor(self):
        """ Test the init method """
        temp_dict = self.model1.to_dict()
        temp_model = BaseModel(**temp_dict)
        self.assertEqual(type(temp_model), BaseModel)
        self.assertDictEqual(temp_model.to_dict(), temp_dict)

    @classmethod
    def tearDownClass(cls):
        """ Destroy Test examples """
        del cls.model1
