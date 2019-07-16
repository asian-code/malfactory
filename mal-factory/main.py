#!/usr/bin/python3

import core
import maleditor
import gmailemail
import os

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
tool_version=0.1

def clear():
    for i in range(4):
        os.system("clear")


def options():
    
    print(" " + purple + bold + "Tool Version: " + rr + str(tool_version) +"\n") 
    print(" " + ul + "Please Select From The Menu" + rr + "\n")
    print(rr + "   [" + purple + "1" + rr + "]\t Malware Terminal IDE")
    print("   [" + purple + "2" + rr + "]\t Basic Malware Templates")
    print("   [" + purple + "3" + rr + "]\t Send Malware With Email (Gmail w/ S.E Templates)")
    print("   [" + purple + "5" + rr + "]\t Send Malware With a Spoofed Email")
    print("   [" + purple + "r" + rr + "]\t Reloads the screen")
    print("\n   [" + purple + "99" + rr + "]\t Exit \n")


def main():
    try:
        while True:
            command = input(red + "Mal" + purple + "Factory" + rr + " > ")
            if command == "1":
                maleditor.startup()
            if command == "3":
                gmailemail.startup()
            elif command == "r":
                clear()
                startup()
            elif command == "99" or command.lower() == "exit" or command.lower() == "quit":
                core.quit()
            else:
                print(rr + "\nSorry, " + command + " is not a command.\n")
    except KeyboardInterrupt:
        core.quit()
    except Exception:
        print(rr + "\n[" + red + "+" + rr + "] Error: something went wrong \n")# Need general error message since this try is the whole program instead of a specific block of code
        raise


def startup():
    os.system("resize -s 40 86")
    clear()
    print(line)
    core.randomlogo()
    print(line + "\n")
    core.textlogo()
    options()
    main()
