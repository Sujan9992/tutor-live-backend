from django.db import models
from account.models import User
import datetime
from django.core.cache import cache
from django.conf import settings

# Create your models here.

class Chat(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
     message = models.TextField(blank=True)
     def __str__(self):
           return self.message
#      class Meta:
#            ordering = ('timestamp',)