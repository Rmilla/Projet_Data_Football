from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Base import for Django'

    def handle(self, *args, **options):
        call_command('importDataCompetitions', **options)
        call_command('importDataClubs', **options)
        call_command('importDataPlayers', **options)
        call_command('importDataGames', **options)
        call_command('importDataClubGames', **options)
        call_command('importDataGameEvents', **options)
        call_command('importDataAppearances', **options)
        call_command('importDataPlayersValuations', **options)