from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "accounts"


urlpatterns = [
    path('register', register_request, name = "register"),
    path('login', login_request, name = 'login'),
    path('logout', logout_request, name = 'logout')


    ]