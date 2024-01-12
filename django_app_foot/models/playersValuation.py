from django.db import models


class PlayersValuation(models.Model):
    
    player_id = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='playerValuations')
    date = models.DateField()
    datetime = models.DateTimeField()
    dateweek = models.DateField()
    market_value_in_eur = models.IntegerField()
    current_clubs_id = models.IntegerField()
    player_club_domestic_competition_id = models.CharField(max_length=100)
    