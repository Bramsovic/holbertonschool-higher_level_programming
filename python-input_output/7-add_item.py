#!/usr/bin/python3
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

def add_item():
    if len(sys.argv) == 1:
        return
    else:
        try:
            charged = load_from_json_file("add_item.json")
        except FileNotFoundError:
            charged = []
        for arg in sys.argv[1:]:
            charged.append(arg)
        save_to_json_file(charged, "add_item.json")
if __name__ =="__main__":
    add_item()