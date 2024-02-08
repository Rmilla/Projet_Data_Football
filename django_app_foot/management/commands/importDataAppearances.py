import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction, connections
from django_app_foot.models import Appearance, Player, Club
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas par lots
        chunk_size = 100
        data_chunks = pd.read_csv('django_app_foot/management/csv/appearances.csv', encoding="utf8", chunksize=chunk_size)

        # Compter le nombre total de chunks
        total_chunks = sum(1 for _ in data_chunks)

        # Recharger le fichier CSV avec pandas par lots pour la boucle principale
        data_chunks = pd.read_csv('django_app_foot/management/csv/appearances.csv', encoding="utf8", chunksize=chunk_size)

        instances_to_create = []
        missing_player_ids_count = 0

        # Vérifier la connexion à la base de données avant l'opération bulk_create
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT 1')

        # Récupérer tous les player_ids à l'avance pour éviter les requêtes individuelles dans la boucle
        existing_player_ids = set(Player.objects.values_list('player_id', flat=True))

        # Iterer sur les chunks du dataframe et ajouter les instances à la liste
        for data_chunk in tqdm(data_chunks, desc='Importation des données', total=total_chunks):
            for index, row in data_chunk.iterrows():
                player_id = row['player_id']

                # Utiliser filter pour vérifier l'existence du joueur
                player_instance = Player.objects.filter(player_id=player_id).first()
                club_instance, created = Club.objects.get_or_create(club_id=row['player_club_id'])
                if player_instance is None:
                    # Si le joueur n'existe pas, passer à la ligne suivante
                    print(f"player_id {player_id} n'existe pas dans la table Player.")
                    missing_player_ids_count += 1
                    continue
                
                mon_modele_instance = Appearance(
                    appearance_id=row['appearance_id'],
                    game_id=row['game_id'],
                    player=player_instance,
                    player_club_id=row['player_club_id'],
                    fk_player_club=club_instance,
                    yellow_cards=row['yellow_cards'],
                    red_cards=row['red_cards'],
                    goals=row['goals'],
                    assists=row['assists'],
                    minutes_played=row['minutes_played'],
                    # ... assignez d'autres champs comme requis
                )
                instances_to_create.append(mon_modele_instance)

        # Début de la transaction pour bulk_create par lots plus petits
        with transaction.atomic():
            for chunk in chunks(instances_to_create, chunk_size):
                Appearance.objects.bulk_create(chunk)

        # Vérifier la connexion à la base de données après l'opération bulk_create
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT 1')

        self.stdout.write(self.style.WARNING(
            f'Nombre de player_id manquants : {missing_player_ids_count}'))
        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))

def chunks(lst, chunk_size):
    """Divise une liste en chunks de taille spécifiée."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]