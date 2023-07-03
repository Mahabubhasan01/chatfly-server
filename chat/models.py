from email.policy import default
import imp
from tkinter.tix import Tree
from django.db import models
# myapp/models.py
import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, full_name, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        if not full_name:
            raise ValueError('The Full Name field must be set')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, password=None):
        user = self.create_user(
            email=email,
            username=username,
            full_name=full_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(
        verbose_name="username", max_length=200, unique=True)
    full_name = models.CharField(
        verbose_name="fullname", max_length=200, blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/profile_image.png')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email


class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add additional fields if necessary (e.g., sender, room, etc.)


class ChatMessage(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='sent_messages', null=True)
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='received_messages', blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username}'
