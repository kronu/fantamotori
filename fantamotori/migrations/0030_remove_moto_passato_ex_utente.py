# Generated by Django 4.0.2 on 2022-12-07 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fantamotori', '0029_alter_moto_passato_ex_utente_alter_moto_punti_utente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moto_passato',
            name='ex_utente',
        ),
    ]
