#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import argparse
    sum = 0
    parser = argparse.ArgumentParser(description="A simple CLI adding machine")
    parser.add_argument("addCLI", type=int, nargs='*')
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[i])
    print("{}".format(sum))
