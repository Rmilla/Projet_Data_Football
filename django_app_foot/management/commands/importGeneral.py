from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Base import for Django '

    def handle(self, *args, **options):
        call_command('cities', *['--import', 'importDataCompetitions'])
        call_command('cities', *['--import', 'importDataClubs'])
        call_command('cities', *['--import', 'importDataPlayers'])
        call_command('cities', *['--import', 'importDataGames'])
        call_command('cities', *['--import', 'importDataClubGames'])
        call_command('cities', *['--import', 'importDataGameEvents'])
        call_command('cities', *['--import', 'importDataAppearances'])
        call_command('cities', *['--import', 'importDataPlayersValuations'])