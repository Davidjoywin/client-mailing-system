import os

import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv


load_dotenv()

email_addr = os.getenv("base_email_address")
app_password = os.getenv("email_app_password")

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    print("Connection Successful")
    server.starttls()
    server.login(email_addr, app_password)
    print("Base email Authenticated Successfully")

except smtplib.SMTPAuthenticationError:
    print("Authentication Error has occurred")

except smtplib.SMTPConnectError:
    print("An error has occurred. Check your network!")

email_msg = EmailMessage()
email_msg['Subject'] = "Testing subject"
email_msg['From'] = email_addr

def send_message(recv_addr, msg):
    email_msg['To'] = recv_addr
    email_msg.set_content(msg)
    msg = f"Subject: {"Testing subject"}\n\n{msg}"

    try:
        # server.sendmail(email_addr, recv_addr, msg)
        server.send_message(email_msg)
        print("Mail sent successfully")
    except smtplib.SMTPRecipientsRefused:
        print("Mail failed to send")
    

if __name__ == "__main__":
    recv_addr = "davidjoy2k18@gmail.com"

    msg = "hello world"
    send_message(recv_addr, msg)
    