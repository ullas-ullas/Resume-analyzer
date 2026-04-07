from django.urls import path
from .views import *

urlpatterns = [
    path("api/register/", RegisterUser),
    path("resume/", CreateResume),
    path("resume/<int:pk>/", fetchCleanedData),
]