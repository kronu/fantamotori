# Generated by Django 4.0.2 on 2022-03-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantamotori', '0008_remove_moto_sfida_giornata_delete_formula_sfida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula_formazione',
            name='vittoria',
            field=models.BooleanField(default=False),
        ),
    ]
