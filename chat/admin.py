from django.contrib import admin

from chat.models import  Message,ChatMessage,CustomUser
# Register your models here.
admin.site.register(Message)
admin.site.register(ChatMessage)
admin.site.register(CustomUser)
