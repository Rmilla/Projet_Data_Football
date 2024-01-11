from django.db import models

class Club_games(models.Model):
    game_id = models.IntegerField()
    club_id = models.IntegerField()
    own_goals = models.IntegerField()
    own_position = models.FloatField(null=True, blank=True)
    own_manager_name = models.CharField(max_length=100)
    opponent_id = models.IntegerField()
    opponent_goals = models.IntegerField()
    opponent_position = models.FloatField(null=True, blank=True)
    opponent_manager_name = models.CharField(max_length=100)
    hosting = models.CharField(max_length=100)

    def __str__(self) :
        return f'{self.game_id}'

    