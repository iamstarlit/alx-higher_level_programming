#!/bin/bash
cat add_item.json
./7-add_item.py
cat add_item.json ; echo ""
./7-add_item.py Best School
cat add_item.json ; echo ""
./7-add_item.py 89 Python C
cat add_item.json ; echo ""
