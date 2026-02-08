from django.contrib import admin
from .models import Roles, Language, AudioFiles, Transcription, EvaluationResults

# Register your models here.
admin.site.register(Roles)
admin.site.register(Language)
admin.site.register(AudioFiles)
admin.site.register(Transcription)
admin.site.register(EvaluationResults)