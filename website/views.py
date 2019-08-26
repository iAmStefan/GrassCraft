from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')
def informations(request):
    return render(request, 'info.html')
def rules(request):
    return render(request, 'rules.html')
def staffRequests(request):
    form = ContactForm
    return render(request, 'staff.html', {'form': form})
def error404(request):
    return render(request, '404.html')

def sendmail(request):
    print('Campurile trebuie completate')
    if request.method == "POST":
        name = request.POST['cereri']
        return HttpResponse(name)
    message = ContactForm.server_name + " " + ContactForm.admin_q1 + " " + ContactForm.admin_q2 + " " + ContactForm.admin_q3 + " " + ContactForm.admin_q4
    if ContactForm.admin_q1.empty_value or ContactForm.admin_q2.empty_value or ContactForm.admin_q3.empty_value or ContactForm.admin_q4.empty_value:
        print('Campurile trebuie completate')
    else:
        send_mail(
        "Aplicatie pentru administrator",
        message,
        settings.EMAIL_HOST_USER,
        [ContactForm.email_adress])
    return render(request, 'staff.html')
