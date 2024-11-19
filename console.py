#!/usr/bin/python3
""" command interpreter entry point"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    cmd interpreter for HBNB
    """

    prompt = "(hbng) "

    def do_quit(self, arg):
        return True

    def EOF_do(self, arg):

        print("")
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
