#!/usr/bin/python3

import os
red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'
had_error = False
try:
    os.system("sudo rm -rf /usr/share/simple-scan")  # folder
    print("[+] removed simple-scan folder in /usr/share/simple-scan")

    os.system("sudo rm -rf /usr/share/applications/simplescan.desktop")  # desktop file
    print("[+] removed desktop file in /usr/share/applications/simplescan.desktop")

    os.system("sudo rm -rf /usr/bin/simplescanner")  # bash file
    print("[+] removed bash file /usr/bin/simplescan")

    # removes the folder where simple scan installation folder is located
    try:
        file = open("location.txt", "r")
        location = file.readlines()[0]
        os.system("sudo rm -rf {}".format(location))
    except:
        had_error=True
        print("[!] Error-Unable to find location.txt")

except:
    had_error = True
    raise
finally:
    if had_error:
        print(red+bold+"[!] Unable to uninstall Simple-scan due to an error"+rr)
    else:
print(green+bold+"[ OK ] Uninstall is complete, no errors !"+rr)