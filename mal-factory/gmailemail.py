#!/usr/bin/python

# smtplib module send mail
# server.login(gmail_sender, gmail_passwd)
# server.sendmail(gmail_sender, [TO], BODY)

import smtplib
import imaplib
import core
import main
import os
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#NP ="""
#REQUEST FOR ASSISTANCE-STRICTLY CONFIDENTIAL

#Hello there """ + name + ". \n" + """I am Dr. Bakare Tunde, the cousin of Nigerian Astronaut, Air Force Major Abacha Tunde.
#He was the first African in space when he made a secret flight to the Salyut 6 space station in 1979.
#He was on a later Soviet spaceflight, Soyuz T-16Z to the secret Soviet military space station Salyut 8T in 1989.
#He was stranded there in 1990 when the Soviet Union was dissolved.
#His other Soviet crew members returned to earth on the Soyuz T-16Z, but his place was taken up by return cargo.
#There have been occasional Progrez supply flights to keep him going since that time.
#He is in good humor, but wants to come home.
#All we need you to do is install our software which gives a tiny bit of energy from your computer to send for his supply flights.
#"""

ITD = """

"""

UA = """
"""

RSU = """
"""

ISU = """
"""

LME = """
"""

LMAE = """
"""

# defines the server for gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
mail = imaplib.IMAP4_SSL('imap.gmail.com')  # port 993
server.ehlo()
server.starttls()
server.ehlo()

# defines everything for the webpage
url = "https://mail.google.com/mail/u/0/#inbox"
line = core.blue + core.bold + "\n--------------------------------------------------------------------------------------" + core.rr
gmail = core.blue + core.bold + "G" + core.rr + "m" + core.yellow + "a" + core.rr + "i" + core.yellow + "l" + core.rr

# CLEARS THE SCREEN
def clear():
    for i in range(4):
        os.system("clear")

def quit():
    core.quit()

def inbox(username, password):
    try:
        print(line)
        core.gmaillogo()
        print(line + "\n")
        while True:
            answer = input(gmail + core.yellow + " > " + core.rr + "")
            answer = answer.lower()
            answer = answer.split(" ")
            if answer[0] == "help":
                print("\n-----------\n")
                print(core.ul + "The Help/Command Menu" + core.rr)
                print("\nhelp - Opens this help menu")
                print("reload - Reloads the screen")
                print("template - See the gmail templates")
                print("send <sendingto@gmail.com> - Send an email with your gmail account")
                print("send <sendingto@gmail.com> -t <template> - Send an email with a pre-set template with your gmail account")
                print("exit - Go back to the homepage")
                print("\n-----------\n")
            elif answer[0] == "template" or answer[0] == "templates":
                print("""\n-----------\n
(DO NOT USE THIS FOR ILLEGAL PURPOUSES
\n-----------\n
NP - (Nigerian Prince) - Send an email asking people to help a helpless rich nigerian prince
* REQUIRES FIRSTNAME AND LASTNAME
-----------
ITD - (IT Department) - Send an email pretending to be a company's I.T department
* REQUIRES LASTNAME, COMPANYNAME
-----------
UA - (Unauthorized Access) - Send an email claiming someone's account has reached unauthorized access
* REQUIRES FIRSTNAME, LASTNAME, COMPANYNAME, AND USERNAME
-----------
RSU - (Router Software Update) - Send an email from a router company asking to download a software update
* REQUIRES FIRSTNAME, LASTNAME, COMPANYNAME, ROUTERNAME
-----------
ISU - (ISP Software Update) - Send an email from an Internet Service Provider company asking to download a software update
* REQUIRES FIRSTNAME, LASTNAME, COMPANYNAME, AND ADDRESS
\n-----------\n
LME - (Legitimate Malfactory Email) - Send an email expressing that the email contains malware from Malfactory
-----------
LMAE - (Legitimate Malware Analysis Email) - Send an email expressing that the email contains malware for analysis
\n-----------\n""")
            elif answer[0] == "exit":
                main.startup()
            elif answer[0] == "reload" or answer[0] == "clear":
                core.clear()
                print(line)
                core.gmaillogo()
                print(line + "\n")
            elif answer[0] == "send":
                try:
                    TO = answer[1]
                    SUBJECT = input("\nSubject: ")
                    print("\n--- Type 'quit' to Finish! ---")
                    TEXT = ""
                    x = 1
                    while True:
                        message = input(str(x) + ": ")
                        if message.lower() == "quit" or message.lower() == "q":
                            print("\n")
                            break
                        TEXT = TEXT + message + "\n"
                        x += 1
                    BODY = '\r\n'.join(['To: %s' % TO,
                                        'From: %s' % username,
                                        'Subject: %s' % SUBJECT,
                                        '', TEXT])
                    try:
                        server.sendmail(username, [TO], BODY)
                        print('Your email was sent!')
                    except:
                        print("Error sending mail! Does the recipient's email exist?")
                except:
                    print("\nError: Could not send email! Your command was incorrectly set.\n")
            elif answer[0] == "send" and answer[3] == "-t":
                try:
                    TO = answer[1]
                    TEMPLATE = answer[3]
                    SUBJECT = input("\nSubject: ")
                    TEXT = TEMPLATE
                    print(TEMPLATE)
                    try:
                        server.sendmail(username, [TO], BODY)
                        print('Your email was sent!')
                    except:
                        print("Error sending mail! Does the recipient's email exist?")
                except:
                    print("\nError: Could not send email! Your command was incorrectly set.\n")
            else:
                print("\nCommand '" + str(answer) + "' was not found. Please type 'help' for help.\n")
    except KeyboardInterrupt:
        main.startup()
    except:
        print("\nError: Can't find input.\n")
        raise


