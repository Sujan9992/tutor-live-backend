from rest_framework import serializers
from .models import *
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    online = serializers.ReadOnlyField(source='userprofile.online')

    class Meta:
        model = User
        fields = ['id', 'full_name', 'password', 'online']

class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='full_name', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='full_name', queryset=User.objects.all())
    class Meta:
        model = Chat
        fields = ['sender', 'receiver', 'message', 'timestamp']