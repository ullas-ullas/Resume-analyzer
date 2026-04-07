from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ResumeModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'password']

    def create(self, validatd_data):
        user = User.objects.create_user(username = validatd_data['username'] ,
                                  password = validatd_data['password'])
        return user
    
class ResumeSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ResumeModel
        fields = ["id", "resume_file", "extracted_text", "created_at", "cleaned_text"]
        read_only_fields = ["extracted_text", "cleaned_text"]
