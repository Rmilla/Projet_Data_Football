from django.db import transaction
from django_app_foot.models import Club_games  # Utilisation du modèle correct
from django.shortcuts import render 
import logging
import csv

logger = logging.getLogger(__name__)

def import_data_club_games(request):  
    game_id = request.GET.get('game_id')
    logger.debug(f"Valeur de game_id dans la vue : {game_id}")
    
    with open('archive/club_games.csv', 'r') as csvfile: 
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        data = list(reader)

        clubs_games = []
        for row in data: 
            try:
                club = Club_games(
                    game_id=int(row[0]) if row[0] else None,
                    club_id=int(row[1]) if row[1] else None,
                    own_goals=int(row[2]) if row[2] else None,
                    own_position=int(row[3]) if row[3] and row[3] != 'null' else 0,  # Utiliser 0 comme valeur par défaut
                    own_manager_name=row[4],
                    opponent_id=int(row[5]) if row[5] else None,
                    opponent_goals=int(row[6]) if row[6] else None,
                    opponents_position=int(row[7]) if row[7] and row[7] != 'null' else 0,  # Utiliser 0 comme valeur par défaut
                    opponent_manager_name=row[8],
                    hosting=row[9]
                )
                clubs_games.append(club)
            except ValueError as e:
            # Gérer l'erreur de conversion
                logger.warning(f"Erreur de conversion : {e}. Ligne ignorée : {row}")


        with transaction.atomic():
            Club_games.objects.bulk_create(clubs_games)

    return render(request, 'import_data.html', {'clubs_games': clubs_games})