from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ResumeModel(models.Model):
    resume_file = models.FileField(upload_to="resume/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extracted_text = models.TextField(blank = True)
    cleaned_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class JobDescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True)
    company = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE)
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)

    match_score = models.FloatField()
    matched_skills = models.JSONField()
    missing_skills = models.JSONField()
    suggestions = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)