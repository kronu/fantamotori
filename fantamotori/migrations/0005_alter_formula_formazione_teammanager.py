# Generated by Django 5.0.1 on 2024-01-24 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantamotori', '0004_alter_moto_formazione_teammanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula_formazione',
            name='teammanager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fantamotori.formula_teammanager'),
        ),
    ]
