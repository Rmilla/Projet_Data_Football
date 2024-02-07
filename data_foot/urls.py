"""
URL configuration for data_foot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django_app_foot.views import(  AppearancesViewSet, ClubGameViewSet, GameEventViewSet,PlayersValuationViewSet,CompetitionViewSet,GameViewSet,ClubViewSet,PlayerViewSet,LastGameViewSet)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'appearances', AppearancesViewSet, basename='appearances')
router.register(r'club_games', ClubGameViewSet, basename='club_game')
router.register(r'competitions', CompetitionViewSet, basename='competition')
router.register(r'games', GameViewSet, basename='game')
router.register(r'player_valuations', PlayersValuationViewSet, basename='player_valuation')
router.register(r'game_events', GameEventViewSet, basename='game_event')
router.register(r'clubs', ClubViewSet, basename='club')
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'last_game', LastGameViewSet, basename='last_game')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the router's URLs
    path('', include(router.urls)),
]   
