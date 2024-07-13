# In views.py use the some library for initalize the my gmail account and mail functionalites 
# My gmail is initalize in setting.py to initalize my email and credantials 
import os

from django.http import HttpResponse  
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def mail(request):
    subject = 'Python(Selenium)'#set the subject for mail
    my_name = 'Shekhar Ghorwade' 
    git_repo = 'https://github.com/ghorwade24/Django-Assignment'
    body = f'Hello, \n\nI am {my_name} I completed given assienment the assienment code is \n in my git repository {git_repo} '
    email_from = settings.EMAIL_HOST_USER #host user means sender 
    recipient_list = ['tech@themedius.ai'] # initalize the reciver user
    cc_list = ['hr@themedius.ai']

    
    email = EmailMessage(subject, body, email_from, recipient_list,cc_list)#this is function for geting the parameter for sending the mail 
    
    # Attach the image
    image_path = os.path.join(settings.MEDIA_ROOT, 'Python(Selenium).jpeg')
    email.attach_file(image_path)# attach_file is function to use to attch the files
    
    
    
    try:
        email.send()
        return HttpResponse("Email sent successfully with image!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")