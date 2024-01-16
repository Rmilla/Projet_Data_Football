import pandas as pd
from django.core.management.base import BaseCommand
from django_app_foot.models import Appearance, Player
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('django_app_foot/management/csv/appearances.csv', encoding="utf8")

        instances_to_create = []
        missing_player_ids_count = 0
        # Iterer sur les lignes du dataframe et ajouter les instances à la liste
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            if Player.objects.filter(player_id=row['player_id']).exists():
                mon_modele_instance = Appearance(
                    appearance_id=row['appearance_id'],
                    game_id=row['game_id'],
                    player_id=row['player_id'],
                    player_club_id=row['player_club_id'],
                    player_current_club_id=row['player_current_club_id'],
                    date=row['date'],
                    player_name=row['player_name'],
                    competition_id=row['competition_id'],
                    yellow_cards=row['yellow_cards'],
                    red_cards=row['red_cards'],
                    goals=row['goals'],
                    assists=row['assists'],
                    minutes_played=row['minutes_played'],
                    # ... assignez d'autres champs comme requis
                )
                instances_to_create.append(mon_modele_instance)
        else:
            print(
                f"player_id {row['player_id']} n'existe pas dans la table Player.")
            missing_player_ids_count += 1

        Appearance.objects.bulk_create(instances_to_create)
        self.stdout.write(self.style.WARNING(
            f'Nombre de player_id manquants : {missing_player_ids_count}'))
        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))