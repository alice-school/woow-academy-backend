from django.urls import path
from . import views

# URLConf
urlpatterns = [
    # create new user
    path('create', views.createUser),
    #check if user exists
    path('check', views.checkValidUser),
    # view user profile by id
    path('profile/<id>', views.getUserProfile),
    # view all users
    path('all', views.viewAllUsers),
    # update user profile
    path('update', views.updateUser),
    # delete user profile
    path('delete/<id>', views.deleteUser),
    # update student points
    path('points/<id>/<points>', views.updateStudentPoints),
    # create cv profile
    path('cv/create', views.createStudentCVProfile),
    # view student cv profile by student id
    path('cv/<id>', views.getStudentCVProfile),
    # view all student cv profiles
    path('cvProfile/all', views.getAllStudentCVProfiles),
    # view all addresses
    path('address/all', views.getAllAddresses),
    #  view address by student id
    path('address/<id>', views.getAddressByUserID),
    
    # view social media by student id
    path('socialMedia/<id>', views.getAllSocialMediaLinks),
    
    # view LinkedIn by student linkedin id
    path('linkedin-data/', views.get_linkedin_data),
    
    # create fully detailed cv profile
    path('cv/create/full', views.createStudentResumeProfile),
]