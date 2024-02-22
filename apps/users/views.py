from django.shortcuts import get_list_or_404
from django.shortcuts import render
from django.http import HttpResponse
from common.serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Address, Recruiter, CV_Profile, Objective, Education, Skill, SocialMedia, WorkExperience, VolunteerExperience, Project

@api_view(['POST'])
def createUser(request):
    return Response({'name': 'Madhusha'})

def updateUser(request):
    return render(request, 'hello.html', {'name': 'Madhusha'})

def deleteUser(request):
    return render(request, 'hello.html', {'name': 'Madhusha'})

@api_view(['GET'])
def viewUser(request, id):
    return Response( {'name': 'Madhusha ' + id})

@api_view(['GET'])
def viewAllUsers(request):
    queryset = get_list_or_404(Student)
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)
    