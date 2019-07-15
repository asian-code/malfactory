#!/usr/bin/python

import os
import sys
import core
import main

rr = core.rr
red = core.lred
ul = core.ul
green = core.green
blue = core.lblue


def clear():
    os.system("clear")


def options():
    print("\t" + ul + "Options" + rr + ":")
    print("[" + green + "s" + rr + "] Save file")
    print("[" + green + "u" + rr + "] Undo last line")
    print("[" + green + "o" + rr + "] Open from txt file")
    print("\nCrtl+C or e to exit\n")
    '''
    print("\t{0}\t{1}".format("[s] Save file", "[u] Undo last line"))
    print("\t{0}  {1}\n".format("[o] Open from txt file", "[e] Exit MalEditor"))
    '''


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
        print(red + "[!] Error- could not find allcmds.txt" + rr)
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
                clear()
                whole_file.pop()
                show_file(whole_file)
            elif command == "s":
                file_name = input("Filename > ")
                save_file = open("/root/{}".format(file_name), "w")

                save_file.close()
            elif check_command(command):
                clear()
                whole_file.append(command)
                show_file(whole_file)
            else:
                print(red + "[-] Not a valid command" + rr)
    except KeyboardInterrupt:
        main.startup()
    except Exception:
        print(red + "[!] Error in MalEditor")
        raise
