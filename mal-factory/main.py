#!/usr/bin/python3

import core
import maleditor
import gmailemail
import os
import sys
import platform

operating_system = platform.system()
green = core.lgreen
yellow = core.yellow
purple = core.lpurple
red = core.lred
blue = core.lblue
cyan = core.lcyan
rr = core.rr
bold = core.bold
ul = core.ul
line = purple + bold + "--------------------------------------------------------------------------------------" + rr
tool_version = 0.1  # get tool version from update.py not in main.py


def get_install_location():
    # allows for python to find installation folder
    loc = ""
    try:
        file = open("location.txt", "r")
        loc = file.read()
        file.close()
    except FileNotFoundError:
        print(red + "[!] Error, location.txt is not located" + rr)
    return loc


def clear():
    for i in range(4):
        os.system("clear")


def options():
    print(" " + purple + bold + "Tool Version: " + rr + str(tool_version) + "\n")
    print(" " + blue + ul + "Please Select From The Menu" + rr + "\n")

    print("\t{:10s} MalEditor".format("[" + purple + "1" + rr + "]"))
    print("\t{:10s} Send Malware With Email w/ Gmail".format("[" + purple + "2" + rr + "]"))
    print("\t{:10s} Reloads The Screen".format("[" + purple + "r" + rr + "]"))
    print()  # prints empty line to separate options from functions
    # print("\t{:10s} Check for Updates(Coming soon)".format("[" + purple + "c" + rr + "]"))
    print("\t{:10s} Uninstall Malfactory(Comming soon)".format("[" + red + "u" + rr + "]"))
    print("\t{:10s} Exit ".format("[" + purple + "99" + rr + "]"))
    print()  # empty line for the looks


def help():
    print("Help menu")
    print("[1] MalEditor -is used for making malware using \"Malscript\", you can write and save your scripts here")
    print("[2] Reloads The Screen -is used for refreshing the screen")
    # etc , add more stuff here


def main():  # takes in user input and check for commands
    try:
        while True:
            command = input(red + "Mal" + purple + "Factory" + rr + " > ")
            command = command.lower()
            if command == "1":
                maleditor.startup()
            if command == "2":
                gmailemail.startup()
            elif command == "r":
                clear()
                startup()
            elif command == "99" or command == "exit" or command == "quit":
                core.quit()
            elif command == "help":
                help()
            else:
                print(rr + red + "\nSorry, " + command + " is not a command.\n")
    except KeyboardInterrupt:
        core.quit()
    except Exception:
        print(
            rr + "\n[" + red + "+" + rr + "] Error: something went wrong \n")  # Need general error message since this try is the whole program instead of a specific block of code
        raise


def startup():  # display logo and options
    os.system("resize -s 40 86")
    clear()
    print(line)
    core.randomlogo()
    print(line + "\n")
    core.textlogo()
    print(blue + "[+] Checking for updates..." + rr)

    # testing code{

    loc = get_install_location()
    # if loc != "":
    updater_loc = loc + "/update"
    print(blue + "[+] Checking for updater in " + rr + updater_loc)

    # method 1
    sys.path.append(loc)
    print("Method 1")
    try:
        import update
        update.main(force=False)
    except ImportError:
        print(red + "[!] Error trying to update" + rr)

    # method 2
    sys.path.insert(0, updater_loc)
    print("Method 2")
    try:
        import update
        update.main(force=False)
    except ImportError:
        print(red + "[!] Error trying to update" + rr)
    # } testing code

    options()

    main()
