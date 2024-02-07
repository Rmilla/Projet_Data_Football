from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import Club, ClubGame, Player
from ..pagination import MyPaginationClass
from django.http import JsonResponse
from rest_framework.decorators import action
from .player import PlayerSerializer
from rest_framework.response import Response
class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = ['club_id','name','last_season']
        

class ClubFilters(filters.FilterSet):

    class Meta:
        model = Club
        fields = {
            'club_id': ['exact'],
            'club_code': ['exact', 'icontains', 'contains'],
            'name': ['exact', 'icontains', 'contains'],
            'squad_size': ['exact'],
            'average_age': ['exact'],
            'stadium_name': ['exact', 'icontains', 'contains'],
            'stadium_seats': ['exact'],
            'net_transfer_record': ['exact', 'icontains', 'contains'],
            'last_season': ['exact'],
            'url': ['exact', 'icontains', 'contains'],
            'foreigners_number': ['exact'],
            'foreigners_percentage': ['exact'],
            'national_team_players': ['exact'],
            'coach_name': ['exact', 'icontains', 'contains'],
        }

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClubFilters

    def list(self, request, *args, **kwargs):
        try:
          
            response = super().list(request, *args, **kwargs)
            return JsonResponse(response.data, safe=False, json_dumps_params={'indent': 2})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=500)
        
   
    @action(detail=True, methods=['get'])
    def get_players_with_appearances(self, request, pk=None):
        try:
            club = self.get_object()
            players = Player.objects.filter(appearances__player_club_id=club.club_id)
            player_serializer = PlayerSerializer(players, many=True)
            return Response(player_serializer.data)
        except Player.DoesNotExist:
            return Response({"error": "Aucun joueur avec des apparitions associées à ce club."}, status=404)
        except Exception as e:
            # Ajout d'impressions pour voir les détails dans la console du serveur
            print(f"Erreur dans l'action get_players_with_appearances : {e}")
            import traceback
            print(traceback.format_exc())
            return Response({"error": str(e)}, status=500)