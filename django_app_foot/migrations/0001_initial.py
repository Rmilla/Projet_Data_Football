# Generated by Django 5.0.1 on 2024-01-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appearances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('competition_id', models.CharField(max_length=100)),
                ('yellow_cards', models.IntegerField()),
                ('red_cards', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Club_games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField()),
                ('club_id', models.IntegerField()),
                ('own_goals', models.IntegerField()),
                ('own_position', models.IntegerField()),
                ('own_manager_name', models.CharField()),
                ('opponent_id', models.IntegerField()),
                ('opponent_goals', models.IntegerField()),
                ('opponent_position', models.IntegerField()),
                ('opponent_manager_name', models.CharField(max_length=100)),
                ('hosting', models.CharField(max_length=100)),
            ],
        ),
    ]
