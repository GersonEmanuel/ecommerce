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
    
