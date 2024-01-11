from django.db import models

class Appearances(models.Model): 
    #game_id
    #player_id
    #player_club_id
    date = models.DateField
    #player_current_club_id
    player_name = models.CharField(max_length=100)
    competition_id = models.CharField(max_length=100)
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

