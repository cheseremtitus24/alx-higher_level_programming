There are cases where tests exist for a module that should be included with the source code but not in the help text for a module, so they need to be placed somewhere other than the docstrings. 
doctest also looks for a module-level variable called 

__test__ and uses it to locate other tests.

The value of __test__ should be a dictionary that maps test set names (as strings) to strings, modules, classes, or functions.


##External Documentation

doctest_in_help.txt file.




