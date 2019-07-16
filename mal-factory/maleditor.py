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
    print(rr + "\n\t\t\t  " + ul + "Options" + rr + ":")
    print("{}\t\t{}".format("  [" + green + "s" + rr + "] Save file",
          "\t\t  [" + green + "r" + rr + "] Remove a line"))
    print("{}  {}".format("  [" + green + "o" + rr + "] Open from txt file",
          "\t\t  [" + green + "e" + rr + "] Exit MalEditor \n"))


def show_file(file: list):
    num = 1
    marker = "-" * 9
    print(marker + " File " + marker)
    for element in file:
        print(num + ")" + element)
        num += 1
    print(marker + " File " + marker)


def check_command(com):
    try:
        file = open("/usr/share/mal-factory/allcmds.txt", "r")
        all_commands = file.readlines()
        allcmd_filtered = []

        # remove the \n on all elements by removing the last 2 character in each element
        for i in all_commands:
            allcmd_filtered.append(i[:len(i) - 1])

    except Exception:
        print(rr + "\n[" + red + "!" + rr + "] Error: could not find allcmds.txt" + rr)
        raise
    finally:
        file.close()

    if com in allcmd_filtered:
        return True

    return False


def startup():
    core.clear()
    # print("[" + green + "+" + rr + "]  Starting Mal-editor... ") (we dont need this , to much text on screen )
    print("[" + green + "OK" + rr + "] Mal-editor Successfully Started!")
    core.maleditorlogo()
    options()
    whole_file = []
    try:
        while True:
            command = input(red + "Mal" + green + "Editor" + rr + " > ")
            if command == "99" or command.lower() == "exit" or command.lower() == "quit" or command.lower() == "e":
                sys.exit()
            elif command == "u":
                core.clear()
                whole_file.pop()
                show_file(whole_file)
            elif command == "s":
                try:
                    filename = input("[*] File name > ")
                    file = open("/root/{}".format(filename), "w")
                    for element in whole_file:
                        file.write(element)
                except Exception:
                    print(red + "[!] Error saving file as " + filename + rr)
                finally:
                    file.close()
                print(green + "[ OK ] File saved in /root/{}".format(filename) + rr)
            elif check_command(command):
                core.clear()
                options()
                whole_file.append(command)
                show_file(whole_file)
            else:
                core.clear()
                show_file(whole_file)
                print(rr + "\n[" + red + "-" + rr + "] Not a valid command: " + command)
    except KeyboardInterrupt:
        main.startup()
    except Exception:
        print(red + core.bold + "[!] Error in MalEditor")
        raise
