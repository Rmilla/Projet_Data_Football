import pandas as pd
from django.core.management.base import BaseCommand
from django_app_foot.models import PlayersValuation
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('django_app_foot\management\csv\player_valuations.csv', encoding="utf8")
        
        instances_to_create = []
        # Iterer sur les lignes du dataframe et enregistrer dans la base de données
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            mon_modele_instance = PlayersValuation(
                date=row['date'],
                datetime=row['datetime'],
                dateweek=row['dateweek'],
                market_value_in_eur=row['market_value_in_eur'],
                current_clubs_id=row['current_club_id'],
                player_club_domestic_competition_id=row['player_club_domestic_competition_id'],
                # ... assignez d'autres champs comme requis
    
            )
            instances_to_create.append(mon_modele_instance)
        PlayersValuation.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))
