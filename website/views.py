from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
import smtplib

def index(request):
    return render(request, 'index.html')
def informations(request):
    return render(request, 'info.html')
def rules(request):
    return render(request, 'rules.html')
def staffRequests(request):
    form = ContactForm()
    return render(request, 'staff.html', {'form': form})
def error404(request):
    return render(request, '404.html')

def sendmail(request):
    form = ContactForm()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.connect("smtp.gmail.com", 465)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("taloistefanel8@gmail.com", "nvhscmqlgkhggzcy")
    server.sendmail(
      "from@address.com",
      "to@address.com",
      "this message is from python")
    server.quit()
    #print('Da')
    #if form.is_valid():
    #    message = ContactForm.server_name + " " + ContactForm.admin_q1 + " " + ContactForm.admin_q2 + " " + ContactForm.admin_q3 + " " + ContactForm.admin_q4
    #    send_mail(
    #    "Aplicatie pentru administrator",
    #    message,
    #    ContactForm.email_adress,
    #    [settings.EMAIL_HOST_USER],
    #    fail_silently= False,
    #    )
    return render(request, 'staff.html', {'form': form})
