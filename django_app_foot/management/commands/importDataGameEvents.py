import pandas as pd
from django.core.management.base import BaseCommand
from django_app_foot.models import GameEvent
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('django_app_foot\management\csv\game_events.csv', encoding="utf8")
        
        instances_to_create = []
        # Iterer sur les lignes du dataframe et enregistrer dans la base de données
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            mon_modele_instance = GameEvent(
                date=row['date'],
                game_id=row['game_id'],
                minute=row['minute'],
                type=row['type'],
                club_id=row['club_id'],
                player_id=row['player_id'],
                description=row['description'],
                player_in_id=row['player_in_id'],
                player_assist_id=row['player_assist_id'],
                
                # ... assignez d'autres champs comme requis
                
            )
            instances_to_create.append(mon_modele_instance)
        GameEvent.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))
