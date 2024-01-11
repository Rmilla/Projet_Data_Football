# myapp/management/commands/import_data.py

import pandas as pd
from django.core.management.base import BaseCommand
from django_app_foot.models import Competition

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('django_app_foot\management\csv\competitions.csv')

        # Iterer sur les lignes du dataframe et enregistrer dans la base de données
        for index, row in data.iterrows():
            mon_modele_instance = Competition(
                competition_id=row['competition_id'],
                competition_code=row['competition_code'],
                name=row['name'],
                country_id=row['country_id'],
                # ... assignez d'autres champs comme requis
            )
            mon_modele_instance.save()

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))
