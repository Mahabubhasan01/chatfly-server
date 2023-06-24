from django.contrib import admin

from chat.models import ChatMessage, Message,CustomUser
# Register your models here.
admin.site.register(ChatMessage)
admin.site.register(Message)
admin.site.register(CustomUser)
