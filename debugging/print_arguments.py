#!/usr/bin/python3
import sys

# Start from index 1 to avoid printing the script name (sys.argv[0])
for arg in sys.argv[1:]:
    print(arg)