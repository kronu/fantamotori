# Creazioni di nuovi oggetti/classi che contengono più varaibili
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utente (con username/password)
class User(AbstractUser):
    immagine = models.TextField()
    # Se partecipa al fantaformula
    fantaformula = models.BooleanField(default=True)
    # Se inizio della stagione, rimuovi completamente l'utente
    # Se invece se ne va a metà stagione, assegnagli rimosso = True
    rimosso = models.BooleanField(default=False)


######################## Fantamoto #########################
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
    gara01 = models.IntegerField(blank=True, null=True)
    gara02 = models.IntegerField(blank=True, null=True)
    gara03 = models.IntegerField(blank=True, null=True)
    gara04 = models.IntegerField(blank=True, null=True)
    gara05 = models.IntegerField(blank=True, null=True)
    gara06 = models.IntegerField(blank=True, null=True)
    gara07 = models.IntegerField(blank=True, null=True)
    gara08 = models.IntegerField(blank=True, null=True)
    gara09 = models.IntegerField(blank=True, null=True)
    gara10 = models.IntegerField(blank=True, null=True)
    gara11 = models.IntegerField(blank=True, null=True)
    gara12 = models.IntegerField(blank=True, null=True)
    gara13 = models.IntegerField(blank=True, null=True)
    gara14 = models.IntegerField(blank=True, null=True)
    gara15 = models.IntegerField(blank=True, null=True)
    gara16 = models.IntegerField(blank=True, null=True)
    gara17 = models.IntegerField(blank=True, null=True)
    gara18 = models.IntegerField(blank=True, null=True)
    gara19 = models.IntegerField(blank=True, null=True)
    gara20 = models.IntegerField(blank=True, null=True)
    gara21 = models.IntegerField(blank=True, null=True)
    gara22 = models.IntegerField(blank=True, null=True)
    gara23 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


class Moto_team(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)
    gara01 = models.IntegerField(blank=True, null=True)
    gara02 = models.IntegerField(blank=True, null=True)
    gara03 = models.IntegerField(blank=True, null=True)
    gara04 = models.IntegerField(blank=True, null=True)
    gara05 = models.IntegerField(blank=True, null=True)
    gara06 = models.IntegerField(blank=True, null=True)
    gara07 = models.IntegerField(blank=True, null=True)
    gara08 = models.IntegerField(blank=True, null=True)
    gara09 = models.IntegerField(blank=True, null=True)
    gara10 = models.IntegerField(blank=True, null=True)
    gara11 = models.IntegerField(blank=True, null=True)
    gara12 = models.IntegerField(blank=True, null=True)
    gara13 = models.IntegerField(blank=True, null=True)
    gara14 = models.IntegerField(blank=True, null=True)
    gara15 = models.IntegerField(blank=True, null=True)
    gara16 = models.IntegerField(blank=True, null=True)
    gara17 = models.IntegerField(blank=True, null=True)
    gara18 = models.IntegerField(blank=True, null=True)
    gara19 = models.IntegerField(blank=True, null=True)
    gara20 = models.IntegerField(blank=True, null=True)
    gara21 = models.IntegerField(blank=True, null=True)
    gara22 = models.IntegerField(blank=True, null=True)
    gara23 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


class Moto_teammanager(models.Model):
    nome = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)
    gara01 = models.IntegerField(blank=True, null=True)
    gara02 = models.IntegerField(blank=True, null=True)
    gara03 = models.IntegerField(blank=True, null=True)
    gara04 = models.IntegerField(blank=True, null=True)
    gara05 = models.IntegerField(blank=True, null=True)
    gara06 = models.IntegerField(blank=True, null=True)
    gara07 = models.IntegerField(blank=True, null=True)
    gara08 = models.IntegerField(blank=True, null=True)
    gara09 = models.IntegerField(blank=True, null=True)
    gara10 = models.IntegerField(blank=True, null=True)
    gara11 = models.IntegerField(blank=True, null=True)
    gara12 = models.IntegerField(blank=True, null=True)
    gara13 = models.IntegerField(blank=True, null=True)
    gara14 = models.IntegerField(blank=True, null=True)
    gara15 = models.IntegerField(blank=True, null=True)
    gara16 = models.IntegerField(blank=True, null=True)
    gara17 = models.IntegerField(blank=True, null=True)
    gara18 = models.IntegerField(blank=True, null=True)
    gara19 = models.IntegerField(blank=True, null=True)
    gara20 = models.IntegerField(blank=True, null=True)
    gara21 = models.IntegerField(blank=True, null=True)
    gara22 = models.IntegerField(blank=True, null=True)
    gara23 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


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
    # Campo boolean se c'è la MotoE e/o la SBK
    motoe = models.BooleanField(default=False)
    sbk = models.BooleanField(default=False)
    posto = models.TextField(default="a")
    calcolata = models.BooleanField(default=False)


