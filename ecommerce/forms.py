from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(attrs={'class':'form_control', 'placeholder': 'Tell us your name'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs='class': 'form_control', 'placeholder': 'input your email'))
    content = forms.CharField(widget= forms.Textarea(attrs= 'class': 'form_control', 'placeholder': 'send us a message'))