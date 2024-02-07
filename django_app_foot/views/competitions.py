from rest_framework import serializers, viewsets, permissions
from django_app_foot.models import Competition, Club
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from ..pagination import MyPaginationClass
from .club import ClubSerializer, ClubFilters
from .games import GameSerializer

class CompetitionSerializer(serializers.ModelSerializer):
    clubs = serializers.SerializerMethodField()

    def get_clubs(self, obj):
        request = self.context.get('request')
        filtered_clubs = ClubFilters(request.GET, queryset=obj.clubs.all()).qs
        return ClubSerializer(filtered_clubs, many=True).data

    class Meta:
        model = Competition
        fields = "__all__"

class CompetitionFilter(filters.FilterSet):
  
    class Meta:
        model = Competition
        fields = {
            "competition_id": ['icontains', 'contains', 'exact'],
            "competition_code": ['icontains', 'contains', 'exact'],
            "name": ['icontains', 'contains', 'exact'],
            "type": ['icontains', 'contains', 'exact'],
            "country_name": ['icontains', 'contains'],
            "domestic_league_code": ['icontains', 'contains'],
            "confederation": ['icontains', 'contains'],
        }

    def filter_last_season(self, queryset, name, value):
        return queryset.filter(clubs__last_season=value).distinct()

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.filter(clubs__gt=0)
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompetitionFilter

    def get_serializer_context(self):
        context = super(CompetitionViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
