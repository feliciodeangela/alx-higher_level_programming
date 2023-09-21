#!/usr/bin/python3
"""This module contains a script that reads input and adds them to a file.."""
import sys

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
ls = load('add_item.json')
for arg in range(1, len(sys.argv)):
    ls.append(sys.argv[arg])
save(ls, 'add_item.json')
