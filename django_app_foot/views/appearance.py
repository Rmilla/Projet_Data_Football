from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import Appearance
from ..pagination import MyPaginationClass


class AppearancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance
        fields = ['goals','date']


class AppearancesFilters(filters.FilterSet):
    class Meta:
        model = Appearance
        fields = {
            'date': ['exact'],
            'player_name': ['exact', 'icontains', 'contains'],
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
