from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

@shared_task
def send_contact_email(name, email, message):
    subject = 'New Contact Form Received'
    body = f'Name: {name}\nE-mail: {email}\nMessage: {message}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sadiqmustafayev20@gmail.com']

    # E-mail send
    send_mail(subject, body, from_email, recipient_list, fail_silently=True)


