from django.db import models

class Competition(models.Model):
    competition_id = models.CharField(primary_key=True)
    CONFEDERATION = [
        ("EU", "europa")
    ]
    competition_code = models.CharField(max_length=5)
    name = models.CharField()
    sub_type = models.CharField()
    type = models.CharField()
    country_name = models.CharField()
    domestic_league_code = models.CharField()
    confederation = models.CharField(choices=CONFEDERATION)
    url = models.URLField()
    country_id = models.IntegerField()