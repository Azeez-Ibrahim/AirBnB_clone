#!/usr/bin/python3
""" Unittest for Amenity class.

"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test cases for Amenity class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup Test examples """
        cls.model1 = Amenity()

    def test_attr(self):
        """ Test attributes of Amenity """
        self.assertEqual(type(self.model1.name), str)

    @classmethod
    def tearDownClass(cls):
        """ Destroy test examples """
        del cls.model1
