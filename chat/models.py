from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group as AuthGroup


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True,blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        AuthGroup,
        verbose_name='groups',
        blank=True,
        related_name='zayan'  # Provide a unique related_name
    )

    def __str__(self):
        return self.email


class ChatMessage(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add additional fields if necessary (e.g., sender, room, etc.)


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender.email}, To: {self.receiver.email}"
