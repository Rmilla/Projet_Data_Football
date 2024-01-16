import csv
from tqdm import tqdm
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from django_app_foot.models import club

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        with open('django_app_foot/management/csv/clubs.csv', 'r', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            clubs = []
            for row in tqdm(reader, desc="Importing data", unit=" rows"):
                club_instance = club.Club(
                    club_id=row['club_id'],
                    club_code=row['club_code'],
                    name=row['name'],
                    squad_size=row['squad_size'],
                    average_age=row['average_age'],
                    foreigners_number=row['foreigners_number'],
                    foreigners_percentage=row['foreigners_percentage'],
                    national_team_players=row['national_team_players'],
                    stadium_name=row['stadium_name'],
                    stadium_seats=row['stadium_seats'],
                    net_transfer_record=row['net_transfer_record'],
                    coach_name=row['coach_name'],
                    last_season=row['last_season'],
                    url=row['url']
                )
                clubs.append(club_instance)

        with transaction.atomic():
            club.Club.objects.bulk_create(clubs)

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))