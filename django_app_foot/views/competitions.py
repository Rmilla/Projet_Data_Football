from rest_framework import serializers, viewsets, permissions, status
from django_app_foot.models import Competition
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from ..pagination import MyPaginationClass
from .club import ClubSerializer
from .games import GameSerializer

class CompetitionSerializer(serializers.ModelSerializer):
    clubs = ClubSerializer(many=True, read_only=True)
   
    class Meta: 

        model = Competition
        fields = "__all__"

class CompetitionFilter(filters.FilterSet):
 
    class Meta:
        model = Competition
        fields = {
            "competition_id": ['icontains', 'contains','exact'],
            "competition_code": ['icontains', 'contains','exact'],
            "name": ['icontains', 'contains','exact'],
            "type": ['icontains', 'contains','exact'],
            "country_name": ['icontains', 'contains'],
            "domestic_league_code": ['icontains', 'contains'],
            "confederation": ['icontains', 'contains'],
        }
class CompetitionViewSet(viewsets.ModelViewSet):
  
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = MyPaginationClass
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompetitionFilter 