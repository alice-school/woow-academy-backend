# resume_classifier/urls.py
from django.urls import path
from .views import predict_industry

urlpatterns = [
    path('predict-industry/', predict_industry, name='predict_industry'),
]
