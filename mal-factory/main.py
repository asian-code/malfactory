#!/usr/bin/python3

import core

green = core.lgreen
lpurple = core.lpurple

def options():
    print(rr + "[" + purple + "1" + rr + "]\t Malware Terminal IDE")
    print("[" + lpurple + "2" + rr + "]\t Basic Malware Templates")
    print("[" + lpurple + "3" + rr + "]\t Spoof Email / Send Malware")
    print("[" + lpurple + "r" + rr + "]\t Reloads the screen")
    print("[" + lpurple + "99" + rr + "]\t Exit")


def main():
    core.random_logo()
    try:
        while True:
            command = input(red + bold + "Mal" + white + bold + "factory >" + rr)
            if command == "1":
                print("")
            elif command == "clear":
                clear()
                random_logo()
            elif command == "99" or command.lower() == "exit" or command.lower() == "quit":
                quit()
            else:
                print(red + bold + "Error " + rr + command)
    except KeyboardInterrupt:
        print(l + "+\n[+] Exiting program" + rr)
    except Exception:
        print("[ " + red + bold + "!" + rr + "] Error :")
        raise


main()
