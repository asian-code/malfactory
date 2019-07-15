#!/usr/bin/python3

import core
import maleditor
import spoofemail
import os

green = core.lgreen
purple = core.lpurple
red = core.lred
blue = core.lblue
cyan = core.lcyan
rr = core.rr
bold = core.bold
ul = core.ul
line = purple + bold + "--------------------------------------------------------------------------------------" + rr


def options():
    print(" " + ul + "Please Select From The Menu" + rr + "\n")
    print(rr + "   [" + purple + "1" + rr + "]\t Malware Terminal IDE")
    print("   [" + purple + "2" + rr + "]\t Basic Malware Templates")
    print("   [" + purple + "3" + rr + "]\t Spoof Email / Send Malware")
    print("   [" + purple + "r" + rr + "]\t Reloads the screen")
    print("   [" + purple + "99" + rr + "]\t Exit \n")


def main():
    try:
        while True:
            command = input(red + "Mal" + cyan + "Factory " + blue + "> " + rr)
            if command == "1":
                maleditor.startup()
            if command == "3":
                spoofemail.startup()
            elif command == "r":
                core.clear()
                startup()
            elif command == "99" or command.lower() == "exit" or command.lower() == "quit":
                core.quit()
            else:
                print(rr + "\nSorry, " + command + "is not a command.\n")
    except KeyboardInterrupt:
        core.quit()
    except Exception:
        print(
            rr + "\n[" + red + "+" + rr + "] Error: Could not run program. Have you installed all the dependencies?" + rr + "\n")
        raise


def startup():
    # makes terminal size bigger to see YOUR GIANT ASS LOGOS, your welcome you cunt XD
    # another way to resize terminal(it doesnt work on all terminal emulators ) resize -s 35 100

    os.system('\e[8;35;100t')
    core.clear()
    print(line)
    core.randomlogo()
    print(line + "\n")
    core.textlogo()
    options()
    main()
