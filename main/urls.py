#URL Configuration of Main APP
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from .import views
urlpatterns = [
    
    path('',views.getInput,name = "get-input"),
    path('sendEmail',views.sendEmail,name="send-email")
]