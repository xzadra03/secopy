from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
# request handler

def theory(request):
    return render(request, 'theory.html')

def test(request):
    return render(request, 'test.html')

def download(request):
    return render(request, 'downloads.html')

def intro(request):
    return render(request, 'index.html')

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

def logout_user(request):
    if request.method == "POST":
        logout(request)
    
    return redirect("/")