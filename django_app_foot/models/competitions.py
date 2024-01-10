from django.db import models

class Competition(models.Model):
    CONFEDERATION = [
        ("EU", "europa")
    ]
    competition_code = models.CharField()
    name = models.CharField()
    sub_type = models.CharField()
    type = models.CharField()
    country_name = models.CharField()
    domestic_league_code = models.CharField()
    confederation = models.CharField(choices=CONFEDERATION)
    url = models.CharField()
    country_id = models.ForeignKey(COUNTRY, on_delete=models.CASCADE, related_name='competition')
