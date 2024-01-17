from django.contrib import admin
from django_app_foot.models import club, player,gameEvent,playersValuation,appearance,clubGame,competition,game

admin.site.register(club.Club)
admin.site.register(player.Player)
admin.site.register(gameEvent.GameEvent)
admin.site.register(playersValuation.PlayersValuation)
admin.site.register(clubGame.ClubGame)
admin.site.register(game.Game)
admin.site.register(appearance.Appearance)
admin.site.register(competition.Competition)