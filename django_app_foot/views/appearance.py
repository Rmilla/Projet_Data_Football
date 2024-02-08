from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import Appearance
from ..pagination import MyPaginationClass



class AppearancesSerializer(serializers.ModelSerializer):
    game_date = serializers.DateField(source='game.date')
    class Meta:
        model = Appearance
        fields = ['player_club_id','goals', 'game_date']

class AppearancesFilters(filters.FilterSet):
    current_club_id = filters.NumberFilter(field_name='player_club_id', lookup_expr='exact')
    min_date = filters.DateFilter(field_name='game__date', lookup_expr='gte')
    max_date = filters.DateFilter(field_name='game__date', lookup_expr='lte')
    class Meta:
        model = Appearance
        fields = {
            'game__date': ['gte', 'lte', 'exact'],
            'yellow_cards': ['exact'],
            'red_cards': ['exact'],
            'goals': ['exact'],
            'assists': ['exact'],
            'minutes_played': ['exact'],
        }

class AppearancesViewSet(viewsets.ModelViewSet):
    queryset = Appearance.objects.all()
    serializer_class = AppearancesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = MyPaginationClass
    filterset_class = AppearancesFilters
