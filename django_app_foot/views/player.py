from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import Player
from ..pagination import MyPaginationClass
from django.http import JsonResponse

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"

        def to_representation(self, instance):
            data = super().to_representation(instance)

            for key, value in data.items():
                if value != value:
                    data[key] = None
            return data

class PlayerFilters(filters.FilterSet):
    class Meta:
        model = Player
        fields = {
            'player_id': ['exact'],
            'first_name': ['exact', 'icontains', 'contains'],
            'last_name': ['exact', 'icontains', 'contains'],
            'name': ['exact', 'icontains', 'contains'],
            'last_season': ['exact'],
            'current_club_id': ['exact'],
            'player_code': ['exact', 'icontains', 'contains'],
            'country_of_birth': ['exact', 'icontains', 'contains'],
            'city_of_birth': ['exact', 'icontains', 'contains'],
            'country_of_citizenship': ['exact', 'icontains', 'contains'],
            'date_of_birth': ['exact'],
            'sub_position': ['exact', 'icontains', 'contains'],
            'position': ['exact', 'icontains', 'contains'],
            'foot': ['exact', 'icontains', 'contains'],
            'height_in_cm': ['exact'],
            'contract_expiration_date': ['exact'],
            'agent_name': ['exact', 'icontains', 'contains'],
            'image_url': ['exact', 'icontains', 'contains'],
            'url': ['exact', 'icontains', 'contains'],
            'current_club_name': ['exact', 'icontains', 'contains'],
            'market_value_in_eur': ['exact'],
            'highest_market_value_in_eur': ['exact'],
        }

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlayerFilters
    pagination_class = MyPaginationClass

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return JsonResponse(response.data, safe=False, json_dumps_params={'indent': 2})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=500)
