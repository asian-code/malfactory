#!/usr/bin/python

#smtplib module send mail
#server.login(gmail_sender, gmail_passwd)
#server.sendmail(gmail_sender, [TO], BODY)

import sys
import smtplib
import os 
import imaplib          
import core
import main

#defines the server for gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
mail = imaplib.IMAP4_SSL('imap.gmail.com') #port 993
server.ehlo()
server.starttls()
server.ehlo()

#defines everything for the webpage
url = "https://mail.google.com/mail/u/0/#inbox"

#CLEARS THE SCREEN
def clear():
  core.clear()

def quit():
  core.quit()

def inbox(username, password):
  try:
    while True:
      answer = input(core.red + "G" + core.white + "mail" + core.yellow + " > " + core.r + "")
      answer = answer.split(" ")
      if answer[0] == "help":
        print("\n-----------\n")
        print(core.ul + "The Help/Command Menu" + core.r)
        print("\nhelp - Opens this help menu")
        print("send <spoofemail@fakewebsite.com> <sendingto@gmail.com> - Send an email with your gmail account")
        print("exit - Go back to the homepage")
        print("\n-----------\n")
      elif answer[0] == "exit":
        main.startup()
      elif answer[0] == "send":
        try:
           FROM = answer[1]
           TO = answer[2]
           SUBJECT = input("\nSubject: ")
           print("\n--- Type 'quit' to Finish! ---")
           TEXT = ""
           x = 1
           while True:
              message = input(str(x) + ": ")
              if message.lower() =="quit" or message.lower()=="q":
                  print("\n")
                  break
              TEXT = TEXT + message +"\n"
              x += 1
           BODY = '\r\n'.join(['To: %s' % TO,
           'From: %s' % FROM,
           'Subject: %s' % SUBJECT,
           '', TEXT])
           try:
              server.sendmail(username, [TO], BODY)
              print ('Your email was sent!')
           except:
              print ("Error sending mail! Does the recipient's email exist?")
        except:
          print("\nError: Could not send email! Your command was incorrectly set.\n")
      else:
        print("\nCommand '" + str(answer) + "' was not found. Please type 'help' for help.\n")
  except KeyboardInterrupt:
    main.startup()
  except:
    print("\nError: Can't find input.\n")
    

#LOGIN INTO GMAIL
def login():
  try:
    gmail_sender = input("Please put your Gmail Username: ")
    gmail_sender = str(gmail_sender)
    gmail_passwd = input("Please enter your password: " + core.invis)
    gmail_passwd = str(gmail_passwd)
    if gmail_sender == "" or gmail_passwd == "":
      print(core.r + "\nSorry! You used an unknown character. Please type in your credentials correctly!")
      input("Please press {ENTER} to continue... " + core.invis)
      print(core.r + "")
      startup()
    authenticate(gmail_sender, gmail_passwd)
  except KeyboardInterrupt:
    main.startup()

#LOGGING INTO THE ACCOUNT
def authenticate(username, password):
  try:
      clear()
      server.login(username, password)
      mail.login(username, password)
      inbox(username, password)
  except smtplib.SMTPAuthenticationError:
      clear()
      core.logo()
      core.name()
      print(core.lcyan + core.bold + "\nUTHENTICATION ERORR!:\n")
      print (core.lblue + "Cannot sign in. Are you sure this account exists?:" + core.r)
      print("\nRight now, the reason you may not log-into your gmail account (if your cresidentials are right) is because google sees this form of authentication as 'less secure'.\n")
      print(core.bold + core.lblue + "How to fix this issue:" + core.r)
      print(core.white + """
1. Login to your Gmail Account
2. Open the link:""")
      print(core.lcyan + core.ul + "https://www.google.com/settings/security/lesssecureapps" + core.r)
      print("3. Allow less secure app access to your gmail account.\n")
      print (core.bold + core.lblue + "I allowed unsecure apps. Why is it still not working?:" + core.r)
      print("""\nSo now it appears you typed in your
cresidentials correctly and allowed unsecure apps, but it still doesnt work. 
      
This is because google doesn't know if the location of the device accessing your gmail (in this case, the tool itself), is by you.\n""")
      print(core.bold + core.lblue + "How to fix this issue as well:" + core.r)
      print("\n1. Allow the location of the device by openining the link:")
      print(core.lcyan + core.ul + "https://www.google.com/settings/security/lesssecureapps" + core.r)
      print("2. If this link does not work, perform it manually from your Gmail account (it should send you a notification that an unknown device tried accessing your account. Allow this device.)")
      print("""3. Try to wait at least 1 minute for this to process.
It make take an hour for the change to kick-in, 
so sit back, relax, and grab a coffee.""")
      print("\n(I personally found that this works best on chrome after signing into my gmail and then clicking on the link.)\n")
      input(core.invis + "Please press {ENTER} to continue... ")
      clear()
      startup()

#BOOTUP SCREEN
def startup():
  try:
    clear()
    core.logo()
    core.name()
    print("")
    print("(Username Ex: username@gmail.com)")
    print("(Password Ex: password1234)")
    print("")
    login()
  except KeyboardInterrupt:
    main.startup()
