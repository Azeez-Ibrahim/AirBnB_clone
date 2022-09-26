#!/usr/bin/python3
""" Unittest for City class.

"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Test Cases for City class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup Test Examples """
        cls.model1 = City()

    def test_attr(self):
        """ Test attributes of City """
        self.assertEqual(type(self.model1.name), str)
        self.assertEqual(type(self.model1.state_id), str)

    @classmethod
    def tearDownClass(cls):
        """ Destroy Test examples """
        del cls.model1
