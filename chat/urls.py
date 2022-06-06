from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('chats/<int:sender>/<int:receiver>/', chat_list, name='chat-detail'),
    path('chats/', chat_list, name='chat-list'),
    path('users/<int:pk>/', user_list, name='user-detail'),
    path('users/', user_list, name='user-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)