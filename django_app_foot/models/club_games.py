from django.db import models

class Club_games(models.Model):
    #game_id
    #club_id
    own_goals = models.IntegerField()
    own_position = models.IntegerField()
    own_manager_name = models.CharField()
    #opponent_id
    opponent_goals = models.IntegerField()
    opponent_position = models.IntegerField()
    opponent_manager_name = models.CharField(max_length=100)
    hosting = models.CharField(max_length=100)
