from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer

# List and create messages
@api_view(['GET', 'POST'])
def MessageListCreate(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, and delete a specific message
# @api_view(['GET', 'PUT', 'DELETE'])
# def MessageDetail(request, pk):
#     try:
#         message = Message.objects.get(pk=pk)
#     except Message.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MessageSerializer(message)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = MessageSerializer(message, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         message.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
