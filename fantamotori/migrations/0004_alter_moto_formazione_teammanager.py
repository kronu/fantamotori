# Generated by Django 5.0.1 on 2024-01-22 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantamotori', '0003_remove_formula_team_piloti_remove_moto_team_piloti_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moto_formazione',
            name='teammanager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fantamotori.moto_teammanager'),
        ),
    ]
