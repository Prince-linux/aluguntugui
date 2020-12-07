from django.shortcuts import render
from .models import Profile

def home(request):
    return render(request, 'profiles/home.html', {
        'profile': request.user.profile,
    })
