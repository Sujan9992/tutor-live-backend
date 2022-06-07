from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from account.serializers import UserProfileSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def chat_list(request):
    if request.method == 'GET':
        user = request.user
        if user:
            chats = Chat.objects.filter(sender=user)
            serializer = ChatSerializer(chats, many=True)
            return Response(serializer.data)

@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def chatHeads(request):
    if request.method == 'GET':
        user = request.user
        if user:
            chats = Chat.objects.filter(receiver=user)
            serializer = ChatSerializer(chats, many=True)
            return Response(serializer.data)

@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def chat_detail(request, sender, receiver):
    if request.method == 'GET':
        chats = Chat.objects.filter(sender=sender, receiver=receiver)
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def chat_create(request, sender, receiver):
    if request.method == 'POST':
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)