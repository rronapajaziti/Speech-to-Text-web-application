import logging
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import AudioFiles
from ..serializers import AudioFilesSerializer

logger = logging.getLogger(__name__)


# get all audio files
@api_view(['GET'])
def getAudioFiles(request):
    audio_files = AudioFiles.objects.all()
    serializer = AudioFilesSerializer(audio_files, many=True)
    return Response(serializer.data)


# get single audio file
@api_view(['GET'])
def getAudioFile(request, pk):
    try:
        audio_file = get_object_or_404(AudioFiles, id=pk)
    except Http404:
        logger.error(f"AudioFile with id={pk} not found")
        raise
    serializer = AudioFilesSerializer(audio_file, many=False)
    return Response(serializer.data)


# add audio file
@api_view(['POST'])
def addAudioFile(request):
    serializer = AudioFilesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# update audio file
@api_view(['PUT'])
def updateAudioFile(request, pk):
    try:
        audio_file = get_object_or_404(AudioFiles, id=pk)
    except Http404:
        logger.error(f"AudioFile with id={pk} not found for update")
        raise
    serializer = AudioFilesSerializer(instance=audio_file, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# delete audio file
@api_view(['DELETE'])
def deleteAudioFile(request, pk):
    try:
        audio_file = get_object_or_404(AudioFiles, id=pk)
    except Http404:
        logger.error(f"AudioFile with id={pk} not found for deletion")
        raise
    audio_file.delete()
    return Response('Item successfully deleted')
