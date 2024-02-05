from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import Club, ClubGame
from .clubGame import ClubGameSerializer
from ..pagination import MyPaginationClass
from django.http import JsonResponse

class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = ['club_id','name','last_season']
        

class ClubFilters(filters.FilterSet):

    class Meta:
        model = Club
        fields = {
            'club_id': ['exact'],
            'club_code': ['exact', 'icontains', 'contains'],
            'name': ['exact', 'icontains', 'contains'],
            'squad_size': ['exact'],
            'average_age': ['exact'],
            'stadium_name': ['exact', 'icontains', 'contains'],
            'stadium_seats': ['exact'],
            'net_transfer_record': ['exact', 'icontains', 'contains'],
            'last_season': ['exact'],
            'url': ['exact', 'icontains', 'contains'],
            'foreigners_number': ['exact'],
            'foreigners_percentage': ['exact'],
            'national_team_players': ['exact'],
            'coach_name': ['exact', 'icontains', 'contains'],
        }

class ClubViewSet(viewsets.ModelViewSet):

    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClubFilters

    def list(self, request, *args, **kwargs):
        try:
          
            response = super().list(request, *args, **kwargs)
            return JsonResponse(response.data, safe=False, json_dumps_params={'indent': 2})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    #on implente la logique de filtrage directement ici
    def get_queryset(self):
        # Filtrez les clubs avec last_season égal à 2023
        return Club.objects.filter(last_season=2023)
    