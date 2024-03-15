# resume_classifier/views.py
from django.http import JsonResponse
from common.utils import get_predicted_industry
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def predict_industry(request):
    student_detailsData = request.data.copy()
    predicted_industry = get_predicted_industry(student_detailsData)
    return Response({"predicted_industry": predicted_industry}, status=status.HTTP_201_CREATED)
