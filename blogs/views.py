from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse

# Create your views here.
'''
def hello(request):
    return HttpResponse('<h2>Hello~~~ :)<h2>')
'''

def home(request):
    return render(request,'index.html',
    {
        'name' : 'Project',
        'author' : 'Toto and friends'
    })

def menu1(request):
    return render(request,'menu1.html')

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

    return HttpResponse(server.sendmail(user, receiver , text ))