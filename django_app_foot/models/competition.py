from django.db import models

class Competition(models.Model):
    competition_id = models.CharField(primary_key=True,max_length=100)
    CONFEDERATION = [
        ("EU", "europa")
    ]
    competition_code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sub_type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    domestic_league_code = models.CharField(max_length=100)
    confederation = models.CharField(choices=CONFEDERATION,max_length=100)
    url = models.URLField()
    country_id = models.IntegerField()