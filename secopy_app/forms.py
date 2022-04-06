#
# file: urls.py
# author: Jan Zádrapa, BUT FIT
# date: 3/2022
# brief: file for setting and hadling registration form used in SeCoPy
#
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError   

#class for customizing Django registration form
class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'joedoe1'}), label='Username', min_length=5, max_length=150)  
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@domain.com'}), label='Email')  
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))
    organisation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BUT'}), label='Organisation', max_length=150)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Joe'}), label='Name', max_length=150)
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}), label='Surname', max_length=150)
         
    #method for checking if email is not already registered
    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("Email Already Exist")  
        return email  
    
    #password checker
    #password must be confirmed by writing again
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
    
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Passwords don't match")  
        return password2  
     
    #save new user to database
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']
        )  
        return user  