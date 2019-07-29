#!/usr/bin/python3

import main
import core
# test
import sys
import os
import urllib


def get_latest_version():
    html = urllib.urlopen("https://malfactory.000webhostapp.com/")
    website = str(html.read())
    # ver = float(website.split("# ")[1])
    # print("Latest version: " + str(ver))
    return float(website.split("# ")[1])


# core.laughingskull()
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
print("Testing communication with server")
try:
    print(get_latest_version())
except:
    print("Error talking with server")


print("Testing code for mac END")
main.startup()
