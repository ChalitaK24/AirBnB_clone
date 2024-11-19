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

    def EOD(self, arg):
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
