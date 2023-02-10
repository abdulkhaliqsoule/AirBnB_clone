#!/usr/bin/python3
import cmd


class HBNBShell(cmd.Cmd):
    intro = ''
    prompt = '(hbnb) '
    file = None

    # ----- basic turtle commands -----
    def do_EOF(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'

    def do_quit(self, arg):
        'exit the console'
        return True


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBShell().cmdloop()
