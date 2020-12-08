from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Profile, Timeline

#def home(request):
#    if request.user.is_authenticated:
#        return render(request, 'profiles/home.html', {
#            'profile': request.user.profile,
#            'timeline': Timeline.objects.get_user_timeline(request.user)
#        })
#    else:
#        return redirect('index')

@login_required
def view_profile(request, uid):
    UserModel = get_user_model()
    user = UserModel.objects.get(pk=uid)
    return render(request, 'profiles/profile.html', {
        'profile': user.profile,
        'timeline': Timeline.objects.get_user_timeline(user)
    })
