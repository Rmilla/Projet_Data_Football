import csv
from tqdm import tqdm
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django_app_foot.models import player

class Command(BaseCommand):
    help = 'Import player data from CSV file'

    def handle(self, *args, **options):
        with open('django_app_foot/management/csv/players.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            players = []
            for row in tqdm(reader, desc="Importing player data", unit=" rows"):

                player_instance = player.Player(
                    player_id=row['player_id'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    name=row['name'],
                    last_season=row['last_season'],
                    current_club_id=row['current_club_id'],
                    player_code=row['player_code'],
                    country_of_birth=row['country_of_birth'],
                    city_of_birth=row['city_of_birth'],
                    country_of_citizenship=row['country_of_citizenship'],
                    date_of_birth=row['date_of_birth'],
                    sub_position=row['sub_position'],
                    position=row['position'],
                    foot=row['foot'],
                    height_in_cm=row['height_in_cm'],
                    contract_expiration_date=row['contract_expiration_date'],
                    agent_name=row['agent_name'],
                    image_url=row['image_url'],
                    url=row['url'],
                    current_club_name=row['current_club_name'],
                    market_value_in_eur=row['market_value_in_eur'],
                    highest_market_value_in_eur=row['highest_market_value_in_eur']
                )
                players.append(player_instance)

        with transaction.atomic():
            player.Player.objects.bulk_create(players)

        self.stdout.write(self.style.SUCCESS('Player data imported successfully.'))
