from rest_framework import serializers, viewsets, permissions, status
from django_app_foot.models import Game
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from ..pagination import MyPaginationClass
from .appearance import AppearancesSerializer



class GameSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Game
        fields =['date','season']
class GameFilter(filters.FilterSet):
    class Meta:
        model = Game
        fields = {
            "game_id": ['icontains','exact'],
            "season": ['icontains','exact'],
            "round": ['icontains','exact'],
            "date": ['exact'],
            "competition": ['exact'],
        }
class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = GameFilter
    pagination_class = MyPaginationClass
