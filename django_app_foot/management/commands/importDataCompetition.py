import pandas as pd
from django.core.management.base import BaseCommand
from django_app_foot.models import Competition
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('django_app_foot/management/csv/competitions.csv', encoding="utf8")

        instances_to_create = []

        # Iterer sur les lignes du dataframe et ajouter les instances à la liste
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            mon_modele_instance = Competition(
                competition_id=row['competition_id'],
                competition_code=row['competition_code'],
                name=row['name'],
                sub_type=row['sub_type'],
                type=row['type'],
                country_name=row['country_name'],
                domestic_league_code=row['domestic_league_code'],
                confederation=row['confederation'],
                url=row['url'],
                country_id=row['country_id']
            )
            instances_to_create.append(mon_modele_instance)

        Competition.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))