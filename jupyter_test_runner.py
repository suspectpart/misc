import sys
import traceback
from termcolor import colored
import numpy as np
import io
from contextlib import redirect_stdout

def run_all_tests(print_stdout = True, clean_tests = True):
	'''
	Executes all methods prefixed _test from inside a jupyter notebook cell. 
	Ligthweight alternative for quick unit testing in jupyter, using plain asserts.
	'''
    tests = [test for test in globals() if test[0:5] == "test_"]
    tests.sort()
    
    print("+-----------------------+")
    print("|     Jupyter Tests     |")
    print("+-----------------------+\n")
    print(":: Loaded {0} Tests\n".format(len(tests)))
    
    errors = 0
    
    for test in tests:
        test_output = test_runner_output = ""
        
        with io.StringIO() as buf, redirect_stdout(buf):    
            try:
                globals()[test]()
                test_runner_output += colored('+ [Pass] {}'.format(test), 'green')
            except Exception as e:
                errors += 1
                _, exc_value, tb = sys.exc_info()
                filename, line, func, text = traceback.extract_tb(tb)[-1]
                if type(e).__name__ == "AssertionError":
                    test_runner_output += colored('- [Fail] {0} (Line {1}: {2})'.format(func, line, text), 'red')
                else:
                    test_runner_output += colored('- [Excp] {0} (Line {1}: {2})'.format(func, line, exc_value), 'red')
            test_output = buf.getvalue()
            
        print(test_runner_output)
        
        if(test_output and print_stdout):
            print("\n".join(list(map(lambda s: "\t" + s , test_output.strip().split("\n")))))
        
    print("\n{0} pass, {1} fail in {2} tests".format(len(tests) - errors, errors, len(tests)))

    list(map(lambda test: globals().pop(test), tests)) if clean_tests else 0
    
    return errors == 0
