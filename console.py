#!/usr/bin/python3
"""Defines the console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter
    Attributes:
        prompt: Text of interactive prompt.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the program")
        print()

    def do_EOF(self, line):
        """exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
