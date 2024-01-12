from django.contrib import admin
from django_app_foot.models import club, player

admin.site.register(club.Club)
admin.site.register(player.Player)
