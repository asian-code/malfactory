#!/usr/bin/python

import os
import sys

def options():
    print("  [-] Options: \n")
    print("  [s] Save file \t [u] Undo last line")
    print("  [o] Open from txt file \t [e] Exit MalEditor")

def print_file(file: list):
    for element in file:
        print(element)

def main():
    print("[+] Starting Mal-editor ")
    options()
    whole_file = []
    try:
        while True:
           command = input("MalEditor >")
           if command == "99" or :
                sys.exit()
           elif command == "2":
                whole_file.pop()
                print_file(whole_file)
           else:
                clear()
                whole_file.append(command)
                print_file(whole_file)
        except KeyboardInterrupt:
            sys.exit()

def startup():
    core.clear()
    main()
