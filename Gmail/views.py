import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def mail(request):
    subject = 'Python(Selenium)'
    my_name = 'Shekhar Ghorwade'
    body = f'Hello, \n\nI am completed given assienment the link of my git repositry and google  form image is attach with the mail  '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['']
    cc_list = ['cc@example.com']
    
    # Create the email message
    email = EmailMessage(subject, body, email_from, recipient_list)
    image_path = os.path.join(settings.MEDIA_ROOT, 'Python(Selenium).jpeg')
    email.attach_file(image_path)
    
    # Attach the image
    
    try:
        email.send()
        return HttpResponse("Email sent successfully with image!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")