from django import forms
from django.contrib.auth import get_user_model
from django.http import HttpResponse

user = get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(error_messages= {'required': 'Your name is required ' },widget = forms.TextInput(attrs={'class':'form_control', 'placeholder': 'Tell us your name'}))
    email = forms.EmailField(error_messages={'invalid': 'input a valid email'},widget= forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'input your email'}))
    content = forms.CharField(error_messages={'required': 'its required a message '},widget= forms.Textarea(attrs= {'class': 'form_control', 'placeholder': 'send us a message'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("The email should be from gmail")
        return email
    
class LoginForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'confirm password', widget= forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = user.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('this user already exists')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = user.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError('this email is already register')
        return email
    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('the passwords should be equals')
        return data
