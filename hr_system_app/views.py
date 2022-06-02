from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Candidate
from .serializers import CandidateSerializer, CandidatesListSerializer


class CreateCandidate(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()


class CandidatesList(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Candidate.objects.all().order_by('-registration_date')
    serializer_class = CandidatesListSerializer
