from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Candidate
from .serializers import CandidateSerializer
from .utils import search_candidates

# View to handle candidate search
class CandidateSearchView(APIView):
    def get(self, request, format=None):
        query = request.query_params.get('query', None)
        if query:
            candidates = search_candidates(query)
            serializer = CandidateSerializer(candidates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)