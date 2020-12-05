from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('home')
    else:
        messages.error(request, "Authentication failed")
        return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')
    
