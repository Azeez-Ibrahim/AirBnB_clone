#!/usr/bin/python3
""" Unittest for the console.

"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """ Test cases for method in console.

    """

    def test_quit(self):
        """ Test the do_quit method """
        self.assertIs(HBNBCommand().onecmd("quit"), True)

    def test_EOF(self):
        """ Test the do_EOF method """
        self.assertIs(HBNBCommand().onecmd("EOF"), True)

    def test_help(self):
        """ Test the default help method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(type(f.getvalue()), str)
            self.assertEqual(f.getvalue(), "\nDocumented commands "
                                           "(type help <topic>):\n======"
                                           "================================"
                                           "==\nEOF  all  create  destroy"
                                           "  help  quit  show  update\n\n")

    def test_emptyline(self):
        """ Test the emptyline method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            tmp = f.getvalue()
            self.assertEqual(tmp, '')

    def test_create(self):
        """ Test the do_create method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            tmp = f.getvalue()
            tmp_list = tmp.split('-')
            self.assertEqual(len(tmp_list), 5)
            for i in tmp_list:
                self.assertEqual(i.isascii(), True)

    def test_show(self):
        """ Test the do_show method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            tmp = f.getvalue()
            self.assertEqual(tmp, "** instance id missing **\n")

    def test_destroy(self):
        """ Test do_destroy method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            tmp = f.getvalue()
            self.assertEqual(tmp, "** instance id missing **\n")

    def test_all(self):
        """ Test do_all method """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            tmp = f.getvalue()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")

    def test_update(self):
        """ Test do_update """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            tmp = f.getvalue()
            self.assertEqual(tmp, "** instance id missing **\n")

    def test_method_all(self):
        """ Test <class_name>.all() """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            tmp = f.getvalue()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], '[')
            self.assertEqual(tmp_list[-2], ']')
            HBNBCommand().onecmd("Review.all()")
            position = len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("User.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("State.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("City.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("Amenity.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")
            HBNBCommand().onecmd("Place.all()")
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            tmp_list = list(tmp)
            self.assertEqual(tmp_list[0], "[")
            self.assertEqual(tmp_list[-2], "]")

    def test_method_count(self):
        """ Test <class_name>.count() """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            tmp = int(f.getvalue().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("Review.count()")
            position = len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("User.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("Amenity.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("State.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("Place.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)
            HBNBCommand().onecmd("City.count()")
            position += len(str(tmp)) + 1
            f.seek(position)
            tmp = int(f.read().strip())
            self.assertEqual(type(tmp), int)

    def test_method_show(self):
        """ Test <class_name>.show("id") """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("567-678")')
            tmp = f.getvalue()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('User.show("6789-98765gh")')
            position = len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('State.show("6789-fghkj")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('City.show("1234-jhg")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Amenity.show("345528u-ghj987")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Review.show("0987ghj-89098")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Place.show("78jhg-ghj789")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")

    def test_method_destroy(self):
        """ Test <class_name>.destroy("id") """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy("567-678")')
            tmp = f.getvalue()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('User.destroy("6789-98765gh")')
            position = len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('State.destroy("6789-fghkj")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('City.destroy("1234-jhg")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Amenity.destroy("345528u-ghj987")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Review.destroy("0987ghj-89098")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Place.destroy("78jhg-ghj789")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")

    def test_method_update(self):
        """ Test <class_name>.update("id", "attr name", "attr value") """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("567-78", "name", "Musa")')
            tmp = f.getvalue()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('User.update("6789-98765gh", "age", 89)')
            position = len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('State.update("6789-fghkj", "place", "EKO")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('City.update("1234-jhg", "car", "BMW")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Amenity.update("34u-ghj987", "house", "VI")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Review.update("0hj-8998", "job", "doctor")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
            HBNBCommand().onecmd('Place.update("7g-gh89", "school", "OAU")')
            position += len(tmp)
            f.seek(position)
            tmp = f.read()
            self.assertEqual(tmp, "** no instance found **\n")
