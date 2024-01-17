import pandas as pd
from django.core.management.base import BaseCommand
# Assurez-vous d'importer le modèle Player
from django_app_foot.models import GameEvent, Player
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas

        data = pd.read_csv(
            'django_app_foot/management/csv/game_events.csv', encoding="utf8")
        print(data.isnull().sum())
        data.fillna(0, inplace=True)

        instances_to_create = []

        missing_player_ids_count = 0

        # Iterer sur les lignes du dataframe
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            if Player.objects.filter(player_id=row['player_id']).exists():
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
            else:
                print(
                    f"player_id {row['player_id']} n'existe pas dans la table Player.")
                missing_player_ids_count += 1
        GameEvent.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.WARNING(
            f'Nombre de player_id manquants : {missing_player_ids_count}'))

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))
