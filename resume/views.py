from django.shortcuts import render
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .utils import *
# Create your views here.

@api_view(['POST'])
def RegisterUser(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateResume(request):
    serializer = ResumeSerialzier(data = request.data)
    if serializer.is_valid():
        text_data = extract_text_from_pdf(serializer.validated_data.get('resume_file'))
        serializer.validated_data['extracted_text'] = text_data
        serializer.validated_data['user'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    