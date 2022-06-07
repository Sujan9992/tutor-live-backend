from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('chats/<int:sender>/<int:receiver>/', chat_list, name='chat-detail'),
    path('chats/', chat_list, name='chat-list'),
    path('chatHeads/', chatHeads, name='chatHeads'),
    path('chatDetails/<int:sender>/<int:receiver>/', chat_detail, name='chat-detail'),
    path('chatCreate/<int:sender>/<int:receiver>/', csrf_exempt(chat_create), name='chat-create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)