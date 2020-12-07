from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='optional')
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='optional')
    email = forms.EmailField(max_length=255, required=True,
                             help_text='valid email required')

    def clean_email(self):
        # TODO: this works but it would be better to ensure uniqueness at
        # database level
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).count() > 0:
            raise ValidationError("A user with that email already exists")
        
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')
