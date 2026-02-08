from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Roles(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.user.username

class Language(models.Model):
    language_name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.language_name} ({self.code})"


class AudioFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=50)
    duration = models.FloatField(help_text="Duration in seconds")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class Transcription(models.Model):
    audio = models.ForeignKey(AudioFiles, on_delete=models.CASCADE)
    raw_text = models.TextField(help_text="Raw transcription output")
    final_text = models.TextField(help_text="Reviewed / corrected transcription", blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("processing", "Processing"),
            ("completed", "Completed"),
            ("failed", "Failed"),
        ],
        default="pending",
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcription {self.id} ({self.status})"


class EvaluationResults(models.Model):
    transcription = models.ForeignKey(Transcription, on_delete=models.CASCADE)
    accuracy_score = models.FloatField()
    error_rate = models.FloatField()
    evaluation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Eval {self.id} – Acc {self.accuracy_score}"
