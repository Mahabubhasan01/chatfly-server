from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import JsonResponse
from .models import Message, CustomUser, ChatMessage
from .serializers import ChatMessageSerializer, MessageSerializer, CustomUserSerializer
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


def save_chat_messages(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')

        # Create a new ChatMessage instance
        chat_message = ChatMessage(content=message_content)
        chat_message.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


class ChatMessageList(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


class ChatMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

# Customuser-api


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login successful
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            # Login failed
            return JsonResponse({'message': 'Invalid username or password'}, status=401)
