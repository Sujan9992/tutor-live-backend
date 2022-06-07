from django.contrib import admin
from .models import *

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ['sender']
    list_filter = ['sender', 'receiver']
    search_fields = ['message']

admin.site.register(Chat, ChatAdmin)