#!/usr/bin/python

import os
import sys
import core

rr = core.rr
red = core.lred
ul = core.ul
green = core.lgreen
blue = core.lblue

def options():
    print("  [-] Options: \n")
    print("  [s] Save file \t [u] Undo last line")
    print("  [o] Open from txt file \t [e] Exit MalEditor")

def print_file(file: list):
    for element in file:
        print(element)

def main():
    print("[" + green + "+" + rr + "] Starting Mal-editor... ")
    options()
    whole_file = []
    try:
        while True:
           command = input(red + "Mal" + green + "Editor" + blue + " >")
           if command == "99" or command.lower() == "exit" or command.lower() == "quit":
                sys.exit()
           elif command == "2":
                whole_file.pop()
                print_file(whole_file)
           else:
                clear()
                whole_file.append(command)
                print_file(whole_file)
        except KeyboardInterrupt:
           print("add malfactory.startup() here")

def startup():
    core.clear()
    main()
