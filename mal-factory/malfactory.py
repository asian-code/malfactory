#!/usr/bin/python3

import main
import core
# test
import sys
import os

#core.laughingskull()
print("Testing code for mac{")
print("Method 1 test")
try:
    test1 = open("location.txt", "r")
    test1.close()
except:
    print("Error with Method 1")
print("Method 2 test")
try:
    test1 = open(os.path.join(os.path[0], "location.txt"), "r")
    test1.close()
except:
    print("Error with Method 2")
    print("Testing code for mac END")
#main.startup()
