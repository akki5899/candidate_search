from django.contrib import admin
from .models import Candidate

# Register the Candidate model with the admin site
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
