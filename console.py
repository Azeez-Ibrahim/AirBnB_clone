#!/usr/bin/python3

'''AirBnB Console (Single use, or customize shell)'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''This is overall class for HBNBCommand'''
    prompt = '(hbnb)'

    def do_quit(self, line):
        '''This is quit method for exiting the program'''
        exit()

    def do_EOF(self, line):
        '''This is exit method for End of file (EOF)'''
        print('')
        exit()

    def emptyline(self):
        '''This is a method to pass when empty line is entered'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
