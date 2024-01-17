from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import PlayersValuation
from ..pagination import MyPaginationClass


class PlayersValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersValuation
        fields = "__all__"


class PlayersValuationFilters(filters.FilterSet):
    class Meta:
        model = PlayersValuation
        fields = {
            'player': ['exact'],
            'date': ['exact',],
            'datetime': ['exact'],
            'dateweek': ['exact'],
            'market_value_in_eur': ['exact'],
            'current_clubs_id': ['exact'],
            'player_club_domestic_competition_id': ['exact']
        }
        



class PlayersValuationViewSet(viewsets.ModelViewSet):
    queryset = PlayersValuation.objects.all()
    serializer_class = PlayersValuationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = MyPaginationClass
    filterset_class = PlayersValuationFilters