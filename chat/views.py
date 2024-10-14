from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
