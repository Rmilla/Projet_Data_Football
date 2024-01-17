import pandas as pd
from django.core.management.base import BaseCommand
from django_app_foot.models import PlayersValuation, Club
from tqdm import tqdm
from datetime import datetime


import pytz


class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        data = pd.read_csv(
            'django_app_foot/management/csv/player_valuations.csv', encoding="utf8")
        data = data.dropna(subset=['current_club_id'])
        instances_to_create = []
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            naive_datetime_str = row['datetime']
            naive_datetime = datetime.strptime(
                naive_datetime_str, '%Y-%m-%d %H:%M:%S')
            aware_datetime = pytz.UTC.localize(naive_datetime)
            mon_modele_instance = PlayersValuation(
                player_id=row['player_id'],
                date=row['date'],
                datetime=aware_datetime,
                dateweek=row['dateweek'],
                market_value_in_eur=row['market_value_in_eur'],
                current_clubs_id=row['current_club_id'],
                player_club_domestic_competition_id=row['player_club_domestic_competition_id'],
                # ... other fields
            )
            instances_to_create.append(mon_modele_instance)
        PlayersValuation.objects.bulk_create(instances_to_create)
        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))
