from django.urls import path
from .views import CreateCandidate

urlpatterns = [
    path('create/candidate/', CreateCandidate.as_view(), name='create-candidate'),
]