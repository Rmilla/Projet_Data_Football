from django.db import models
from django.db.models import Model, Manager, QuerySet

class Club(models.Model):
    
    club_id = models.IntegerField(primary_key=True)
    club_code = models.CharField(max_length=255)
    competition= models.ForeignKey(
        "Competition", on_delete=models.CASCADE, related_name='clubs', default=1)
    name = models.CharField(max_length=255)
    squad_size = models.IntegerField() 
    average_age = models.CharField(max_length=255) 
    stadium_name = models.CharField(max_length=255)
    stadium_seats= models.IntegerField()
    net_transfer_record= models.CharField(max_length=255)
    last_season= models.IntegerField()
    url= models.CharField(max_length=255)
    foreigners_number = models.IntegerField()
    foreigners_percentage = models.CharField(max_length=255)
    national_team_players = models.IntegerField()
    coach_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'
