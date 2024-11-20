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

        if args[0] not in self.classes:
            print("** class does't exist **")
            return
        if len(args) == 1:
            print("** instance is missing **")
            return

        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)

        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        args = arg.split()

        if len (args) == 9:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesnt exist **")
            return
        if len(args) == 1:
            print("** instance is missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]

        storage.save()

    def do_all(self, arg):
        args = arg.split(maxsplit=3)
        objs = storage.all()

    def do_update(self, arg):
        args = arg,splt(maxsplit=3)


        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)


        attr_name = args[2]
        attr_value = args[3].strip('"')

    try:
        if attr_value.isdigit():
            attr_value = int(attr_value)
        elif '.' in attr_value:
            attr_value = float(attr_value)

    except ValueError:
        pass

    setattr(obj, attr_name, attr_value)
    obj.save()


    def help_quit(self):

        print("Quit command to exit program")

    def help_EOF(self):
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
