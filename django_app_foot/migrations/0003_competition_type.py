# Generated by Django 5.0.1 on 2024-01-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app_foot', '0002_alter_competition_competition_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
