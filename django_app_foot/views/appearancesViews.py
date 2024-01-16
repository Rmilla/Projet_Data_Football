from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from django_filters import rest_framework as filters
from ..models import Appearance


class AppearancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance
        fields = "__all__"


'''
class AppearancesFilters(filters.FilterSet):
    class Meta:
        model = Appearance
        fields = {
        }
'''


class AppearancesViewSet(viewsets.ModelViewSet):
    queryset = Appearance.objects.all()
    serializer_class = AppearancesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    # filterset_class = AppearancesFilters
