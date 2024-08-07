from django.urls import path
from .views import CandidateSearchView

# URL patterns for the candidates app
urlpatterns = [
    path('search/', CandidateSearchView.as_view(), name='candidate-search'),
]