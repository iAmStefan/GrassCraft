from django import forms

class ContactForm(forms.Form):
    admin = "admin"
    helper = "helper"
    builder = "builder"
    recover = "recover"
    server_name = forms.CharField(required= False, label = "Numele de pe serverul de Minecraft", widget = forms.TextInput(attrs = {'class' : 'serverName'}))
    email_adress = forms.EmailField(required = False, label = "Adresa de e-mail", widget = forms.EmailInput(attrs = {'class' : 'emailAddress'}))
    admin_q1 = forms.CharField(required= False, label = "Ce faci daca cineva face reclama la canal de Youtube ?", widget = forms.TextInput(attrs = {'class' : 'admin'}))
    admin_q2 = forms.CharField(required = False, label = "Ce faci daca cineva face abuz de /helpop ?", widget = forms.TextInput(attrs = {'class' : 'admin'}))
    admin_q3 = forms.CharField(required = False, label = "Ce faci daca cineva foloseste hack/cheat ?", widget = forms.TextInput(attrs = {'class' : 'admin'}))
    admin_q4 = forms.CharField(required = False, label = "Ce faci daca cineva face reclama la un server de Minecraft ?", widget = forms.TextInput(attrs = {'class' : 'admin'}))

    helper_q1 = forms.CharField(required= False, label = "Cat timp se da mute la limbaj licentios ?", widget = forms.TextInput(attrs = {'class' : 'helper'}))
    helper_q2 = forms.FileField(required = False, label = "Dovada cu orele jucate {minim 20 ore}", widget = forms.FileInput(attrs = {'class' : 'helper_Q2'}))
    helper_q3 = forms.CharField(required = False, label = "Daca ajungi helper cum vei ajuta serverul ?", widget= forms.Textarea(attrs = {'class' : 'helper' , 'rows' : 3}))

    builder_q1 = forms.CharField(required = False, label = "Cat timp ai stat cel mai mult la o constructie ?", widget = forms.TextInput(attrs = {'class' : 'builder'}))
    builder_q2 = forms.FileField(required = False, label = "Poza cu niste constructii", widget = forms.FileInput(attrs = {'class' : 'builder_Q2'}))
    builder_q3 = forms.CharField(required = False, label = "Daca ai fi un animal ce animal ai fi ?", widget= forms.TextInput(attrs = {'class' : 'builder'}))

    recover_q1 = forms.FileField(required = False, label = "Poza cu numele pe server", widget = forms.FileInput(attrs = {'class' : 'recover_Q1'}))
    recover_q2 = forms.CharField(required = False, label = "Numele de discord", widget = forms.TextInput(attrs = {'class' : 'recover'}))
    recover_q3 = forms.CharField(required = False, label = "Data pierderii parolei", widget= forms.TextInput(attrs = {'class' : 'recover'}))
