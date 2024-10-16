# api/urls.py
from django.urls import path
from .views import MessageListCreate

urlpatterns = [
    path('messages/', MessageListCreate, name='message-list-create'),
    
]