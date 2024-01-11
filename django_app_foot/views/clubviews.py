from django.db import transaction
from django_app_foot.models import clubModel
from django.shortcuts import render 
import csv

def import_data(request):
    with open('archive/clubs.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)

    clubs = []
    for row in data:
        club = clubModel.Club(club_id=row[0], club_code=row[1], domestic_competition_id=row[2],
                        squad_size=row[4], average_age=row[5],foreigners_number=row[6],foreigners_percentage=row[7],
                        national_team_players=row[8],stadium_name=row[9],stadium_seats=row[10],net_transfer_record=row[11],
                        coach_name=row[12],last_season=row[13],url=row[15])
        clubs.append(club)

    with transaction.atomic():
        clubModel.Club.objects.bulk_create(clubs)

    return render(request, 'import_data.html', {'clubs':clubs})
