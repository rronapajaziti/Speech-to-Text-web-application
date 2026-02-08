import logging
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Language
from ..serializers import LanguageSerializer

logger = logging.getLogger(__name__)


# get all languages
@api_view(['GET'])
def getLanguages(request):
    languages = Language.objects.all()
    serializer = LanguageSerializer(languages, many=True)
    return Response(serializer.data)


# get single language
@api_view(['GET'])
def getLanguage(request, pk):
    try:
        language = get_object_or_404(Language, id=pk)
    except Http404:
        logger.error(f"Language with id={pk} not found")
        raise
    serializer = LanguageSerializer(language, many=False)
    return Response(serializer.data)


# add language
@api_view(['POST'])
def addLanguage(request):
    serializer = LanguageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# update language
@api_view(['PUT'])
def updateLanguage(request, pk):
    try:
        language = get_object_or_404(Language, id=pk)
    except Http404:
        logger.error(f"Language with id={pk} not found for update")
        raise
    serializer = LanguageSerializer(instance=language, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# delete language
@api_view(['DELETE'])
def deleteLanguage(request, pk):
    try:
        language = get_object_or_404(Language, id=pk)
    except Http404:
        logger.error(f"Language with id={pk} not found for deletion")
        raise
    language.delete()
    return Response('Item successfully deleted')
