#!/usr/bin/python3
""" command interpreter entry point"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    cmd interpreter for HBNB
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):

        print("")
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg not on self.classes:
            print("** class doesn't exist **")
            return
        
        obj = self.classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return


        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        args = arg.split()


    def do_all(self, arg):
        args = arg.split(maxsplit=3)

    def help_quit(self):

        print("Quit command to exit program")

    def help_EOF(self):
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
