from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import GameEvent
from ..pagination import MyPaginationClass
from .games import GameSerializer

class GameEventSerializer(serializers.ModelSerializer):
    games = GameSerializer(many = True, read_only = True)
    class Meta:
        model = GameEvent
        fields = [ "games"]


class GameEventFilters(filters.FilterSet):
    class Meta:
        model = GameEvent
        fields = {
            'date': ['exact'],
            'game': ['exact'],
            'minute': ['exact'],
            'type': ['exact'],
            'club_id': ['exact'],
            'description': ['exact'],
            'player_in_id': ['exact'],
            'player_assist_id': ['exact'],
        }
        


class GameEventViewSet(viewsets.ModelViewSet):
    queryset = GameEvent.objects.all()
    serializer_class = GameEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = MyPaginationClass
    filterset_class = GameEventFilters
    