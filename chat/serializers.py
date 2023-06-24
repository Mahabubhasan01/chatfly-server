from rest_framework import serializers
from .models import Message,ChatMessage,CustomUser

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
