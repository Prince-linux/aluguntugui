from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='optional')
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='optional')
    email = forms.EmailField(max_length=255, required=True,
                             help_text='valid email required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')
