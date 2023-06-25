from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add additional fields if necessary (e.g., sender, room, etc.)


class ChatMessage(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages', null=True)
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages', blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username}'
