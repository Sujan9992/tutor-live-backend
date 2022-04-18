from django.urls import path
from .views import *

urlpatterns = [
    path('chats/<int:sender>/<int:receiver>/', chat_list, name='chat-detail'),
    path('chats/', chat_list, name='chat-list'),
    path('users/<int:pk>/', user_list, name='user-detail'),
    path('users/', user_list, name='user-list'),
]