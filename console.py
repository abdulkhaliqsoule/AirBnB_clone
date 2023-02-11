#!/usr/bin/python3
"""entrpoint of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


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
if __name__ == '__main__':
    HBNBCommand().cmdloop()
