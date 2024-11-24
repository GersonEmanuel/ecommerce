from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model, logout
from .forms import *

# Create your views here.
def home_page(request):
    context={'title': 'pricipal page', 'content':'principal'}
    if request.user.is_authenticated:
        context['premium_content'] = 'you are a premium user' 
    return render(request, 'index.html', context)

def about_page(request):
    context = {'title':'about page', 'content':
               'welcome to about page'}
    return render(request, 'about_page.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {'title': 'contact page', 'content':'Welcome contact page', 'form': contact_form }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    
    return render(request, 'contact_page.html', context)

