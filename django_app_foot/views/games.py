from rest_framework import serializers, viewsets, permissions, status
from models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = []

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]
    #filter_backend = [DjangoFilterBackend]
    #filterset_class = GameFilters