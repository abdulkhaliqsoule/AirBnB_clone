#!/usr/bin/python3
"""entrpoint of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """AirBnB console"""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        'exit the console'
        return True

    do_EOF = do_quit

    def do_create(self, line):
        """Creates an object"""
        if not len(line):
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_object = eval(line)()
        print(new_object.id)
        new_object.save()

    def do_show(self, line):
        """shows an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        key_value = strings[0] + "." + strings[1]
        if key_value not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[key_value])

    def do_destroy(self, line):
        """deletes an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        key_value = strings[0] + "." + strings[1]
        if key_value not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[key_value]
        storage.save()

    def do_all(self, line):
        """prints string representation ofall objects"""
        if not len(line):
            print([obj for obj in storage.all().values()])
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        print([obj for obj in storage.all().values()
              if strings[0] == type(obj).__name__])

    def do_update(self, line):
        """updates an object"""
        if not len(line):
            print("** class name missing **")
            return
        strings = split(line)
        for string in strings:
            if string.startswith('"') and string.endswith('"'):
                string = string[1:-1]
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        if len(strings) == 2:
            print("** attribute name missing **")
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[keyValue], strings[2], eval(strings[3]))
        except:
            setattr(storage.all()[keyValue], strings[2], strings[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
