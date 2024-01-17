from rest_framework import serializers, viewsets, permissions, status
from models import Game
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = {
            "game_id": ['exact'],
            "season": ['exact'],
            "round": ['exact'],
            "date": ['exact'],
            "home_club_goals": ['exact'],
            "away_club_goals": ['exact'],
            "home_club_position": ['exact'],
            "competition": ['exact'],
            "home_club_id": ['exact'],
            "away_club_id": ['exact'],
        }

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backend = [DjangoFilterBackend]
    #filterset_class = GameFilters