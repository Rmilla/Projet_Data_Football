# Generated by Django 5.0.1 on 2024-01-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app_foot', '0007_alter_club_net_transfer_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='average_age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='club',
            name='foreigners_percentage',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='player',
            name='date_of_birth',
            field=models.CharField(max_length=255),
        ),
    ]
