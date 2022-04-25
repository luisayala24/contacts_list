from django.shortcuts import render

from django.http import HttpResponse

from contactslist.models import Contacts

def index(request):
    return HttpResponse('Hello')

def display(request):
    contacts = Contacts.objects.all() 
    
    s=""
    for c in contacts:
        s+=c.to_string()+'<br>'
    return HttpResponse("Contacts:<br>"+s)    