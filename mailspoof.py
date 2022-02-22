import smtplib
from email.message import EmailMessage
import os
import time

def server():
	global server
	print("[+] Connecting..")
	server = smtplib.SMTP('mail.smtp2go.com',2525)
	server.starttls()
	server.login("akashadmin124","admin")
	os.system("clear")

server()
sender = input("enter the sender mail : ")
reciever = input("enter the reciever mail: ")
subject = input("enter the subject: ")
message = input("enter the body of the message: ")

email = EmailMessage()
email['From'] = sender
email['To'] = reciever
email['Subject'] = subject
email.set_content(message)

print("[+]Sending...")
server.send_message(email)
os.system("clear")
print("Sent Sucessfully!")