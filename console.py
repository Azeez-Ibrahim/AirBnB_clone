#!/usr/bin/python3

'''AirBnB Console (Single use, or customize shell)'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    '''This is overall class for HBNBCommand'''
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}	

    def do_quit(self, args):
        '''This is quit method for exiting the program'''
        exit()

    def do_EOF(self, args):
        '''This is exit method for End of file (EOF)'''
        print('')
        exit()

    def do_create(self, args):
        'create instance of basemodel, saves it'
        args = args.split()
        if args is None:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes.get(args[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, args):
        'print string __str__ of an instance based on class name'
        args = args.split()
        'expecting: args = [name, name_id]'
        if len(args) != 2:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if args[1] == v.id:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        'deletes an instance based on class name or id'
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        'print string __str__ of an instance based on class name or nothing'
        args = args.split()
        if not args:
            for k, v in storage.all().items():
                print(v)
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if args[0] == v.__class__.__name__:
                    print(v)
                    return
            print('[]')


    def emptyline(self):
        '''This is a method to pass when empty line is entered'''
        pass    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
