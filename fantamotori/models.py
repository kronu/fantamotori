from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    immagine = models.TextField()
    fantaformula = models.BooleanField(default=True)

#Fantamoto
class Moto_punti(models.Model):
    p_scontri = models.IntegerField(default="0")
    p_generali = models.IntegerField(default="0")
    differenza = models.IntegerField(default="0")
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT, default="1")

class Moto_piloti(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)

class Moto_team(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)

class Moto_teammanager(models.Model):
    nome = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)

class Moto_formazione(models.Model):
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)
    giornata = models.IntegerField()
    data = models.DateTimeField()
    piloti = models.ManyToManyField(Moto_piloti)
    team = models.ManyToManyField(Moto_team)
    teammanager = models.ForeignKey(Moto_teammanager, on_delete=models.PROTECT, blank=True, null=True)
    p_totali = models.IntegerField(blank=True, null=True)
    risultato = models.IntegerField(blank=True, null=True)
    capitano = models.ForeignKey(Moto_piloti, on_delete=models.PROTECT, related_name="capitan", blank=True, null=True)

class Moto_giornata(models.Model):
    data = models.DateTimeField()
    motoe = models.BooleanField(default=False)
    posto = models.TextField(default="a")


#Fanta Formula
class Formula_punti(models.Model):
    p_scontri = models.IntegerField(default="0")
    p_generali = models.IntegerField(default="0")
    differenza = models.IntegerField(default="0")
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT, default="1")

class Formula_piloti(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)

class Formula_team(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)

class Formula_teammanager(models.Model):
    nome = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)

class Formula_formazione(models.Model):
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)
    giornata = models.IntegerField()
    data = models.DateTimeField()
    piloti = models.ManyToManyField(Formula_piloti)
    team = models.ManyToManyField(Formula_team)
    teammanager = models.ForeignKey(Formula_teammanager, on_delete=models.PROTECT, blank=True, null=True)
    p_totali = models.IntegerField(blank=True, null=True)
    risultato = models.IntegerField(blank=True, null=True)

class Formula_giornata(models.Model):
    data = models.DateTimeField()
    f2 = models.BooleanField(default=False)
    posto = models.TextField(default="a")