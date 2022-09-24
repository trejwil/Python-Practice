import smtplib
import os
from email.message import EmailMessage
import ssl

sender_email = "myscriptnew@gmail.com"
receiver_email = "placeholder" #set this to scrape email client or take input
email_password = os.environment.get #create environment variable later

subject = input("Subject: ")
body = """"


"""
em = EmailMessage()
em["from"] = sender_email
em["To"] = receiver_email
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender_email, email_password)
    smtp.sendmail(sender_email, receiver_email, em.as_string())
