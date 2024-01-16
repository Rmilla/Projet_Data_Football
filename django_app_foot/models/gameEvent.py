from django.db import models


class GameEvent(models.Model):

    date = models.DateField()
    game = models.ForeignKey(
        'Game', on_delete=models.CASCADE, related_name='games')
    minute = models.IntegerField()
    type = models.CharField(max_length=100)
    club_id = models.CharField(max_length=100)
    player = models.ForeignKey(
        'Player', on_delete=models.CASCADE, related_name='players', null=True, blank=True)
    description = models.CharField(max_length=100)
    player_in_id = models.IntegerField()
    player_assist_id = models.IntegerField()
