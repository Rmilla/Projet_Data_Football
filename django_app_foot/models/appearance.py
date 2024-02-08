from django.db import models


class Appearance(models.Model):
    appearance_id = models.CharField(primary_key=True, max_length=100)
    game = models.ForeignKey(
        'Game', on_delete=models.CASCADE, related_name='appearences')
    player = models.ForeignKey(
        'Player', on_delete=models.CASCADE, related_name='appearances', null=True)
    player_club_id = models.IntegerField()
    fk_player_club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='old_players', null=True)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.appearance_id}'