# LOGIN INTO GMAIL
def login():
    try:
        gmail_sender = input("Please put your " + gmail + " Username: ")
        gmail_sender = str(gmail_sender)
        gmail_passwd = input("Please enter your " + core.red + "password" + core.rr + ": " + core.invis)
        gmail_passwd = str(gmail_passwd)
        print(core.rr + "")
        if gmail_sender == "" or gmail_passwd == "":
            print(core.rr + "\nSorry! You used an unknown character. Please type in your credentials correctly!")
            input("Please press {ENTER} to continue... " + core.invis)
            print(core.rr + "")
            startup()
        authenticate(gmail_sender, gmail_passwd)
    except KeyboardInterrupt:
        main.startup()


# LOGGING INTO THE ACCOUNT
def authenticate(username, password):
    try:
        clear()
        server.login(username, password)
        mail.login(username, password)
        inbox(username, password)
    except smtplib.SMTPAuthenticationError:
        clear()
        core.gmaillogo()
        core.gmailgmailname()
        print(core.lcyan + core.bold + "\nUTHENTICATION ERORR!:\n")
        print(core.lblue + "Cannot sign in. Are you sure this account exists?:" + core.rr)
        print(
            "\nRight now, the reason you may not log-into your gmail account (if your cresidentials are right) is because google sees this form of authentication as 'less secure'.\n")
        print(core.bold + core.lblue + "How to fix this issue:" + core.rr)
        print(core.white + """
1. Login to your Gmail Account
2. Open the link:""")
        print(core.lcyan + core.ul + "https://www.google.com/settings/security/lesssecureapps" + core.rr)
        print("3. Allow less secure app access to your gmail account.\n")
        print(core.bold + core.lblue + "I allowed unsecure apps. Why is it still not working?:" + core.rr)
        print("""\nSo now it appears you typed in your
cresidentials correctly and allowed unsecure apps, but it still doesnt work. 

This is because google doesn't know if the location of the device accessing your gmail (in this case, the tool itself), is by you.\n""")
        print(core.bold + core.lblue + "How to fix this issue as well:" + core.rr)
        print("\n1. Allow the location of the device by openining the link:")
        print(core.lcyan + core.ul + "https://www.google.com/settings/security/lesssecureapps" + core.rr)
        print(
            "2. If this link does not work, perform it manually from your Gmail account (it should send you a notification that an unknown device tried accessing your account. Allow this device.)")
        print("""3. Try to wait at least 1 minute for this to process.
It make take an hour for the change to kick-in, 
so sit back, relax, and grab a coffee.""")
        print(
            "\n(I personally found that this works best on chrome after signing into my gmail and then clicking on the link.)\n")
        input(core.invis + "Please press {ENTER} to continue... ")
        print(rr + "")
        clear()
        startup()


# BOOTUP SCREEN
def startup():
    try:
        clear()
        print(line)
        core.gmaillogo()
        print(NP)
        print(line)
        core.gmailname()
        print("")
        print(core.rr + "[" + core.blue + "+" + core.rr + "] (Username Ex: username@gmail.com)")
        print(core.rr + "[" + core.blue + "+" + core.rr + "] (Password Ex: password1234)")
        print("")
        login()
    except KeyboardInterrupt:
        main.startup()
