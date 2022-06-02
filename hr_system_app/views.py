from wsgiref.util import FileWrapper
from django.http import HttpResponse
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


class DownloadCandidateResume(ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id, format=None):
        queryset = Candidate.objects.get(id=id)
        resume = queryset.resume.path
        document = open(resume, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/msword')
        response['Content-Disposition'] = 'filename="%s"' % queryset.resume.name
        return response