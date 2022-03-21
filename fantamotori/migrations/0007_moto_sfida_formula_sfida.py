# Generated by Django 4.0.2 on 2022-03-10 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fantamotori', '0006_formula_formazione_username_formula_piloti_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moto_sfida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giocatori', models.TextField()),
                ('giornata', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fantamotori.moto_giornata')),
            ],
        ),
        migrations.CreateModel(
            name='Formula_sfida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giocatori', models.TextField()),
                ('giornata', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fantamotori.moto_giornata')),
            ],
        ),
    ]
