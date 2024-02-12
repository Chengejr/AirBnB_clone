#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB objects.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl+D).
        """
        print("\nGoodbye!")
        return True

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
