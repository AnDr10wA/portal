from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', cotalog_view, name = 'cotalog_url'),
    path('products/<slug:slug>', category_detail, name = 'category_detail_url'),
    path('product/<str:category>/<slug:slug>', product_detail, name = 'product_detail_url'),


]

