# Generated by Django 5.0.1 on 2024-01-15 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app_foot', '0025_rename_opponent_clubgame_opponent_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubgame',
            old_name='opponent_id',
            new_name='opponent',
        ),
    ]
