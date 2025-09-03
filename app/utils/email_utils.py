import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

# EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

EMAIL_ADDRESS="kylinja@gmail.com"
EMAIL_PASSWORD="rjmgzouxmqmszytc"


def send_email():
    msg = MIMEMultipart("Hello, this is a plain text email.")
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = "test email"

    # msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            try:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            except Exception as e:
                print("error logging in :",e)
                server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        # return True
    except Exception as e:
        print("Error sending email:", e)
        # return False
    print("email sent")
    
    send_email()
