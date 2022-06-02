from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Candidate
from .serializers import CandidateSerializer


class CreateCandidate(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()