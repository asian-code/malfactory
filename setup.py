#!/usr/bin/python3


import time
import subprocess

had_error = False
red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'
p = platform.system()

def get_current_dir():
    save_location = str(subprocess.check_output(["pwd"]))
    # save directory to txt file in the simple-scan folder
    # delete this folder later in uninstaller.py
    folder = save_location.split("/")
    folder.remove("b'")  # this is needed to remove the first element in the list
    folder[len(folder) - 1] = folder[len(folder) - 1].split("\\")[0]  # removes the \n in the last element
    result = ""
    for i in folder:
        result += "/" + i
    return result


def save_folder_location(location):
    try:
        file = open(location + "/location.txt", "w")
        file.write(location)
    except:
        print(red+bold+"[!] Error writing to file"+rr)
        had_error = True
        raise
    finally:
        file.close()


try:
    # add modules u use here
    
    # subprocess.call("pip3 install scapy", shell=True)
    # subprocess.call("pip3 install curses",shell=True)

    subprocess.call("sudo mv mal-factory /usr/share", shell=True)  # folder
    print("[+] moved mal-factory folder to /usr/share")

    subprocess.call("sudo mv malfactory.desktop /usr/share/applications/", shell=True)  # .desktop file
    print("[+] moved desktop to /usr/share/applications")

    subprocess.call("sudo mv malfactory /usr/bin", shell=True)  # bash file
    print("[+] moved bash file to /usr/bin")

    save_folder_location(get_current_dir())

    time.sleep(1)
except:
    had_error = True
    raise
finally:
    if had_error:
        print(red+bold+"[-] Setup Failed, an error stopped the setup process "+rr)
    else:
        print(green+bold+"[+] Setup is complete, no errors!"+rr)
