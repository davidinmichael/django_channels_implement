from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .serializers import ChatSerializer
from .models import Chats


class ChatsView(APIView):

    def get(self, request):
        chats = Chats.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            notif = serializer.save()
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {
                    "type": "send_notification",
                    "message": f"{notif.message} Created at {notif.time_created}"
                }
            )
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
