#!/usr/bin/python3
""" Unittest for Review Class.

"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test cases for Review class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup Test Examples """
        cls.model1 = Review()

    def test_attr(self):
        """ Test attributes """
        self.assertEqual(type(self.model1.place_id), str)
        self.assertEqual(type(self.model1.user_id), str)
        self.assertEqual(type(self.model1.text), str)

    @classmethod
    def tearDownClass(cls):
        """ Destroy Test Examples """
        del cls.model1
