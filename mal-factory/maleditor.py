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
    print("\n\t" + ul + "Options" + rr + ":")
    print("\t{}\t\t{}".format("[" + green + "s" + rr + "] Save file", "\t[" + green + "u" + rr + "] Undo last line"))
    print("\t{}  {}".format("[" + green + "o" + rr + "] Open from txt file", "\t[" + green + "e" + rr + "] Exit MalEditor \n"))


def show_file(file: list):
    for element in file:
        print(element)


def check_command(com):
    try:
        with open("/usr/share/mal-factory/allcmds.txt", "r") as f:
            all_commands = f.read()

            '''       
             for i in all_commands:
                            print(i, end="")
            '''

            if com in all_commands:
                return True
            f.close()
    except Exception:
        print(red + core.bold + "[!] Error- could not find allcmds.txt" + rr)
    return False


def startup():
    core.clear()
    print("[" + green + "+" + rr + "]  Starting Mal-editor... ")
    print("[" + green + "OK" + rr + "] Mal-editor Successfully Started!")
    options()
    whole_file = []
    try:
        while True:
            command = input(red + "Mal" + green + "Editor" + rr + " > ")
            if command == "99" or command.lower() == "exit" or command.lower() == "quit":
                sys.exit()
            elif command == "u":
                core.clear()
                whole_file.pop()
                show_file(whole_file)
            elif check_command(command):
                core.clear()
                whole_file.append(command)
                show_file(whole_file)
            else:
                print(red + core.bold + "[-] Not a valid command" + rr)
    except KeyboardInterrupt:
        main.startup()
    except Exception:
        print(red + core.bold + "[!] Error in MalEditor")
        raise
