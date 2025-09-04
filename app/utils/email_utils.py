import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(subject: str, recipient: str, body: str):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            try:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            except Exception as e:
                print("error logging in :",e)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
