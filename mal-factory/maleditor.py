#!/usr/bin/python

import core
import main
import platform
import sys
import os

rr = core.rr
red = core.lred
ul = core.ul
green = core.lgreen
blue = core.lblue
operating_system = platform.system()


# maleditor is only for Editing/Saving Malscript files. Another program will convert the malscript to code for target platform
def options():
    print(rr + "\n\t  " + ul + "Options" + rr + ":")
    print("{:30s}{:30s}".format("  [" + green + "s" + rr + "] Save file", "[" + green + "r" + rr + "] Remove a line"))
    print("{:30s}{:30s}".format("  [" + green + "o" + rr + "] Open from txt file",
                                "[" + green + "e" + rr + "] Exit MalEditor"))
    print()  # empty line separator


def show_file(file: list, filename: str):
    if len(file) > 0:
        num = 1
        marker = "-" * 9
        print(marker + " {} ".format(filename) + marker)
        for element in file:
            print(str(num) + ")\t" + element)
            num += 1
        print(marker + " {} ".format(filename) + marker)


def read_from_file(location: str):
    try:
        fileloc = open(location, "r")
        content = fileloc.readlines()
        fileloc.close()
        return content
    except Exception:
        print(rr + "\n[" + red + "!" + rr + "] Error: could not find file in {}".format(location) + rr)


def check_command(com, raw_commands: list):
    allcmd_filtered = []

    # remove the \n on all elements by removing the last 2 character in each element
    for i in raw_commands:
        allcmd_filtered.append(i[:len(i) - 1])

    if com in allcmd_filtered:
        return True

    return False


def set_screen(file_to_show, fname):
    core.clear()
    options()
    show_file(file_to_show, fname)


def startup():
    core.clear()
    # print("[" + green + "+" + rr + "]  Starting Mal-editor... ") (we dont need this , to much text on screen )
    print("[" + green + "OK" + rr + "] Mal-editor Successfully Started!")
    core.maleditorlogo()
    options()

    whole_file = []
    CurrentFileName = "Untitled"
    if operating_system == "Linux":
        raw_cmd = read_from_file(os.path.join(sys.path[0], "allcmds.txt"))
    else:
        raw_cmd = read_from_file("~/mal-factory/allcmds.txt")

    try:
        while True:
            command = input(red + "Mal" + green + "Editor" + rr + " > ")
            if command == "99" or command.lower() == "exit" or command.lower() == "quit" or command.lower() == "e":
                raise KeyboardInterrupt

            elif command.split(" ")[0] == "r":
                try:
                    whole_file.pop(int(command.split(" ")[1]))
                except:
                    print("[!] Error trying to remove a line")
                set_screen(whole_file, CurrentFileName)


            elif command == "s":
                try:
                    filename = input(blue + "[*] Save as" + rr + ": ")
                    CurrentFileName = filename
                    savefile = open("~/{}.txt".format(filename), "w")
                    for element in whole_file:
                        savefile.write(element + "\n")
                    savefile.close()
                except Exception:
                    print(red + "[!] Error saving file as " + filename + rr)

                print(green + "[ OK ] File saved in ~/{}".format(filename) + rr)

            elif check_command(command, raw_cmd):
                whole_file.append(command)
                set_screen(whole_file, CurrentFileName)
            else:
                set_screen(whole_file, CurrentFileName)
                print(rr + "\n[" + red + "-" + rr + "] Not a valid command: " + command)

            core.clear()
            options()
            show_file(whole_file, CurrentFileName)

    except KeyboardInterrupt:
        main.startup()
    except Exception:
        print(red + core.bold + "[!] Error in MalEditor")
        raise
