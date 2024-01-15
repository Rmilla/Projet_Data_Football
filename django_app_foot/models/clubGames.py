from django.db import models

class ClubGames(models.Model):
    game_id = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='games')
    club_id = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='clubs')
    own_goals = models.IntegerField()
    own_position = models.FloatField(null=True, blank=True)
    own_manager_name = models.CharField(max_length=100)
    opponent_id = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='opponent_club')
    opponent_goals = models.IntegerField()
    opponent_position = models.FloatField(null=True, blank=True)
    opponent_manager_name = models.CharField(max_length=100)
    hosting = models.CharField(max_length=100)

    def __str__(self) :
        return f'{self.game_id}'