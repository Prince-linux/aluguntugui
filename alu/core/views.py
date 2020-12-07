from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .forms import RegistrationForm

def home(request):
    if request.user.is_authenticated:
        return redirect('profiles:home')
    else:
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
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return render(request, 'core/registration_done.html', {
                'page_title': 'Registration Complete'})
    else:
        form = RegistrationForm()
    return render(request, 'core/registration.html', {
        'form': form,
        'page_title': 'Registration',
    })

def activate(request, uidb64, token):
    UserModel = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except:
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'core/activated.html', {
            'page_title': 'Account Active',
        })
    else:
        return render(request, 'core/activation_failed.html', {
            'page_title': 'Activation Failed',
        })
    
    
