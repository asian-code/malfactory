#!/usr/bin/python
import os
import sys


def options():
    print("\tOptions: ")

    print("\t\t1) Save file")
    print("\t\t2) Undo last line")
    print("\t\t3) Open from txt file")

    print("\n\t\t99) Exit MalEditor without saving")


def clear():
    for i in range(3):
        os.system("clear")


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
                if command == "99":
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
