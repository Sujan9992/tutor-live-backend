from django.db import models
from account.models import User
import datetime
from django.core.cache import cache
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      
      def __str__(self):
            return self.full_name
      
      def last_seen(self):
            return cache.get('last_seen_%s' % self.user.full_name)

      def online(self):
            if self.last_seen():
                  now = datetime.datetime.now()
                  if now > self.last_seen() + datetime.timedelta(
                          seconds=settings.USER_ONLINE_TIMEOUT):
                        return False
                  else:
                        return True
            else:
                  return False

class Chat(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
     message = models.TextField(blank=True)
     timestamp = models.DateTimeField(auto_now_add=True)
     is_read = models.BooleanField(default=False)
     def __str__(self):
           return self.message
     class Meta:
           ordering = ('timestamp',)