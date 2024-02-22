from django.core.validators import MinValueValidator
from django.db import models
class Student(models.Model):
    userID = models.CharField(max_length=50, primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    dob = models.DateField()
    userPassword = models.CharField(max_length=255)
    
class Address(models.Model):
    addressID = models.CharField(max_length=50, primary_key=True)
    userID = models.ForeignKey(Student, on_delete=models.CASCADE)
    lineOne = models.CharField(max_length=255)
    lineTwo = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postCode = models.CharField(max_length=255)
    
class Recruiter(models.Model):
    userID = models.CharField(max_length=50, primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    profile_img = models.TextField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    userPassword = models.CharField(max_length=255)
    
class CV_Profile(models.Model):
    cvID = models.CharField(max_length=50, primary_key=True)
    userID = models.ForeignKey(Student, on_delete=models.CASCADE)
    profile_img = models.TextField()
    about = models.TextField()
    points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
class Objective(models.Model):
    objectiveID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE)
    objective_description = models.TextField()

class Education(models.Model):
    educationID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    education_course = models.CharField(max_length=255)
    education_start_date = models.DateField()
    education_end_date = models.DateField()

class Skill(models.Model):
    skillID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    skill_level = models.CharField(max_length=255)
    
class SocialMedia(models.Model):
    socialMediaID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE)
    socialMedia_name = models.CharField(max_length=255)
    socialMedia_link = models.CharField(max_length=255)
    
class WorkExperience(models.Model):
    workExperienceID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    job_description = models.TextField()
    job_address = models.CharField(max_length=255)
    
class VolunteerExperience(models.Model):
    volunteerExperienceID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    volunteer_start_date = models.DateField()
    volunteer_end_date = models.DateField()
    volunteer_description = models.TextField()
    
class Project(models.Model):
    projectID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    

