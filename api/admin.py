# api/admin.py
from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'messagetext')  # Columns to display
    search_fields = ('name', 'email')  # Fields to search

admin.site.register(Message, MessageAdmin)