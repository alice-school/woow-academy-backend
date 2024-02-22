from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.viewAllUsers),
    path('hello/<id>', views.viewUser)
]