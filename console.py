#!/usr/bin/python3
""" command interpreter entry point"""

import cmd
from models.base_model import BaseModel
from models import storage

valid_classes = {"BaseModel": BaseModel}


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

    def do_create(self, arg):
         if not arg:
             print("** class name missing **")
             return
         if arg not in valid_classes:
             print("** class doesn't exist **")
             return
         new_instance = valid_classes[arg]()
         new_instance.save()
         print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
            
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        if arg and arg not in valid_classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        result = []
        for key, obj in objects.items():
            if not arg or key.startswith(arg + "."):
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        args = arg.split(maxsplit=3)
        if len(args) < 1:
            print("** class name missing **")
            return

        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        try:
             if '.' in attr_value:
                 attr_value = float(attr_value)
             else:
                 attr_value = int(attr_value)
        except ValueError:
             pass
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
     HBNBCommand().cmdloop()
