#!/usr/bin/python3
""" Unittest for State.

"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Test cases for State class.

    """

    @classmethod
    def setUpClass(cls):
        """ Setup Test examples """
        cls.model1 = State()

    def test_attr(self):
        """ Test attributes """
        self.assertEqual(type(self.model1.name), str)

    @classmethod
    def tearDownClass(cls):
        """ Destroy Test Examples """
        del cls.model1
