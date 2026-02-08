from rest_framework import serializers
from .models import User, Roles, Language, AudioFiles, Transcription, EvaluationResults


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class AudioFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFiles
        fields = "__all__"


class TranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcription
        fields = "__all__"


class EvaluationResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationResults
        fields = "__all__"