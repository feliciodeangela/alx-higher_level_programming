#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='A simple CLI replicator')
    parser.add_argument("prnt", nargs='*')
    ar = parser.parse_args()
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("0 arguments.")
