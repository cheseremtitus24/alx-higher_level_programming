#!/usr/bin/env python3
"""In the previous example, the formatting of the help text leaves something to be desired. Since it comes from the docstring, it retains the indentation from our source. We could edit the source to remove the extra white-space, but that would leave our application looking poorly formatted. An alternative solution is to implement a help handler for the greet command, named help_greet(). When present, the help handler is called on to produce help text for the named command."""
import cmd


class HelloWorld(cmd.Cmd):
    """Simple command processor example.
    It does not make use of the default help
    which is derived from a function docstring
    rather it reads from help_*funcname*"""

    def do_greet(self, person):
        if person:
            print("Hi", person)
        else:
            print("Hi")

    def help_greet(self):
        print("\n".join(['greet [person]', '\t\tGreet the named person', ]))

    def do_EOF(self, line):
        """ This handles case when CTRL-D is pressed and cause a successful exit without throwing off an error"""
        return True

    def do_bye(self, line):
        """ Exits the program"""
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
