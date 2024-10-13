from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(error_messages= {'required': 'Your name is required ' },widget = forms.TextInput(attrs={'class':'form_control', 'placeholder': 'Tell us your name'}))
    email = forms.EmailField(error_messages={'invalid': 'input a valid email'},widget= forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'input your email'}))
    content = forms.CharField(error_messages={'required': 'its required a message '},widget= forms.Textarea(attrs= {'class': 'form_control', 'placeholder': 'send us a message'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com")
        return email