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
from django.urls import path

from django_app_foot.views import AppearancesViewSet, ClubGameViewSet, GameEventViewSet,PlayersValuationViewSet,CompetitionViewSet,GameViewSet,ClubViewSet,PlayerViewSet



urlpatterns = [
    path('admin/', admin.site.urls),
    path('appearances/', AppearancesViewSet .as_view({'get': 'list'})),
    path('club_games/', ClubGameViewSet.as_view({'get': 'list'})),

    path('competitions/', CompetitionViewSet.as_view({'get': 'list'})),
    path('games/', GameViewSet.as_view({'get': 'list'})),


    path('player_valuations/', PlayersValuationViewSet.as_view({'get': 'list'})),
    path('game_events/', GameEventViewSet.as_view({'get': 'list'})),
    path('clubs/', ClubViewSet.as_view({'get': 'list'})),
    path('players/', PlayerViewSet.as_view({'get': 'list'}))

]
