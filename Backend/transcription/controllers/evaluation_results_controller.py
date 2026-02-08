import logging
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import EvaluationResults
from ..serializers import EvaluationResultsSerializer

logger = logging.getLogger(__name__)


# get all evaluation results
@api_view(['GET'])
def getEvaluationResults(request):
    evaluation_results = EvaluationResults.objects.all()
    serializer = EvaluationResultsSerializer(evaluation_results, many=True)
    return Response(serializer.data)


# get single evaluation result
@api_view(['GET'])
def getEvaluationResult(request, pk):
    try:
        evaluation_result = get_object_or_404(EvaluationResults, id=pk)
    except Http404:
        logger.error(f"EvaluationResult with id={pk} not found")
        raise
    serializer = EvaluationResultsSerializer(evaluation_result, many=False)
    return Response(serializer.data)


# add evaluation result
@api_view(['POST'])
def addEvaluationResult(request):
    serializer = EvaluationResultsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# update evaluation result
@api_view(['PUT'])
def updateEvaluationResult(request, pk):
    try:
        evaluation_result = get_object_or_404(EvaluationResults, id=pk)
    except Http404:
        logger.error(f"EvaluationResult with id={pk} not found for update")
        raise
    serializer = EvaluationResultsSerializer(instance=evaluation_result, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# delete evaluation result
@api_view(['DELETE'])
def deleteEvaluationResult(request, pk):
    try:
        evaluation_result = get_object_or_404(EvaluationResults, id=pk)
    except Http404:
        logger.error(f"EvaluationResult with id={pk} not found for deletion")
        raise
    evaluation_result.delete()
    return Response('Item successfully deleted')
