#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def sendemail():
    print("eiei")
    user = "todolistthinknot@gmail.com"
    receiver = 'onwanyaardsana@gmail.com'
    password = "todo123456"
    subject = 'Python!'

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = receiver
    msg['Subject'] = subject

    body = 'send email from python'
    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)

    server.sendmail(user, receiver , text )
    server.quit()

if __name__ == '__main__':
    main()
 

    
