from django.db import models
from models import COMPETITION #HOME_CLUB, AWAY_CLUB

class GAMES(models.Model):
    game_id = models.UUIDField(PrimaryKey=True)
    season = models.IntegerField()
    round = models.CharField()
    date = models.DateField()
    home_club_goals = models.IntegerField()
    away_club_goals = models.IntegerField()
    home_club_position = models.IntegerField()
    competition_id = models.ForeignKey(COMPETITION, on_delete=models.CASCADE, related_name='competition')
    #home_club_id = models.ForeignKey(HOME_CLUB, on_delete=models.CASCADE, related_name='competition')
    #away_club_id = models.ForeignKey(AWAY_CLUB, on_delete=models.CASCADE, related_name='competition')
