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

    def do_quit(self, line):
        '''This is quit method for exiting the program'''
        exit()

    def do_EOF(self, line):
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

    def emptyline(self):
        '''This is a method to pass when empty line is entered'''
        pass    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
