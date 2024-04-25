import os
import ssl
import smtplib

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    
    username = "max.solo213@gmail.com"
    password = os.getenv("PASSWORD")
    
    context = ssl.create_default_context()
    receiver = "max.solo213@gmail.com"
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    
if __name__ == "__main__":
    send_email()
    