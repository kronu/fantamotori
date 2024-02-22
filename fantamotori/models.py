# Creazioni di nuovi oggetti/classi che contengono più varaibili
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utente (con username/password)
class User(AbstractUser):
    immagine = models.TextField()
    # fanta -> 0 = entrambi, 1 = solo moto, 2 = solo formula
    fanta = models.IntegerField(default="3")
    # Se inizio della stagione, rimuovi completamente l'utente
    # Se invece se ne va a metà stagione, assegnagli rimosso = True
    rimosso = models.BooleanField(default=False)


######################## Fantamoto #########################
class Moto_punti(models.Model):
    p_scontri = models.IntegerField(default="0")
    p_generali = models.IntegerField(default="0")
    differenza = models.IntegerField(default="0")
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)


class Moto_team(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
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
    totale = models.IntegerField(default=0)


class Moto_piloti(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    team = models.ForeignKey(Moto_team, on_delete=models.PROTECT, blank=True, null=True)
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
    totale = models.IntegerField(default=0)


class Moto_teammanager(models.Model):
    nome = models.TextField()
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    team = models.ForeignKey(Moto_team, on_delete=models.PROTECT, blank=True, null=True)
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
    totale = models.IntegerField(default=0)


class Moto_formazione(models.Model):
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT)
    giornata = models.IntegerField()
    data = models.DateTimeField()
    piloti = models.ManyToManyField(Moto_piloti)
    team = models.ManyToManyField(Moto_team)
    teammanager = models.ForeignKey(Moto_teammanager, on_delete=models.PROTECT, blank=True, null=True)
    p_totali = models.IntegerField(blank=True, null=True)
    risultato = models.IntegerField(blank=True, null=True)
    capitano = models.ForeignKey(Moto_piloti, on_delete=models.PROTECT, related_name="capitan", blank=True, null=True)
    cap_gara = models.IntegerField(blank=True, null=True)


class Moto_giornata(models.Model):
    data = models.DateTimeField()
    #categ -> "gp,2,3,e,sbk"
    categ = models.TextField()
    posto = models.TextField()
    calcolata = models.BooleanField(default=False)
    annullata = models.BooleanField(default=False)


class Moto_scontri(models.Model):
    giornata = models.ForeignKey(Moto_giornata, on_delete=models.PROTECT)
    # scontri -> "primo+secondo/terzo+quarto/..."
    scontri = models.TextField()


####################### Fanta Formula #########################
class Formula_punti(models.Model):
    p_scontri = models.IntegerField(default="0")
    p_generali = models.IntegerField(default="0")
    differenza = models.IntegerField(default="0")
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)


class Formula_team(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
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
    gara24 = models.IntegerField(blank=True, null=True)
    gara25 = models.IntegerField(blank=True, null=True)
    gara26 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


class Formula_piloti(models.Model):
    nome = models.TextField()
    categoria = models.TextField()
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    team = models.ForeignKey(Formula_team, on_delete=models.PROTECT, blank=True, null=True)
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
    gara24 = models.IntegerField(blank=True, null=True)
    gara25 = models.IntegerField(blank=True, null=True)
    gara26 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


class Formula_teammanager(models.Model):
    nome = models.TextField()
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    team = models.ForeignKey(Formula_team, on_delete=models.PROTECT, blank=True, null=True)
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
    gara24 = models.IntegerField(blank=True, null=True)
    gara25 = models.IntegerField(blank=True, null=True)
    gara26 = models.IntegerField(blank=True, null=True)
    totale = models.IntegerField(default=0)


class Formula_formazione(models.Model):
    username = models.TextField()
    utente = models.ForeignKey(User, on_delete=models.PROTECT)
    giornata = models.IntegerField()
    data = models.DateTimeField()
    piloti = models.ManyToManyField(Formula_piloti)
    team = models.ManyToManyField(Formula_team)
    teammanager = models.ForeignKey(Formula_teammanager, on_delete=models.PROTECT, blank=True, null=True)
    p_totali = models.IntegerField(blank=True, null=True)
    risultato = models.IntegerField(blank=True, null=True)
    capitano = models.ForeignKey(Formula_piloti, on_delete=models.PROTECT, related_name="capitan", blank=True, null=True)
    cap_gara = models.IntegerField(blank=True, null=True)


class Formula_giornata(models.Model):
    data = models.DateTimeField()
    # categ -> "sprint,f1,f2,f3,indy"
    categ = models.TextField()
    posto = models.TextField()
    calcolata = models.BooleanField(default=False)
    annullata = models.BooleanField(default=False)


class Formula_scontri(models.Model):
    giornata = models.ForeignKey(Formula_giornata, on_delete=models.PROTECT)
    # scontri -> "primo+secondo/terzo+quarto/..."
    scontri = models.TextField()