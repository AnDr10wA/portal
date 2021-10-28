
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', main_view, name = 'main_forum_url'),
    path('category/<slug:slug>', category_forum_deteil, name = 'detail_category_forum_url'),
    path('topic/<slug:slug>', topic_detail, name = 'topic_detail_url'),
    path('message/', save_message, name = 'message_form_url' )

]