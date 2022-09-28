#!/usr/bin/python3
""" Unittest for the User class.

"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ Test cases for the User class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup test examples """
        cls.user1 = User()

    def test_attr(self):
        """ Test attributes of User """
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.last_name), str)
        with self.assertRaises(AttributeError):
            print(self.user1.number)

    @classmethod
    def tearDownClass(cls):
        """ Destroy test Examples """
        del cls.user1
