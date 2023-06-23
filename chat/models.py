from django.db import models

class ChatMessage(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add additional fields if necessary (e.g., sender, room, etc.)
