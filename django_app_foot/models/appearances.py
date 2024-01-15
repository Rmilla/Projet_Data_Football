from django.db import models

class Appearance(models.Model): 
    appearance_id = models.CharField(primary_key=True,max_length=100)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='appearences')
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='appearances')
    player_club_id = models.IntegerField()
    player_current_club_id = models.IntegerField()
    date = models.DateField()
    player_name = models.CharField(max_length=100)
    competition_id = models.CharField(max_length=100)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)