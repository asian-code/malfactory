#!/usr/bin/python

import os
import sys
import core
import main

rr = core.rr
red = core.lred
ul = core.ul
green = core.lgreen
blue = core.lblue


def options():
    print("\t" + ul + "Options" + rr + ":")
    print("\t{}\t\t{}".format("[s] Save file", "[u] Undo last line"))
    print("\t{}  {}".format("[o] Open from txt file", "[e] Exit MalEditor"))


def show_file(file: list):
    for element in file:
        print(element)


def check_command(com):
    with open("allcmds.txt", "r") as f:
        all_commands = f.read()

        '''       
         for i in all_commands:
                        print(i, end="")
        '''

        if com in all_commands:
            return True
        f.close()
    return False


def startup():
    print("[" + green + "+" + rr + "] Starting Mal-editor... ")
    options()
    whole_file = []
    try:
        while True:
            command = input(red + "Mal" + green + "Editor" + blue + " > ")
            if command == "99" or command.lower() == "exit" or command.lower() == "quit":
                sys.exit()
            elif command == "u":
                main.clear()
                whole_file.pop()
                show_file(whole_file)
            elif check_command(command):
                main.clear()
                whole_file.append(command)
                show_file(whole_file)
            else:
                print(red + core.bold + "[-] Not a valid command" + rr)
    except KeyboardInterrupt:
        main.startup()
    except Exception:
        print(red + core.bold + "[!] Error in MalEditor")
        raise
