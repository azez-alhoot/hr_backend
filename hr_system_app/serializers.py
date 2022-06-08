from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class CandidatesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'full_name', 'date_of_birth', 'years_of_experience', 'department']

