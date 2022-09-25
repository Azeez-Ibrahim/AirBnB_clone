#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models import storage
import re


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

    def do_EOF(self, args):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, args):
        """Exits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, args):
        """Creates an instance."""
        if args == "" or args is None:
            print("** class name missing **")
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            b = self.classes[args]()
            b.save()
            print(b.id)

    def do_show(self, args):
        "print string __str__ of an instance based on class name"
        args = args.split()
        "expecting: args = [name, name_id]"
        if len(args) != 1:
            print("** class name missing **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if args[1] == v.id:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if args == "" or args is None:
            print("** class name missing **")
        else:
            words = args.split()
            if words[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances."""
        if args != "":
            words = args.split()
            if words[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                list_str = [
                    str(obj)
                    for key, obj in storage.all().items()
                    if type(obj).__name__ == words[0]
                ]
                print(list_str)
        else:
            list_str = [str(obj) for key, obj in storage.all().items()]
            print(list_str)

    def do_update(self, args):
        """
        Update an instance based on class name and id
        by adding or updating attribute
        Args:
            args (...): Name, id and atributes of a model
        """

        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                all_instances = storage.all()
                class_instance = "{}.{}".format(args[0], args[1])
                if class_instance not in all_instances:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr = args[2]
                    value = args[3].strip('"')
                    if hasattr(all_instances[class_instance], attr):
                        attr_type = type(getattr(all_instances[class_instance],
                                                 attr))
                        if attr_type == int:
                            setattr(all_instances[class_instance],
                                    attr, int(value))
                        elif attr_type == float:
                            setattr(all_instances[class_instance],
                                    attr, float(value))
                        elif attr_type == str:
                            setattr(all_instances[class_instance], attr, value)
                        storage.save()
                    else:
                        if value.isnumeric():
                            setattr(all_instances[class_instance],
                                    attr, int(value))
                        else:
                            setattr(all_instances[class_instance], attr, value)
                        storage.save()

    def default(self, args):
        """Methods with User.
        Args:
            args (str): Arguments passed
        """
        args_list = args.split(".")
        if args_list[0] not in self.classes or len(args_list) != 2:
            super().default(args)
        else:
            if args_list[1] == "all()":
                self.all_method(args_list[0])
            elif args_list[1] == "count()":
                print(self.count_method(args_list[0]))
            elif args_list[1][:4] == "show":
                tmp = args_list[1].split('"')
                self.do_show(args_list[0] + " " + tmp[1])
            elif args_list[1][:7] == "destroy":
                tmp = args_list[1].split('"')
                self.do_destroy(args_list[0] + " " + tmp[1])
            elif args_list[1][:6] == "update":
                if "{" not in args_list[1]:
                    tmp = args_list[1].split('"')
                else:
                    tmp = args_list[1].split("{")
                if len(tmp) == 7 and "{" not in tmp[2]:
                    self.do_update(
                        args_list[0] + " " + tmp[1] +
                        " " + tmp[3] + " " + tmp[5]
                    )
                elif len(tmp) == 5:
                    self.do_update(
                        args_list[0] + " " + tmp[1] +
                        " " + tmp[3] + " " + tmp[4][1:-1]
                    )
                else:
                    self.update_dict(
                        args_list[0] + " " + tmp[0][8:-3],
                        "{'" + tmp[1][1:-1]
                    )

    @classmethod
    def all_method(cls, class_name):
        """Print all instances 'class name'"""
        all_instances = storage.all()
        number = cls.count_method(class_name)
        count = 0
        print("[", end="")
        for key in all_instances:
            if class_name == key.split(".")[0]:
                print(all_instances[key], end="")
                if count != number - 1:
                    print(", ", end="")
                    count += 1
        print("]")

    def update_dict(self, class_id, attr_dict):
        """Update Object using Dictionary.
        Args:
            class_id (str) : Class name and unique ID
            attr_dict (str): Dictionary containing  the attributes
        """
        tmp_dict = eval(attr_dict)
        for key, value in tmp_dict.items():
            self.do_update(class_id + " " + key + " " + str(value))

    @staticmethod
    def count_method(class_name):
        """Print the number of instances of a class"""
        all_instances = storage.all()
        count = 0
        for key in all_instances:
            if class_name == key.split(".")[0]:
                count += 1
        return count


if __name__ == "__main__":
    HBNBCommand().cmdloop()
