import sys, parser
from errors import *

if __name__ == "__main__":

    # add input checks here
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py \"input_string\"")
        exit(1)
    
    input_string = sys.argv[1]
    input_string = input_string.replace(" ", "")

    try:
        parser.parse(input_string)
    except TerminalException as e:
        print("Terminal Exception")
        print(e.arg)
        print("\t" + e.arg)
    except RuleNotFoundException as e:
        print("Rule Not Found")
        print("\t" + e.arg)
        exit(1)

    # program terminates normally
    exit(0)