# Generated by Django 5.0.1 on 2024-01-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app_foot', '0002_rename_opponents_position_club_games_opponent_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_games',
            name='own_position',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
