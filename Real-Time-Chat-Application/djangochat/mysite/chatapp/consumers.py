from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync, sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom,ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        print("WebSocket connected")

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("WebSocket disconnected")

    async def receive(self, text_data):
        data = json.loads(text_data)

        message = data['message']
        user_name = data['user_name']
        room = data['room_name']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_name': user_name,
                'room': room,
            }
        )

        await self.save_message(user_name,room,message)

    async def chat_message(self, event):
        message = event['message']
        user_name = event['user_name']
        room = event['room']

        await self.send(
            text_data=json.dumps({
                'message': message,
                'user_name': user_name,
                'room': room,
            })
        )


    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room)
        ChatMessage.objects.create(user=user, room=room, message_content=message)

