from django.http import JsonResponse
from .models import ChatMessage

def save_chat_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')

        # Create a new ChatMessage instance
        chat_message = ChatMessage(content=message_content)
        chat_message.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
