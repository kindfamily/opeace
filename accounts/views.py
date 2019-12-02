from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout
from .forms import *

def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        
        user = authenticate(username=name, password=pwd)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form":form})
    
def logout(request):
    django_logout(request)
    return redirect("/")

