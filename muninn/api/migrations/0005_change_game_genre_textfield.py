# Generated by Django 2.0.7 on 2018-07-30 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_change_game_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.TextField(),
        ),
    ]
