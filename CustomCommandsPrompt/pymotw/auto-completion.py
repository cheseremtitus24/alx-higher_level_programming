#!/usr/bin/env python3
"""
Once the command is known, argument completion is handled by methods with the prefix complete_. This allows you to assemble a list of possible completions using your own criteria (query a database, look at at a file or directory on the filesystem, etc.). In this case, the program has a hard-coded set of “friends” who receive a less formal greeting than named or anonymous strangers. A real program would probably save the list somewhere, and either read it once and cache the contents to be scanned as needed.
"""
import cmd


class HelloWorld(cmd.Cmd):
    """Simple command processor example.
    It does not make use of the default help
    which is derived from a function docstring
    rather it reads from help_*funcname*"""

    FRIENDS = ['Alice', 'Adam', 'Barbara', 'Bob']

    def do_greet(self, person):
        'This help msg is overriden by help_greet'
        if person and person in self.__class__.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello," + person
        else:
            greeting = 'hello'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        """ Perfoms argument autocompletions """
        if not text:
            completions = self.__class__.FRIENDS[:]
        else:
            completions = [ f for f in self.__class__.FRIENDS if f.startswith(text)]
        return completions

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
