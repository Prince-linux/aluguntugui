from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import QueuedEmail

def send_emails():
    # TODO: limit the number of emails each time this function runs
    for qe in QueuedEmail.objects.all():
        user = qe.user
        template = qe.template
        data = qe.data
        data['user'] = user
        subject = qe.subject
        message = render_to_string(template, data)
        dest = user.email
        try:
            email = EmailMessage(subject, message, to=[dest])
            email.send()
            qe.delete()
        except Exception as e:
            print("Failed to send email: {}".format(e))
            
