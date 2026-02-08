from django.contrib import admin
from .models import Roles, User, Language, AudioFiles, Transcription, EvaluationResults

# Register your models here.
admin.site.register(Roles)
admin.site.register(User)
admin.site.register(Language)
admin.site.register(AudioFiles)
admin.site.register(Transcription)
admin.site.register(EvaluationResults)
