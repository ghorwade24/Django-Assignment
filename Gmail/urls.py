from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.mail, name="Sending mails"),# This url of our views.py in this we create the mail function
    
]
