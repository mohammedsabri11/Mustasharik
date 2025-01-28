"""
Definition of urls for Mustasharik.
"""

from datetime import datetime
from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contract/', views.contract, name='contract'),
    path('chat-with-gpt/', views.chat_view, name='chat-with-gpt'),
  
   
]
