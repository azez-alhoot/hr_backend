from django.urls import path
from .views import CreateCandidate, CandidatesList

urlpatterns = [
    path('create/candidate/', CreateCandidate.as_view(), name='create-candidate'),
    path('candidates/list', CandidatesList.as_view(), name='candidate-list'),
]