class Moto_passato(models.Model):
    ex_pscontri = models.IntegerField(default="0")
    ex_pgenerali = models.IntegerField(default="0")
    ex_differenza = models.IntegerField(default="0")
    ex_username = models.TextField(default="a")


####################### Fanta Formula #########################
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
    gara01 = models.IntegerField(blank=True, null=True)
    gara02 = models.IntegerField(blank=True, null=True)
    gara03 = models.IntegerField(blank=True, null=True)
    gara04 = models.IntegerField(blank=True, null=True)
    gara05 = models.IntegerField(blank=True, null=True)
    gara06 = models.IntegerField(blank=True, null=True)
    gara07 = models.IntegerField(blank=True, null=True)
    gara08 = models.IntegerField(blank=True, null=True)
    gara09 = models.IntegerField(blank=True, null=True)
    gara10 = models.IntegerField(blank=True, null=True)
    gara11 = models.IntegerField(blank=True, null=True)
    gara12 = models.IntegerField(blank=True, null=True)
    gara13 = models.IntegerField(blank=True, null=True)
    gara14 = models.IntegerField(blank=True, null=True)
    gara15 = models.IntegerField(blank=True, null=True)
    gara16 = models.IntegerField(blank=True, null=True)
    gara17 = models.IntegerField(blank=True, null=True)
    gara18 = models.IntegerField(blank=True, null=True)
    gara19 = models.IntegerField(blank=True, null=True)
    gara20 = models.IntegerField(blank=True, null=True)
    gara21 = models.IntegerField(blank=True, null=True)
    gara22 = models.IntegerField(blank=True, null=True)
    gara23 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


class Formula_team(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)
    gara01 = models.IntegerField(blank=True, null=True)
    gara02 = models.IntegerField(blank=True, null=True)
    gara03 = models.IntegerField(blank=True, null=True)
    gara04 = models.IntegerField(blank=True, null=True)
    gara05 = models.IntegerField(blank=True, null=True)
    gara06 = models.IntegerField(blank=True, null=True)
    gara07 = models.IntegerField(blank=True, null=True)
    gara08 = models.IntegerField(blank=True, null=True)
    gara09 = models.IntegerField(blank=True, null=True)
    gara10 = models.IntegerField(blank=True, null=True)
    gara11 = models.IntegerField(blank=True, null=True)
    gara12 = models.IntegerField(blank=True, null=True)
    gara13 = models.IntegerField(blank=True, null=True)
    gara14 = models.IntegerField(blank=True, null=True)
    gara15 = models.IntegerField(blank=True, null=True)
    gara16 = models.IntegerField(blank=True, null=True)
    gara17 = models.IntegerField(blank=True, null=True)
    gara18 = models.IntegerField(blank=True, null=True)
    gara19 = models.IntegerField(blank=True, null=True)
    gara20 = models.IntegerField(blank=True, null=True)
    gara21 = models.IntegerField(blank=True, null=True)
    gara22 = models.IntegerField(blank=True, null=True)
    gara23 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


class Formula_teammanager(models.Model):
    nome = models.TextField()
    username = models.TextField(default="a")
    utente = models.ForeignKey(User, on_delete=models.PROTECT)
    gara01 = models.IntegerField(blank=True, null=True)
    gara02 = models.IntegerField(blank=True, null=True)
    gara03 = models.IntegerField(blank=True, null=True)
    gara04 = models.IntegerField(blank=True, null=True)
    gara05 = models.IntegerField(blank=True, null=True)
    gara06 = models.IntegerField(blank=True, null=True)
    gara07 = models.IntegerField(blank=True, null=True)
    gara08 = models.IntegerField(blank=True, null=True)
    gara09 = models.IntegerField(blank=True, null=True)
    gara10 = models.IntegerField(blank=True, null=True)
    gara11 = models.IntegerField(blank=True, null=True)
    gara12 = models.IntegerField(blank=True, null=True)
    gara13 = models.IntegerField(blank=True, null=True)
    gara14 = models.IntegerField(blank=True, null=True)
    gara15 = models.IntegerField(blank=True, null=True)
    gara16 = models.IntegerField(blank=True, null=True)
    gara17 = models.IntegerField(blank=True, null=True)
    gara18 = models.IntegerField(blank=True, null=True)
    gara19 = models.IntegerField(blank=True, null=True)
    gara20 = models.IntegerField(blank=True, null=True)
    gara21 = models.IntegerField(blank=True, null=True)
    gara22 = models.IntegerField(blank=True, null=True)
    gara23 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


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
    # Campo boolean se c'è la sprint race e/o la F2
    sprint = models.BooleanField(default=False)
    f2 = models.BooleanField(default=False)
    posto = models.TextField(default="a")
    calcolata = models.BooleanField(default=False)


class Formula_passato(models.Model):
    ex_pscontri = models.IntegerField(default="0")
    ex_pgenerali = models.IntegerField(default="0")
    ex_differenza = models.IntegerField(default="0")
    ex_username = models.TextField(default="a")