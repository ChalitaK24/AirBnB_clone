#!/usr/bin/python3
""" command interpreter entry point"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    cmd interpreter for HBNB
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):

        print("")
        return True

    def emptyline(self):
        pass

    def help_quit(self):

        print("Quit command to exit program")

    def help_EOF(self):
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
