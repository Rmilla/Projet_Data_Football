# Generated by Django 5.0.1 on 2024-02-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app_foot', '0015_alter_clubgame_is_win'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubgame',
            name='is_win',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
