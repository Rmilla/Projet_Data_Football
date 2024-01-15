from django.db import models

class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    round = models.CharField(max_length=100)
    date = models.DateField()
    home_club_goals = models.IntegerField()
    away_club_goals = models.IntegerField()
    home_club_position = models.IntegerField()
    competition = models.ForeignKey("Competition", on_delete=models.CASCADE, related_name='games')
    home_club = models.ForeignKey("Club", on_delete=models.CASCADE, related_name='homeClubs')
    away_club = models.ForeignKey("Club", on_delete=models.CASCADE, related_name='awayClubs')
