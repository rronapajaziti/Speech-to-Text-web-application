import logging
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Transcription
from ..serializers import TranscriptionSerializer

logger = logging.getLogger(__name__)


# get all transcriptions
@api_view(['GET'])
def getTranscriptions(request):
    transcriptions = Transcription.objects.all()
    serializer = TranscriptionSerializer(transcriptions, many=True)
    return Response(serializer.data)


# get single transcription
@api_view(['GET'])
def getTranscription(request, pk):
    try:
        transcription = get_object_or_404(Transcription, id=pk)
    except Http404:
        logger.error(f"Transcription with id={pk} not found")
        raise
    serializer = TranscriptionSerializer(transcription, many=False)
    return Response(serializer.data)


# add transcription
@api_view(['POST'])
def addTranscription(request):
    serializer = TranscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# update transcription
@api_view(['PUT'])
def updateTranscription(request, pk):
    try:
        transcription = get_object_or_404(Transcription, id=pk)
    except Http404:
        logger.error(f"Transcription with id={pk} not found for update")
        raise
    serializer = TranscriptionSerializer(instance=transcription, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# delete transcription
@api_view(['DELETE'])
def deleteTranscription(request, pk):
    try:
        transcription = get_object_or_404(Transcription, id=pk)
    except Http404:
        logger.error(f"Transcription with id={pk} not found for deletion")
        raise
    transcription.delete()
    return Response('Item successfully deleted')
