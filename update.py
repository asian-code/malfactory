#!/usr/bin/python
import subprocess
import os, time
import sys
from urllib.request import urlopen

had_error = False
original_location = ""
red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'

def get_tool_version():
    html = urlopen("https://malfactory.000webhostapp.com/")
    website = str(html.read())
    return website


app_name = "MalFactory"
try:
    if os.path.exists("location.txt") == False:
        raise Exception("Missing location.txt file")
    else:
        print("location.txt is located")
except:
    print(
        red + bold + "[!] Error -"+app_name+" was never properly installed to update,\n\tMissing location.txt file" + rr)
    sys.exit()

file = open("location.txt", "r")
location = file.readlines()[0]
file.close()

old_location = location.split("/")
old_location.pop(0)  # remove first element (empty element)
original_location = old_location.pop()  # remove last element (name of installation folder)
original_location = original_location.split("\\")[0]  # removes the \n inside the string

install_location = ""
for i in old_location:
    install_location += "/{}".format(i)

original_location = str(install_location + "/" + original_location)

print(
    green + bold + "[+] Original file location:" + original_location + "\n[+] Location to install: " + install_location + rr)
try:
    # installs new version
    subprocess.call("./gitAddress", shell=True)
    time.sleep(1)
    print(green + bold + "[ OK ] Installed new version of " + app_name + rr)

    # uninstalls current version
    print("[+] Uninstalling old version of " + app_name)
    subprocess.call("sudo python3 uninstaller.py", shell=True)

    time.sleep(1)
    # move new version to the location of old installation folder
    subprocess.call("sudo mv /usr/var/malfactory {}".format(install_location), shell=True)
    print(green + bold + "[+] Moved new files to correct location" + rr)

    time.sleep(1)
    # setup the program for the user
    print("[+] Running setup.py in - {}/setup.py".format(original_location))

    # setup new version
    subprocess.call("sudo python3 setup.py", shell=True, cwd=original_location)  # cwd changes process directory

except:
    had_error = True
    raise

finally:
    if had_error:
        print(red + bold + "[!] Error updating "+app_name + rr)
    else:
        print(green + bold + "[ OK ] Update complete!!\n" + rr)
