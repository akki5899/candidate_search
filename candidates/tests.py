from django.test import TestCase
from .models import Candidate
from .utils import search_candidates

class CandidateSearchTestCase(TestCase):
    def setUp(self):
        Candidate.objects.create(name="Ajay Kumar Yadav")
        Candidate.objects.create(name="Ajay Kumar Sharma")
        Candidate.objects.create(name="Kumar Sharma Yadav")
        Candidate.objects.create(name="Ajay Singh")
        Candidate.objects.create(name="Rajesh Yadav")

    def test_search_candidates(self):
        query = "Ajay Kumar Yadav"
        results = search_candidates(query)
        result_names = [candidate.name for candidate in results]
        expected_names = ["Ajay Kumar Yadav", "Ajay Kumar Sharma", "Kumar Sharma Yadav", "Ajay Singh", "Rajesh Yadav"]
        self.assertEqual(result_names, expected_names)
