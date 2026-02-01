import logging
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Roles
from ..serializers import RolesSerializer

logger = logging.getLogger(__name__)


#get all roles
@api_view(['GET'])
def getRoles(request):
    roles = Roles.objects.all()
    serializer = RolesSerializer(roles,many=True)
    return Response(serializer.data)

#get single role
@api_view(['GET'])

def getRole(request,pk):
    try:
        role = get_object_or_404(Roles, id=pk)
    except Http404:
        logger.error(f"Role with id={pk} not found")
        raise
    serializer = RolesSerializer(role,many=False)
    return Response(serializer.data)

#add role
@api_view(['POST'])
def addRole(request):
    serializer = RolesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update role
@api_view(['PUT'])
def updateRole(request,pk):
    try:
        role = get_object_or_404(Roles, id=pk)
    except Http404:
        logger.error(f"Role with id={pk} not found for update")
        raise
    serializer = RolesSerializer(instance=role, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete role
@api_view(['DELETE'])
def deleteRole(request,pk):
    try:
        role = get_object_or_404(Roles, id=pk)
    except Http404:
        logger.error(f"Role with id={pk} not found for deletion")
        raise
    role.delete()
    return Response('Item successfully deleted')