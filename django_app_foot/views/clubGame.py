from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import ClubGame
from ..pagination import MyPaginationClass
from django.http import JsonResponse
import json


class ClubGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubGame
        fields = "__all__"
        # Empeche les erreur avec NaN

        def to_representation(self, instance):
            data = super().to_representation(instance)

            for key, value in data.items():
                if value != value:
                    data[key] = None
            return data


class ClubGameFilters(filters.FilterSet):
    class Meta:
        model = ClubGame
        fields = {
            'game': ['exact'],
            'club': ['exact'],
            'own_goals': ['exact'],
            'own_position': ['icontains', 'contains', 'exact'],
            'own_manager_name': ['exact', 'icontains', 'contains'],
            'opponent_goals': ['exact'],
            'opponent_position': ['icontains', 'contains', 'exact'],
            'opponent_manager_name': ['exact'],
            'hosting': ['exact']
        }


class ClubGameViewSet(viewsets.ModelViewSet):

    queryset = ClubGame.objects.all()
    serializer_class = ClubGameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = MyPaginationClass
    filterset_class = ClubGameFilters
    # Convertion des données en json

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return JsonResponse(response.data, safe=False, json_dumps_params={'indent': 2})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=500)
