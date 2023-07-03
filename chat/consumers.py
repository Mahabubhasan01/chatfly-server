import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import ChatMessage, CustomUser


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'chat_room'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message_content = data.get('message')
            receiver_id = data.get('receiver_id')

            if message_content and receiver_id:
                receiver = await self.get_receiver(receiver_id)
                await self.save_chat_message(message_content, receiver)
                await self.channel_layer.group_send(self.room_group_name, {'type': 'chat_message', 'message': message_content})

        except json.JSONDecodeError:
            print('Invalid JSON data received')
            print('Received data:', text_data)

    @database_sync_to_async
    def get_receiver(self, receiver_id):
        return CustomUser.objects.get(id=receiver_id)

    @database_sync_to_async
    def save_chat_message(self, message_content, receiver):
        chat_message = ChatMessage(content=message_content, receiver=receiver)
        chat_message.save()

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
