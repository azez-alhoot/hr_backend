from django.urls import path
from .views import CreateCandidate, CandidatesList, DownloadCandidateResume

urlpatterns = [
    path('create/candidate/', CreateCandidate.as_view(), name='create-candidate'),
    path('candidates/list', CandidatesList.as_view(), name='candidate-list'),
    path('download/resume/<int:id>/', DownloadCandidateResume.as_view(), name='download-resume')
]