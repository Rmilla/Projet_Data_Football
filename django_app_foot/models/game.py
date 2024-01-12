from django.db import models

class Game(models.Model):
    game_id = models.IntegerField(PrimaryKey=True)
    season = models.IntegerField()
    round = models.CharField()
    date = models.DateField()
    home_club_goals = models.IntegerField()
    away_club_goals = models.IntegerField()
    home_club_position = models.IntegerField()
    competition_id = models.ForeignKey("Competition", on_delete=models.CASCADE, related_name='competitions')
    home_club_id = models.ForeignKey("Club", on_delete=models.CASCADE, related_name='homeClubs')
    away_club_id = models.ForeignKey("Club", on_delete=models.CASCADE, related_name='awayClubs')
