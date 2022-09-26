#!/usr/bin/python3
""" Unittest for Place class.

"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test cases for Place class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup Test Examples """
        cls.model1 = Place()

    def test_attr(self):
        """ Test for attributes """
        self.assertEqual(type(self.model1.city_id), str)
        self.assertEqual(type(self.model1.user_id), str)
        self.assertEqual(type(self.model1.name), str)
        self.assertEqual(type(self.model1.description), str)
        self.assertEqual(type(self.model1.number_rooms), int)
        self.assertEqual(type(self.model1.number_bathrooms), int)
        self.assertEqual(type(self.model1.max_guest), int)
        self.assertEqual(type(self.model1.price_by_night), int)
        self.assertEqual(type(self.model1.latitude), float)
        self.assertEqual(type(self.model1.longitude), float)
        self.assertEqual(type(self.model1.amenity_ids), list)

    @classmethod
    def tearDownClass(cls):
        """ Destroy Test Examples """
        del cls.model1
