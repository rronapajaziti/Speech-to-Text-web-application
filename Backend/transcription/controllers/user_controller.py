import logging
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import User
from ..serializers import UserSerializer

logger = logging.getLogger(__name__)

#get all users

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

#get single user
@api_view(['GET'])

def getUser(request,pk):
    try:
        users = get_object_or_404(User,id=pk)
    except Http404:
        logger.error(f"User with id={pk} not found")
        raise
    serializer = UserSerializer(users,many=False)
    return Response(serializer.data)

#add user
@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update user
@api_view(['PUT'])
def updateUser(request,pk):
    try:
        user = get_object_or_404(User, id=pk)
    except Http404:
        logger.error(f"User with id={pk} not found for update")
        raise
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete user
@api_view(['DELETE'])
def deleteUser(request,pk):
    try:
        user = get_object_or_404(User, id=pk)
    except Http404:
        logger.error(f"User with id={pk} not found for deletion")
        raise
    user.delete()
    return Response('Item successfully deleted')