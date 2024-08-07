from django.db.models import Q
from .models import Candidate

def search_candidates(query: str):
    query_words = query.strip().lower().split()
    exact_query = query.strip().lower()
    
    # Create a Q object for partial matches
    q_objects = Q()
    for word in query_words:
        q_objects |= Q(name__icontains=word)
    
    # Query for exact matches
    exact_matches = Candidate.objects.filter(name__iexact=exact_query)
    
    # Query for partial matches with annotation for sorting
    partial_matches = Candidate.objects.filter(q_objects).exclude(name__iexact=exact_query)
    
    # Annotate with the number of matching query words
    partial_matches = partial_matches.annotate(
        match_count=Sum(
            Case(
                When(name__icontains=word, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            ) for word in query_words
        )
    ).order_by('-match_count')

    # Combine exact matches with partial matches
    result = list(exact_matches) + list(partial_matches)
    
    return result
