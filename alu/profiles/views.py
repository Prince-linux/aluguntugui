from django.shortcuts import render, redirect
from .models import Profile, Timeline

def home(request):
    if request.user.is_authenticated:
        return render(request, 'profiles/home.html', {
            'profile': request.user.profile,
            'timeline': Timeline.objects.get_user_timeline(request.user)
        })
    else:
        return redirect('index')
