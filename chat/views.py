from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework import generics
from .models import Message, CustomUser, ChatMessage
from .serializers import ChatMessageSerializer, MessageSerializer, CustomUserSerializer


# ChatMessage API views
class ChatMessageList(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


class ChatMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


# Message API views
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# CustomUser API views
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Save chat messages view
def save_chat_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')
        receiver = request.POST.get('receiver')

        # Create a new ChatMessage instance
        chat_message = ChatMessage(content=message_content, receiver=receiver)
        chat_message.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login successful
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            # Login failed
            return JsonResponse({'message': 'Invalid username or password'}, status=401)
