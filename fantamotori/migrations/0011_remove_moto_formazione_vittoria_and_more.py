# Generated by Django 4.0.2 on 2022-03-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantamotori', '0010_moto_formazione_vittoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moto_formazione',
            name='vittoria',
        ),
        migrations.AddField(
            model_name='moto_formazione',
            name='risultato',
            field=models.IntegerField(default='0'),
        ),
    ]
