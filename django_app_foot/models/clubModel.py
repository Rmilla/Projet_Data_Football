from django.db import models
from django.db.models import Model, Manager, QuerySet

class Club(models.Model):
    
    club_id = models.IntegerField(primary_key=True)
    club_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    #domestic_competition = models.CharField(max_length=255) #foreignKey 
    squad_size = models.IntegerField() 
    average_age = models.FloatField() 
    foreigner_percentage = models.FloatField()
    national_teams_players = models.IntegerField() 
    stadium_name = models.CharField(max_length=255)
    stadium_seats= models.IntegerField()
    net_transfer_record= models.IntegerField()
    last_season= models.IntegerField()
    url= models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'
