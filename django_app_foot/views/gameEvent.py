from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import GameEvent
from ..pagination import MyPaginationClass


class GameEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEvent
        fields = "__all__"


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
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = MyPaginationClass
    filterset_class = GameEventFilters