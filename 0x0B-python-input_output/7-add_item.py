#!/usr/bin/python3
"""
7-add_item.py

Adds all arguments to a Python list, then
saves them to a file.
"""

# import modules
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        args = load_from_json_file("add_item.json")
    except FileNotFoundError:
        args = []

    # Add all arguments from command line to args list.
    args.extend(sys.argv[1:])
    save_to_json_file(args, "add_item.json")
