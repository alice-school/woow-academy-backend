from django.core.validators import MinValueValidator
from django.db import models
class Student(models.Model):
    userID = models.CharField(max_length=50, primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    dob = models.DateField(default='2006-01-01')
    userPassword = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'Student'
    
class Address(models.Model):
    addressID = models.CharField(max_length=50, primary_key=True)
    userID = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='userID')
    lineOne = models.CharField(max_length=255)
    lineTwo = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postCode = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'Address'
    
class Recruiter(models.Model):
    userID = models.CharField(max_length=50, primary_key=True, db_column='userID')
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    profile_img = models.TextField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    userPassword = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'Recruiter'
    
class CV_Profile(models.Model):
    cvID = models.CharField(max_length=50, primary_key=True)
    userID = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='userID')
    profile_img = models.TextField()
    about = models.CharField(max_length=255, db_column='about', db_collation='utf8mb4_unicode_ci')
    points = models.IntegerField(max_length=255, validators=[MinValueValidator(0)])
    
    class Meta:
        db_table = 'CV_Profile'
    
class Objective(models.Model):
    objectiveID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE, db_column='cvID')
    objective_description = models.TextField()
    
    class Meta:
        db_table = 'Objective'

class Education(models.Model):
    educationID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE, db_column='cvID')
    institution = models.CharField(max_length=255)
    education_course = models.CharField(max_length=255)
    education_start_date = models.DateField()
    education_end_date = models.DateField()
    
    class Meta:
        db_table = 'Education'

class Skill(models.Model):
    skillID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE, db_column='cvID')
    skill_name = models.CharField(max_length=255)
    skill_level = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'Skill'
    
class SocialMedia(models.Model):
    socialMediaID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE, db_column='cvID')
    socialMedia_name = models.CharField(max_length=255)
    socialMedia_link = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'SocialMedia'
    
class WorkExperience(models.Model):
    workExperienceID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE, db_column='cvID')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    job_description = models.TextField()
    job_address = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'WorkExperience'
    
class VolunteerExperience(models.Model):
    volunteerExperienceID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE, db_column='cvID')
    organization_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    volunteer_start_date = models.DateField()
    volunteer_end_date = models.DateField()
    volunteer_description = models.TextField()
    
    class Meta:
        db_table = 'VolunteerExperience'
    
class Project(models.Model):
    projectID = models.CharField(max_length=50, primary_key=True)
    cvID = models.ForeignKey(CV_Profile, on_delete=models.CASCADE, db_column='cvID')
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    
    class Meta:
        db_table = 'Project'
    

