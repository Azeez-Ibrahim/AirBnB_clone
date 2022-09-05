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
        if len(args) != 2:
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
                        attr_type = type(getattr(all_instances[class_instance], attr))
                        if attr_type == int:
                            setattr(all_instances[class_instance], attr, int(value))
                        elif attr_type == float:
                            setattr(all_instances[class_instance], attr, float(value))
                        elif attr_type == str:
                            setattr(all_instances[class_instance], attr, value)
                        storage.save()
                    else:
                        if value.isnumeric():
                            setattr(all_instances[class_instance], attr, int(value))
                        else:
                            setattr(all_instances[class_instance], attr, value)
                        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
