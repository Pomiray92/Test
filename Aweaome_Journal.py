
from distutils.errors import LinkError
import os
import smtplib
import time
import datetime
import smtpd
from   email.mime.multipart import *    # Optional (& advanced)
from   email.mime.text      import *    # Optional (& advanced)
from   colorama             import *    # Optional (& advanced)
from   art                  import *    # Optional (& advanced)

    # Initializing colorama
init()

    # Datetime variable
now       = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")

#   email function  (optional & advanced)
# def gmail_send(subject, message, from_mail, to_mail, password):
#     global link
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from_mail, password)
#     msg            = EmailMessage()
#     message        = f'{message}'
#     msg.set_content(message)
#     msg['Subject'] = subject
#     msg['From']    = from_mail
#     msg['To']      = to
#     server.send_message(msg)


# open_file = ("journal.text", "r")
# file_content = open_file.read()
# print(file_content)
# open_file.close()


print(Fore.LIGHTCYAN_EX + "")               # Open Art funk
                                            #...............
tprint("AWESOME JOURNAL", font="random")    # Art library
                                            #...............
print(""+Style.RESET_ALL)                   # Close Art funk


new_entry = input("ENTER DIARY ENTRY HERE >>> ")


here = os.getcwd().replace("\\","/")    # defining path variable for later if statement

    # Display current
if os.getcwd() in new_entry:    # If weird path things in entry, dont save entry
    print("Something went wrong. NOT ADDING") 

elif new_entry != "":    # If entry is not empty
    with open("Journal.txt", "a") as file:
        file.write(now + "  " + new_entry + "\n")   
else:
    print("Empty sting. NOT ADDING")  