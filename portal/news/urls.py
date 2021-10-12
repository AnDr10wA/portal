from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', news_list, name = 'news_list_url'),
    # path('create', NewsCreate.as_view(), name = 'news_create_url'),
    path('<str:slug>', NewsDetail.as_view(), name = 'news_detail_url'),


]
