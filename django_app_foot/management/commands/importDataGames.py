import pandas as pd
from django.core.management.base import BaseCommand
from django_app_foot.models import Game
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas

        data = pd.read_csv(
            'django_app_foot/management/csv/games.csv', encoding="utf8")
        print(data.isnull().sum())
        # data.to_numeric()
        data.fillna(0, inplace=True)

        instances_to_create = []

        # Iterer sur les lignes du dataframe et ajouter les instances à la liste
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            mon_modele_instance = Game(

                game_id=row['game_id'],
                season=row['season'],
                round=row['round'],
                date=row['date'],
                home_club_goals=row['home_club_goals'],
                away_club_goals=row['away_club_goals'],
                home_club_position=row['home_club_position'],
                competition_id=row['competition_id'],
                home_club_id=row['home_club_id'],
                away_club_id=row['away_club_id']
            )

            instances_to_create.append(mon_modele_instance)

        Game.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))

