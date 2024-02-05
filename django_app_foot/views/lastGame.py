from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions
from ..pagination import MyPaginationClass
from ..models import club, clubGame

class LastGameSerializer (serializers.ModelSerializer):
    club = serializers.PrimaryKeyRelatedField(queryset = club.Club.objects.all())
    class Meta:
        model = clubGame.ClubGame
        fields = '__all__'
        ordering = ('-date')

class LastGameViewSet(viewsets.ModelViewSet):
    queryset = clubGame.ClubGame.objects.all()
    serializer_class = LastGameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = MyPaginationClass
