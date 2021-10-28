from django.contrib import admin
from django.urls import path, include
from .views import get_message_form, save_form
urlpatterns = [
    path('', get_message_form, name = 'help_me'),
    path('submit', save_form, name= 'save_form_url' ),

    ]