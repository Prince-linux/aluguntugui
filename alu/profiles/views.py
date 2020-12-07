from django.shortcuts import render, redirect
from .models import Profile

def home(request):
    if request.user.is_authenticated:
        return render(request, 'profiles/home.html', {
            'profile': request.user.profile,
        })
    else:
        return redirect('index')
