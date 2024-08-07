from rest_framework import serializers
from .models import Candidate

# Serializer for the Candidate model
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name']