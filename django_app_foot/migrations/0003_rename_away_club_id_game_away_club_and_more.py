# Generated by Django 5.0.1 on 2024-01-12 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app_foot', '0002_alter_game_competition_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='away_club_id',
            new_name='away_club',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='competition_id',
            new_name='competition',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='home_club_id',
            new_name='home_club',
        ),
    ]
