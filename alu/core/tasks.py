from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from .models import Activation

def send_emails():
    for activation in Activation.objects.all():
        user = activation.user
        subject = "Activate your account"
        message = render_to_string('core/activation_email.html', {
            'user': user,
            'host': settings.HOST,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        dest = user.email
        try:
            email = EmailMessage(subject, message, to=[dest])
            email.send()
            activation.delete()
        except:
            print("Failed to send email")
