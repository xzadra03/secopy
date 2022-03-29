#
# file: views.py
# author: Jan Zádrapa, BUT FIT
# date: 3/2022
# brief: handler for certain situations 
#

from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

#requested site theory
def theory(request):
    return render(request, 'theory.html')

#requested site test
def test(request):
    return render(request, 'test.html')

#requested site downloads
def download(request):
    return render(request, 'downloads.html')

#requested site home
def intro(request):
    return render(request, 'index.html')

#login validator
def auth_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("../")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#register validator
def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()
            login(request, user)
            messages.success(request, "Registration succesful.")
            return redirect("../")
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)

#logout function, them redirect home
def logout_user(request):
    if request.method == "POST":
        logout(request)
    
    return redirect("/")