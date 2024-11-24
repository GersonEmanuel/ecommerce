from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from ecommerce.forms import LoginForms, RegisterForm
from django.http import HttpResponse
from django.utils.http import url_has_allowed_host_and_scheme

# Create your views here.

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
            return redirect('home')
    return render(request, 'auth/login.html', context)


def logout_page(request):
    context = {'content': 'logout was successfully'}
    logout(request)
    return render(request, 'auth/logout.html', context)

User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
            "form": form
              }
    if form.is_valid():
        username = form.clean_username()
        email = form.clean_email()
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username=username,email=email,password=password)
        print(new_user)
        return redirect('home')
    return render(request, "auth/register.html", context)



