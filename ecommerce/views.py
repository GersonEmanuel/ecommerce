from django.shortcuts import render, redirect
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

def login_page(request):
    form = LoginForms(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password) 
    if user is not None:
        login(request, user)
        return redirect('')
    return render(request, 'auth/login.html', context)

def logout_page(request):
    logout(request)
    return render(request, 'auth/logout.html')

User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)


