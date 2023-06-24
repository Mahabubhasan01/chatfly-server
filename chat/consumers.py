import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'chat_room'

        # Join the room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data.get('message')

        if message_content:
            # Save the chat message asynchronously
            await self.save_chat_message(message_content)

            # Broadcast the message to all connected clients
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message_content
                }
            )

    @database_sync_to_async
    def save_chat_message(self, message_content):
        # Create and save the ChatMessage instance
        chat_message = Message(content=message_content)
        chat_message.save()

    async def chat_message(self, event):
        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
