from django.contrib import admin
from .models import *

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'timestamp', 'is_read']
    list_filter = ['sender', 'receiver']
    search_fields = ['message']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']
    search_fields = ['user']

admin.site.register(Chat, ChatAdmin)
admin.site.register(UserProfile, UserProfileAdmin)