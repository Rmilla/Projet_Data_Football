import pandas as pd
from django.core.management.base import BaseCommand

from django_app_foot.models import ClubGame, Club

from tqdm import tqdm


class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas

        data = pd.read_csv(
            'django_app_foot/management/csv/club_games.csv', encoding="utf8")


        instances_to_create = []
        # Iterer sur les lignes du dataframe et enregistrer dans la base de données
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):

            if Club.objects.filter(club_id=row['club_id']).exists():
                mon_modele_instance = ClubGame(
                    game_id=row['game_id'],
                    club_id=row['club_id'],
                    own_goals=row['own_goals'],
                    own_position=row['own_position'],
                    own_manager_name=row['own_manager_name'],
                    opponent_id=row['opponent_id'],
                    opponent_goals=row['opponent_goals'],
                    opponent_position=row['opponent_position'],
                    opponent_manager_name=row['opponent_manager_name'],
                    hosting=row['hosting'],
                    # ... assignez d'autres champs comme requis
                )
                instances_to_create.append(mon_modele_instance)


        ClubGame.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))
