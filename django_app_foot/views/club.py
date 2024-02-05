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
        
    def to_representation(self, instance):
            data = super().to_representation(instance)

            for key, value in data.items():
                if value != value:
                    data[key] = None
            return data

class ClubFilters(filters.FilterSet):
    # min_date = filters.DateFilter(field_name='clubGames__game__date', lookup_expr='gte')
    # max_date = filters.DateFilter(field_name='clubGames__game__date', lookup_expr='lte')
    # season = filters.NumberFilter(field_name = 'clubGames__game__season')
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
    queryset = Club.objects.all()
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
        
    