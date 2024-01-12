from django.db import models

class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    last_season = models.IntegerField()
    current_club_id = models.IntegerField()
    player_code = models.CharField(max_length=255)
    country_of_birth = models.CharField(max_length=255)
    city_of_birth = models.CharField(max_length=255)
    country_of_citizenship = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    sub_position = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    foot = models.CharField(max_length=255)
    height_in_cm = models.CharField(max_length=255)
    contract_expiration_date = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255)
    image_url = models.URLField()
    url = models.URLField()
    current_club_name = models.CharField(max_length=255)
    market_value_in_eur = models.CharField(max_length=255)
    highest_market_value_in_eur = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'