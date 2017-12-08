import os
import sys
import platform

def do_tests():
    exec(open("tests/test.py").read())

def do_tests_with_env():
    pass
    #activate_this_file = ""
    #execfile(activate_this_file, dict(__file__=activate_this_file))
    #execfile("tests/test.py")

print(sys.argv, sys.argv[1])

if len(sys.argv) != 2:
    raise ValueError('Too much arguments! Try with \'test\'')

if str(sys.argv[1]) != 'test':
    print(str(sys.argv[1]))
    raise ValueError('Option not yet implemented. Try \'test\'')
# Check if virtualenv is activated
if hasattr(sys, 'real_prefix'):
    do_tests()
    sys.exit()
else:
    do_tests_with_env()
    sys.exit()
