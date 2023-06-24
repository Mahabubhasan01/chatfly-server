from django.http import JsonResponse
from .models import Message, ChatMessage, CustomUser
from .serializers import MessageSerializer, CustomUserSerializer
from rest_framework import generics


def save_chat_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')

        # Create a new ChatMessage instance
        chat_message = Message(content=message_content)
        chat_message.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
