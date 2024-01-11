from django.db import models


class Competition(models.Model):
    
    competition_id = models.CharField(primary_key=True)
    competition_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    country_id = models.IntegerField( default=0)
    