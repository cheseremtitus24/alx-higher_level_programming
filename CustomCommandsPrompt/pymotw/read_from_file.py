#!/usr/bin/env python3
import cmd

'''
With use_rawinput set to False and prompt set to an empty string, we can call the script on this input file:
'''
class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    # Disable rawinput module use
    use_rawinput = False
    
    # Do not show a prompt after each command read
    prompt = ''
    
    def do_greet(self, line):
        print ("hello,", line)
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys
    input = open(sys.argv[1], 'rt')
    try:
        HelloWorld(stdin=input).cmdloop()
    finally:
        input.close()
