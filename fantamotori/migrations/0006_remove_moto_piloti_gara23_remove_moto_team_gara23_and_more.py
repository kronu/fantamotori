# Generated by Django 5.0.1 on 2024-02-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantamotori', '0005_alter_formula_formazione_teammanager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moto_piloti',
            name='gara23',
        ),
        migrations.RemoveField(
            model_name='moto_team',
            name='gara23',
        ),
        migrations.RemoveField(
            model_name='moto_teammanager',
            name='gara23',
        ),
        migrations.AddField(
            model_name='formula_piloti',
            name='gara24',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='formula_piloti',
            name='gara25',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='formula_piloti',
            name='gara26',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='formula_team',
            name='gara24',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='formula_team',
            name='gara25',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='formula_team',
            name='gara26',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='formula_teammanager',
            name='gara24',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='formula_teammanager',
            name='gara25',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='formula_teammanager',
            name='gara26',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
