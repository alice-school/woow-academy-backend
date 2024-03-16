import requests
from django.shortcuts import get_list_or_404,get_object_or_404
from django.shortcuts import render
from common.serializers import StudentSerializer, AddressSerializer, RecruiterSerializer, CV_ProfileSerializer, ObjectiveSerializer, EducationSerializer, SkillSerializer, SocialMediaSerializer, WorkExperienceSerializer, VolunteerExperienceSerializer, ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Address, Recruiter, CV_Profile, Objective, Education, Skill, SocialMedia, WorkExperience, VolunteerExperience, Project
# create new user
@api_view(['POST'])
def createUser(request):
    
    data = request.data.copy()
    
    print(data)
    
    
    # dob birth is mysql date format, so if dob is empty, set it to 2006 january 1st
    if data['dob'] == '':
        data['dob'] = '2006-01-01'
        
    serializer = StudentSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        resposeData = {
            'data': serializer.data,
            'message': "User created successfully",
            'status': status.HTTP_201_CREATED
        }
        print(resposeData)
        return Response(resposeData, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update user profile by id
@api_view(['PUT'])
def updateUser(request, id):
    try:
        user = Student.objects.get(userID=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = request.data.copy()
    serializer = StudentSerializer(user, data=data)
    
    if serializer.is_valid():
        serializer.save()
        responseData = {
            'data': serializer.data,
            'message': 'User updated successfully',
            'status': status.HTTP_200_OK
        }
        
        return Response(responseData, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete user by id
def deleteUser(request, id):
    try:
        user = Student.objects.get(userID=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# check valid user
@api_view(['POST'])
def checkValidUser(request):
    data = request.data.copy()
    email = data['email']
    userPassword = data['userPassword']
    
    # check if email and password are empty
    if email == '' or userPassword == '':
        responseData = {
            'message': 'Email and password cannot be empty',
            'status': status.HTTP_400_BAD_REQUEST
        }
        return Response(responseData, status=status.HTTP_400_BAD_REQUEST)
    
    # check if user exists
    user = Student.objects.filter(email=email, userPassword=userPassword)
    
    
    
    # if user exists, return user data
    if user.exists():
        serializer = StudentSerializer(user, many=True)
        
        responseData = {
            'data': serializer.data[0],
            'message': 'User found',
            'status': status.HTTP_200_OK
        }
        
        return Response(responseData, status=status.HTTP_200_OK)
    else:
        responseData = {
            'message': 'User not found',
            'status': status.HTTP_404_NOT_FOUND
        }
        
        return Response(responseData, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def viewAllUsers(request):
    queryset = get_list_or_404(Student)
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)
    
# get user profile details
@api_view(['GET'])
def getUserProfile(request, id):    
    print("getting user profile",id)
    try:
        user = Student.objects.get(userID=id)
        print(user)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def getStudentCVProfile(request, id):
    try:
        cvProfile = CV_Profile.objects.get(userID=id)
    except CV_Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CV_ProfileSerializer(cvProfile)
    return Response(serializer.data)
    
#  update CV_Profile points
@api_view(['PUT'])
def updateStudentPoints(request, id, points):
    try:
        user = Student.objects.get(userID=id)
        cvProfile = CV_Profile.objects.get(userID=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = request.data.copy()
    serializer = CV_ProfileSerializer(cvProfile, data=data)
    
    if serializer.is_valid():
        serializer.save()
        responseData = {
            'data': serializer.data,
            'message': 'User points updated successfully',
            'status': status.HTTP_200_OK
        }
        
        return Response(responseData, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# create cv profile
@api_view(['POST'])
def createStudentCVProfile(request):
    data = request.data.copy()
    # update dob in student table
    userID = data['userID']
    dob = data['dob']
    try:
        user = Student.objects.get(userID=userID)
        user.dob = dob
        user.save()
        
        user_serializer = StudentSerializer(user)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # insert address details
    addressID = data['addressID']
    userID = data['userID']
    lineOne = data['lineOne']
    lineTwo = data['lineTwo']
    city = data['city']
    postCode = data['postCode']
    

    # insert address details
    addressSerializer = AddressSerializer(data=data)
    if addressSerializer.is_valid():
        addressSerializer.save()
    else:
        return Response(addressSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # insert cv profile details
    cvProfileSerializer = CV_ProfileSerializer(data=data)
    cvID = data['cvID']
    userID = data['userID']
    profile_img = data['profile_img']
    about = data['about']
    points = data['points']
    gender = data['gender']
    
    print(data)
    
    
    if cvProfileSerializer.is_valid():
        cvProfileSerializer.save()
        responseData = {
            'data': {
                "student": user_serializer.data,
                "address": addressSerializer.data,
                "cvProfile": cvProfileSerializer.data
                },
            'message': 'CV Profile created successfully',
            'status': status.HTTP_201_CREATED
        }
        return Response(responseData, status=status.HTTP_201_CREATED)
    else:
        return Response(cvProfileSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# view all addresses
@api_view(['GET'])
def getAllAddresses(request):
    queryset = get_list_or_404(Address)
    serializer = AddressSerializer(queryset, many=True)
    responseData = {
        'data': serializer.data,
        'status': status.HTTP_200_OK
    }
    return Response(responseData, status=status.HTTP_200_OK)

# view address by user id
@api_view(['GET'])
def getAddressByUserID(request, id):
    try:
        address = Address.objects.get(userID=id)
    except Address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AddressSerializer(address)
    return Response(serializer.data)

# view all student cv profiles
@api_view(['GET'])
def getAllStudentCVProfiles(request):
    print("getting all student cv profiles")
    queryset = get_list_or_404(CV_Profile)
    serializer = CV_ProfileSerializer(queryset, many=True)
    responseData = {
        'data': serializer.data,
        'status': status.HTTP_200_OK
    }
    return Response(responseData, status=status.HTTP_200_OK)

# view all social medial links for a student's cv profile
@api_view(['GET'])
def getAllSocialMediaLinks(request, id):
    try:
        cvProfile = CV_Profile.objects.get(userID=id)
        socialMedia = get_list_or_404(SocialMedia, cvID=cvProfile.cvID)
        serializer = SocialMediaSerializer(socialMedia, many=True)
        responseData = {
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }
        return Response(responseData, status=status.HTTP_200_OK)
    except SocialMedia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def createStudentResumeProfile(request):
    requestData = request.data.copy()
    print(requestData)
    
    try:
        # create cv profile
        cvProfileSerializer = CV_ProfileSerializer(data=requestData['cvProfile'])
        if cvProfileSerializer.is_valid():
            cvProfileSerializer.save()
        else:
            return Response(cvProfileSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # create objective
        objectiveSerializer = ObjectiveSerializer(data=requestData['objective'])
        if objectiveSerializer.is_valid():
            objectiveSerializer.save()
        else:
            return Response(objectiveSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # create education -> eduction is a list of objects so we need to loop through the list and save each object
        educationData = requestData['education']
        for education in educationData:
            educationSerializer = EducationSerializer(data=education)
            if educationSerializer.is_valid():
                educationSerializer.save()
            else:
                return Response(educationSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # create skill -> skill is a list of objects so we need to loop through the list and save each object
        skillData = requestData['skill']
        for skill in skillData:
            skillSerializer = SkillSerializer(data=skill)
            if skillSerializer.is_valid():
                skillSerializer.save()
            else:
                return Response(skillSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        # create social media -> social media is a list of objects so we need to loop through the list and save each object
        socialMediaData = requestData['socialMedia']
        for socialMedia in socialMediaData:
            socialMediaSerializer = SocialMediaSerializer(data=socialMedia)
            if socialMediaSerializer.is_valid():
                socialMediaSerializer.save()
            else:
                return Response(socialMediaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        # create work experience -> work experience is a list of objects so we need to loop through the list and save each object
        workExperienceData = requestData['workExperience']
        for workExperience in workExperienceData:
            workExperienceSerializer = WorkExperienceSerializer(data=workExperience)
            if workExperienceSerializer.is_valid():
                workExperienceSerializer.save()
            else:
                return Response(workExperienceSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        # create volunteer experience -> volunteer experience is a list of objects so we need to loop through the list and save each object
        volunteerExperienceData = requestData['volunteerExperience']
        for volunteerExperience in volunteerExperienceData:
            volunteerExperienceSerializer = VolunteerExperienceSerializer(data=volunteerExperience)
            if volunteerExperienceSerializer.is_valid():
                volunteerExperienceSerializer.save()
            else:
                return Response(volunteerExperienceSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        # create project -> project is a list of objects so we need to loop through the list and save each object
        projectData = requestData['project']
        for project in projectData:
            projectSerializer = ProjectSerializer(data=project)
            if projectSerializer.is_valid():
                projectSerializer.save()
            else:
                return Response(projectSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        responseData = {
            "data": requestData,
            'message': 'Resume profile created successfully',
            'status': status.HTTP_201_CREATED
        }
    
        return Response(responseData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET'])
# def get_linkedin_data(request):
#     url = 'https://nubela.co/proxycurl/api/v2/linkedin'
#     params = {
#         'url': 'https://www.linkedin.com/in/',
#         'skills': 'include',
#     }
#     headers = {
#         'Authorization': 'Bearer Token HeayQqdLjYhPeRs07UEGGA',
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'Access-Control-Allow-Origin': '*',
#         'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
#         'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token',
#         'Access-Control-Allow-Credentials': 'true',
#     }
    
#     try:
#         response = request.get(url, params=params, headers=headers)
#         response.raise_for_status()
#         return Response(response.json(), status=status.HTTP_200_OK)
#     except request.exceptions.RequestException as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_linkedin_data(request):
    
    url = 'https://nubela.co/proxycurl/api/v2/linkedin'

    params = {
        'url': request.GET.get('url'),
        'skills': request.GET.get('skills'),
    }
    
    
    print(params)
    
    headers = {
        'Authorization': 'Bearer 3_gr3ltdWpwEBPn--JU9aw',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token',
        'Access-Control-Allow-Credentials': 'true',
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return Response(response.json(), status=status.HTTP_200_OK)

    except requests.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)