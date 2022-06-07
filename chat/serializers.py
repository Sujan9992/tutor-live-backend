from rest_framework import serializers
from .models import *
from account.models import User

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['sender', 'receiver', 'message']