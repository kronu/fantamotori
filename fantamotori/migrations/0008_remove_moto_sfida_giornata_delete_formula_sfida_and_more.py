# Generated by Django 4.0.2 on 2022-03-10 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fantamotori', '0007_moto_sfida_formula_sfida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moto_sfida',
            name='giornata',
        ),
        migrations.DeleteModel(
            name='Formula_sfida',
        ),
        migrations.DeleteModel(
            name='Moto_sfida',
        ),
    ]
