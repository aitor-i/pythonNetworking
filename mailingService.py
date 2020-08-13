import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.www.gooogle.com", 25)

server.ehlo()

mail = input("Enter your gmail domain: ")

password = input("Enter your password: ")

server.login(mail, password)

msg = MIMEMultipart()
msg["from"] = ""
msg["to"] = ""
msg["subject"] = ""

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))
