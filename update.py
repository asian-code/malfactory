#!/usr/bin/python
import subprocess
import os
import sys
from urllib.request import urlopen
import platform

red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'
lblue = '\033[94m'

app_name = "MalFactory"
tool_version = 0.1  # [ CHANGE ME ]    -every time there is a important change in the coding of malfactory
operating_system = platform.system()


def get_latest_version():
    html = urlopen("https://malfactory.000webhostapp.com/")
    website = str(html.read())
    return float(website.split(": ")[1][0:3])


def setup_program(original_location):
    # setup the program for the user
    print("[+] Running setup.py in - {}/setup.py".format(original_location))
    subprocess.call("sudo python3 setup.py", shell=True, cwd=original_location)  # cwd changes process directory


def uninstall_current_version(original_location):
    # uninstalls current version
    print("[+] Uninstalling old version of " + app_name)
    subprocess.call("sudo python3 uninstaller.py", shell=True, cwd=original_location)


def get_locations():
    # get location from location.txt
    file = open("location.txt", "r")
    location = file.readlines()[0]
    file.close()

    old_location = location.split("/")
    old_location.pop(0)  # remove first element (empty element)
    original_loc = old_location.pop()  # remove last element (name of installation folder)
    original_loc = original_loc.split("\\")[0]  # removes the \n inside the string

    install_loc = ""
    for i in old_location:
        install_loc += "/{}".format(i)

    original_location = str(install_loc + "/" + original_loc)
    return install_loc, original_location


def start_update(force=False):  # force update doesnt require user permission to update
    had_error = False
    run_program = True  # if wants to run updater
    if not force:
        # check if an update is needed
        try:
            if tool_version >= get_latest_version():
                print(lblue + "[+] You seem to have the latest version of {}".format(app_name))

                # testing code {
                # update_anyway = input(lblue + "[*] You seem to have the latest version of {}. Would you like to update anyway? (y/n) :{}".format(app_name, rr))
                update_anyway = "n"
                update_anyway = update_anyway.lower()
                if update_anyway == "n" or update_anyway == "no":
                    run_program = False
                # } testing code

            else:
                permission = input(lblue + "[*] Update is available, Would you like to install now? (y/n): " + rr)
                permission = permission.lower()
                if permission == "n" or permission == "no":
                    print("[+] Exiting updater")
                    run_program = False

        except Exception:
            print("[-] Unable to connect to connect to server, check internet connection")

    if run_program:
        # check if app was properly installed into system
        try:
            testfile = open(os.path.join(sys.path[0], "location.txt"), "r")
            testfile.close()
        except:
            print(bold + "[!] Error -" + app_name + " was never properly installed to update,\t[Missing location.txt]" + rr)

        # save locations
        install_location, original_location = get_locations()

        print(
            green + bold + "{:30s}\t{}\n{:30s}\t{}\n{:30s}\t{}".
            format("[+] Detected OS:", operating_system, "[+] Original file location:", original_location,
                   "[+] Location to install:", install_location) + rr)

        try:
            if operating_system == "Linux":
                # installs new version
                subprocess.call("./gitAddress", shell=True, cwd=original_location)
                print(green + bold + "[ OK ] Installed new version of " + app_name + rr)

                uninstall_current_version(original_location)

                # move new version to the location of old installation folder
                subprocess.call("sudo mv /usr/var/malfactory {}".format(install_location), shell=True)
                print(green + bold + "[+] Moved new files to correct location" + rr)

                setup_program(original_location)
            else:
                # Run stuff for Mac users

                # installs new version into ~/Downloads
                subprocess.call("./gitAddressMac", shell=True, cwd=original_location)
                print(green + bold + "[ OK ] Installed new version of " + app_name + rr)

                uninstall_current_version(original_location)

                # move new version to the location of old installation folder
                subprocess.call("sudo mv ~/Downloads/malfactory {}".format(install_location), shell=True)
                print(green + bold + "[+] Moved new files to correct location" + rr)

                setup_program(original_location)


        except Exception:
            had_error = True
            raise

        finally:
            if had_error:
                print(red + bold + "[!] Error updating " + app_name + rr)
            else:
                print(green + bold + "[ OK ] Update complete!!\n" + rr)
