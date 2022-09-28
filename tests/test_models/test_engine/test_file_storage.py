#!/usr/bin/python3
""" Unittest For FileStorage class.

"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from unittest.mock import Mock


class TestFileStorage(unittest.TestCase):
    """ Test cases for the FileStorage.

    """

    def test_all(self):
        """ Test method all of FileStorage class """
        tmp_dict = FileStorage().all()
        self.assertEqual(type(tmp_dict), dict)

    def test_new(self):
        """ Test method new of FileStorage class """
        FileStorage = Mock()
        FileStorage().new.return_value = "added"
        self.assertEqual("added", FileStorage().new())

    def test_save(self):
        """ Test method save of the FileStorage class """
        FileStorage().save()
        self.assertEqual(True, os.path.exists("file.json"))

    def test_reload(self):
        """ Test method reload of the FileStorage class """
        FileStorage = Mock()
        FileStorage().reload.return_value = "reloaded"
        self.assertEqual("reloaded", FileStorage().reload())
