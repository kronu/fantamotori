from cmath import log
from django.forms import ValidationError
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Moto_giornata, Moto_formazione, Moto_piloti, Moto_punti, Moto_team, Moto_teammanager, User
from .models import Formula_giornata, Formula_formazione, Formula_piloti, Formula_punti, Formula_team, Formula_teammanager

def register(request):
    raise Exception("Non dovresti essere qui")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username, username, password)
        user.save()
        return render(request, "register.html", {
            "message": "Utente salvato"
        })
    return render(request, "register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("sceltafanta"))
        else:
            return render(request, "login.html", {
                "message": "Username e/o password non corrette"
            })
    return render(request, "login.html")


@login_required
def sceltafanta(request):
    return render(request, "scelta_fanta.html")


################################### MOTO #######################################
@login_required
def moto_home(request):
    now = timezone.localtime()
    alldates = Moto_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    nextgara = Moto_giornata.objects.get(data=nextdate)
    return render(request, "fantamoto/home.html", {
        "nextgara": nextgara
    })
    

@login_required
def moto_classscontri(request):
    ranking = Moto_punti.objects.order_by("-p_scontri", "-differenza")
    return render(request, "fantamoto/classifica_scontri.html", {
        "ranking": ranking
    })


@login_required
def moto_classpunti(request):
    ranking = Moto_punti.objects.order_by("-p_generali", "-differenza")
    return render(request, "fantamoto/classifica_punti.html", {
        "ranking": ranking
    })


@login_required
def moto_rose(request):
    tutti = User.objects.order_by("username")
    return render(request, "fantamoto/rose_totali.html", {
        "tutti": tutti
    })


@login_required
def moto_rosautente(request, utente):
    piloti = Moto_piloti.objects.filter(username=utente)
    teams = Moto_team.objects.filter(username=utente)
    team_man = Moto_teammanager.objects.get(username=utente)
    return render(request, "fantamoto/rosa_utente.html", {
        "utente": utente,
        "piloti": piloti,
        "teams": teams,
        "tm": team_man
    })


@login_required
def moto_cal_scelta(request):
    giornate = Moto_giornata.objects.all()
    return render(request, "fantamoto/calendario.html", {
        "giornate": giornate
    })


@login_required 
def moto_calendario(request, id):
    giornata = Moto_giornata.objects.get(id=id)
    if id == "1" or id == "10" or id == "19":
        sfida1 = ["Albwin27", "Zanno"]
        sfida2 = ["Paul Bird Motorsport", "Tazza"]
        sfida3 = ["Dragon trainer", "Cicciobirro01"]
        sfida4 = ["Team As Turbo", "Pellons"]
        sfida5 = ["Cortez Black Team", "Vettel05"]
    elif id == "2" or id == "11" or id == "20":
        sfida1 = ["Tazza", "Albwin27"]
        sfida2 = ["Cicciobirro01", "Zanno"]
        sfida3 = ["Pellons", "Paul Bird Motorsport"]
        sfida4 = ["Vettel05", "Dragon trainer"]
        sfida5 = ["Cortez Black Team", "Team As Turbo"]
    elif id == "3" or id == "12" or id == "21":
        sfida1 = ["Albwin27", "Cortez Black Team"]
        sfida2 = ["Vettel05", "Team As Turbo"]
        sfida3 = ["Pellons", "Dragon trainer"]
        sfida4 = ["Cicciobirro01", "Paul Bird Motorsport"]
        sfida5 = ["Zanno", "Tazza"]
    elif id == "4" or id == "13":
        sfida1 = ["Pellons", "Albwin27"]
        sfida2 = ["Vettel05", "Cicciobirro01"]
        sfida3 = ["Tazza", "Cortez Black Team"]
        sfida4 = ["Team As Turbo", "Zanno"]
        sfida5 = ["Dragon trainer", "Paul Bird Motorsport"]
    elif id == "5" or id == "14":
        sfida1 = ["Albwin27", "Vettel05"]
        sfida2 = ["Cortez Black Team", "Pellons"]
        sfida3 = ["Cicciobirro01", "Team As Turbo"]
        sfida4 = ["Tazza", "Dragon trainer"]
        sfida5 = ["Zanno", "Paul Bird Motorsport"]
    elif id == "6" or id == "15":
        sfida1 = ["Cicciobirro01", "Albwin27"]
        sfida2 = ["Pellons", "Tazza"]
        sfida3 = ["Zanno", "Vettel05"]
        sfida4 = ["Paul Bird Motorsport", "Cortez Black Team"]
        sfida5 = ["Team As Turbo", "Dragon trainer"]
    elif id == "7" or id == "16":
        sfida1 = ["Albwin27", "Team As Turbo"]
        sfida2 = ["Dragon trainer", "Cortez Black Team"]
        sfida3 = ["Paul Bird Motorsport", "Vettel05"]
        sfida4 = ["Zanno", "Pellons"]
        sfida5 = ["Tazza", "Cicciobirro01"]
    elif id == "8" or id == "17":
        sfida1 = ["Dragon trainer", "Albwin27"]
        sfida2 = ["Paul Bird Motorsport", "Team As Turbo"]
        sfida3 = ["Cortez Black Team", "Zanno"]
        sfida4 = ["Vettel05", "Tazza"]
        sfida5 = ["Cicciobirro01", "Pellons"]
    elif id == "9" or id == "18":
        sfida1 = ["Albwin27", "Paul Bird Motorsport"]
        sfida2 = ["Dragon trainer", "Zanno"]
        sfida3 = ["Team As Turbo", "Tazza"]
        sfida4 = ["Cortez Black Team", "Cicciobirro01"]
        sfida5 = ["Vettel05", "Pellons"]
    return render(request, "fantamoto/giornata.html", {
        "now_id": id,
        "giornata": giornata,
        "sfida1": sfida1,
        "sfida2": sfida2,
        "sfida3": sfida3,
        "sfida4": sfida4,
        "sfida5": sfida5
    })


@login_required
def moto_scontro(request, id, scontro):
    sfida = scontro.replace("_", " - ")
    sfidante1 = scontro.split("_")[0]
    sfidante2 = scontro.split("_")[1]
    id_sfidante1 = User.objects.get(username=sfidante1).id
    id_sfidante2 = User.objects.get(username=sfidante2).id
    try:
        formazione1 = Moto_formazione.objects.get(utente_id=id_sfidante1, giornata=id)
    except:
        formazione1 = ""
    try:
        formazione2 = Moto_formazione.objects.get(utente_id=id_sfidante2, giornata=id)
    except:
        formazione2 = ""
    # Ottieni formazione primo user
    try:
        piloti1 = formazione1.piloti.all()
        teams1 = formazione1.team.all()
        tm1 = formazione1.teammanager.nome
    except:
        piloti1 = ""
        teams1 = ""
        tm1 = ""
    try:
        capitano1 = formazione1.capitano.nome
    except:
        capitano1 = None
    # Ottieni formazione secondo user
    try:
        piloti2 = formazione2.piloti.all()
        teams2 = formazione2.team.all()
        tm2 = formazione2.teammanager.nome
    except:
        piloti2 = ""
        teams2 = ""
        tm2 = ""
    try:
        capitano2 = formazione2.capitano.nome
    except:
        capitano2 = None
    return render(request, "fantamoto/risultato_scontro.html", {
        "now_id": id,
        "sfida": sfida,
        "formazione1": formazione1,
        "formazione2": formazione2,
        "piloti1": piloti1,
        "piloti2": piloti2,
        "teams1": teams1,
        "teams2": teams2,
        "tm1": tm1,
        "tm2": tm2,
        "capitano1": capitano1,
        "capitano2": capitano2
    })


@login_required
def moto_formazione(request):
    now = timezone.localtime()
    alldates = Moto_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    nextgara = Moto_giornata.objects.get(data=nextdate)
    piloti = Moto_piloti.objects.filter(utente_id=request.user.id)
    teams = Moto_team.objects.filter(utente_id=request.user.id)
    tm = Moto_teammanager.objects.get(utente_id=request.user.id)
    return render(request, "fantamoto/scelta_formazione.html", {
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "nextgara": nextgara
    })


@login_required
def moto_schieramento(request):
    if request.method == "POST":
        # Trova prossima gara
        now = timezone.localtime()
        alldates = Moto_giornata.objects.values_list('data', flat=True)
        alldates = list(alldates)
        for date in alldates:
            date = timezone.localtime(date)
            if date > now:
                nextdate = date
                break
        nextgara = Moto_giornata.objects.get(data=nextdate)
        # Variabili
        categorie_piloti = []
        categorie_teams = []
        check_capitano = []
        piloti = request.POST.getlist("piloti")
        teams = request.POST.getlist("teams")
        tm = request.POST.get("tm")
        capitano = request.POST["capitan"]
        # Se non c'è la MotoE
        if nextgara.motoe == 0:
            # Check numero piloti, teams e tm
            if len(piloti) != 6:
                raise ValidationError("Devi selezionare 6 piloti (NO MOTOE), per rifare la formazione torna indietro")
            if len(teams) != 3:
                raise ValidationError("Devi selezionare 3 team (NO MOTOE), per rifare la formazione torna indietro")
            if tm is None:
                raise ValidationError("Seleziona il team manager, per rifare la formazione torna indietro")
            # Check categoria piloti
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti or "MotoE" in categorie_piloti:
                raise ValidationError("Scegli almeno un pilota per ogni categoria, esclusa la MotoE")
            # Check categoria teams
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams or "MotoE" in categorie_teams:
                raise ValidationError("Scegli almeno un team per ogni categoria, esclusa la MotoE")
        # Se c'è la MotoE
        elif nextgara.motoe == 1:
            if len(piloti) != 7:
                raise ValidationError("Devi selezionare 7 piloti (CON MOTOE), per rifare la formazione torna indietro")
            if len(teams) != 4:
                raise ValidationError("Devi selezionare 4 team (CON MOTOE), per rifare la formazione torna indietro")
            if tm is None:
                raise ValidationError("Seleziona il team manager, per rifare la formazione torna indietro")
            # Check categoria piloti
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti or "MotoE" not in categorie_piloti:
                raise ValidationError("Scegli almeno un pilota per ogni categoria, inclusa la MotoE")
            # Check categoria teams
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams or "MotoE" not in categorie_teams:
                raise ValidationError("Scegli almeno un team per ogni categoria, inclusa la MotoE")
        # Check capitano sia tra gli schierati
        for pilota in piloti:
            check_capitano.append(pilota.split(" - ")[0])
        if capitano not in check_capitano and capitano != "0":
            raise ValidationError("Capitano selezionato non schierato nella formazione, per rifare la formazione torna indietro")
        # La formazione non ha errori
        # Se formazione già schierata, sostituiscila con quella nuova
        if Moto_formazione.objects.filter(giornata=nextgara.id, username=request.user.username):
            Moto_formazione.objects.filter(giornata=nextgara.id, username=request.user.username).delete()
        # Variabili
        formazione_giornata = nextgara.id
        formazione_data = now
        formazione_piloti = []
        formazione_teams = []
        for pilota in piloti:
            p = pilota.split(" - ")[0]
            p_id = Moto_piloti.objects.get(nome=p)
            formazione_piloti.append(p_id)
        for team in teams:
            t = team.split(" - ")[0]
            t_id = Moto_team.objects.get(nome=t)
            formazione_teams.append(t_id)
        formazione_tm = Moto_teammanager.objects.get(nome=tm)
        formazione_user = request.user
        if capitano != "0":
            formazione_capitano = Moto_piloti.objects.get(nome=capitano)
        else:
            formazione_capitano = None
        # Salva la formazione
        formazione = Moto_formazione.objects.create(
            giornata = formazione_giornata,
            data = formazione_data,
            teammanager = formazione_tm,
            username = request.user.username,
            utente = formazione_user,
            capitano = formazione_capitano)
        formazione.piloti.set(formazione_piloti)
        formazione.team.set(formazione_teams)
        formazione.save()
        return HttpResponseRedirect(reverse("fantamoto/home"))


@login_required
def moto_calcscelta(request):
    autorizzati = [1, 2, 3, 4]
    if request.user.id not in autorizzati:
        raise Exception("Non sei autorizzato ad accedere al calcolo giornate")
    giornate = Moto_giornata.objects.all()
    utenti = User.objects.all()
    return render(request, "fantamoto/calcolo_scelta.html", {
        "giornate": giornate,
        "utenti": utenti
    })


@login_required
def moto_calcformazione(request, id, utente):
    # Error handling
    autorizzati = [1, 2, 3, 4]
    if request.user.id not in autorizzati:
        raise Exception("Non sei autorizzato ad accedere al calcolo giornate")
    if id == "0" and utente == "0":
        raise Exception("Ricordati di selezionare una giornata e un utente")
    elif utente == "0":
        raise Exception("Ricordati di selezionare un utente")
    elif id == "0":
        raise Exception("Ricordati di selezionare una giornata")
    # Variabili
    user = User.objects.get(id=utente).username
    try:
        formazione = Moto_formazione.objects.get(utente_id=utente, giornata=id)
        piloti = formazione.piloti.all()
        teams = formazione.team.all()
        tm = formazione.teammanager
        capitano = formazione.capitano
        calcolata = formazione.p_totali
    except:
        now = timezone.localtime()
        giornata = Moto_giornata.objects.get(id=id).data
        if now > giornata:
            formazione = Moto_formazione.objects.create(
                giornata = id,
                data = now,
                utente_id = utente,
                username = user
            ).save()
        else:
            raise Exception("La gara non è stata ancora disputata >:(")
        return render(request, "fantamoto/calcolo_formazione.html", {
            "id": id,
            "utente": utente,
            "user": user
        })
    return render(request, "fantamoto/calcolo_formazione.html", {
        "id": id,
        "utente": utente,
        "user": user,
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "capitano": capitano,
        "calcolata": calcolata,
        "formazione": formazione
    })

 
@login_required
def moto_calctotale(request, id, utente):
    autorizzati = [1, 2, 3, 4]
    if request.user.id not in autorizzati:
        raise Exception("Non sei autorizzato ad accedere al calcolo giornate")
    if request.method == "POST":
        # Calcola il punteggio totale
        p_piloti = request.POST.getlist("p_piloti")
        p_teams = request.POST.getlist("p_teams")
        p_tm = request.POST.get("p_tm")
        p_totali = 0
        for uno in p_piloti:
            p_totali += int(uno)
        for uno in p_teams:
            p_totali += int(uno)
        p_totali += int(p_tm)
        # Controlla chi è l'avversario
        user = User.objects.get(id=utente).username
        if id == "1" or id == "10" or id == "19":
            sfide = [["Albwin27", "Zanno"], ["Paul Bird Motorsport", "Tazza"], ["Dragon trainer", "Cicciobirro01"], ["Team As Turbo", "Pellons"],
            ["Cortez Black Team", "Vettel05"]]
        elif id == "2" or id == "11" or id == "20":
            sfide = [["Tazza", "Albwin27"], ["Cicciobirro01", "Zanno"], ["Pellons", "Paul Bird Motorsport"], ["Vettel05", "Dragon trainer"],
            ["Cortez Black Team", "Team As Turbo"]]
        elif id == "3" or id == "12" or id == "21":
            sfide = [["Albwin27", "Cortez Black Team"], ["Vettel05", "Team As Turbo"], ["Pellons", "Dragon trainer"], 
            ["Cicciobirro01", "Paul Bird Motorsport"], ["Zanno", "Tazza"]]
        elif id == "4" or id == "13":
            sfide = [["Pellons", "Albwin27"], ["Vettel05", "Cicciobirro01"], ["Tazza", "Cortez Black Team"], ["Team As Turbo", "Zanno"], 
            ["Dragon trainer", "Paul Bird Motorsport"]]
        elif id == "5" or id == "14":
            sfide = [["Albwin27", "Vettel05"], ["Cortez Black Team", "Pellons"], ["Cicciobirro01", "Team As Turbo"], ["Tazza", "Dragon trainer"],
            ["Zanno", "Paul Bird Motorsport"]]
        elif id == "6" or id == "15":
            sfide = [["Cicciobirro01", "Albwin27"], ["Pellons", "Tazza"], ["Zanno", "Vettel05"], ["Paul Bird Motorsport", "Cortez Black Team"], 
            ["Team As Turbo", "Dragon trainer"]]
        elif id == "7" or id == "16":
            sfide = [["Albwin27", "Team As Turbo"], ["Dragon trainer", "Cortez Black Team"], ["Paul Bird Motorsport", "Vettel05"], 
            ["Zanno", "Pellons"], ["Tazza", "Cicciobirro01"]]
        elif id == "8" or id == "17":
            sfide = [["Dragon trainer", "Albwin27"], ["Paul Bird Motorsport", "Team As Turbo"], ["Cortez Black Team", "Zanno"], 
            ["Vettel05", "Tazza"], ["Cicciobirro01", "Pellons"]]
        elif id == "9" or id == "18":
            sfide = [["Albwin27", "Paul Bird Motorsport"], ["Dragon trainer", "Zanno"], ["Team As Turbo", "Tazza"],
            ["Cortez Black Team", "Cicciobirro01"], ["Vettel05", "Pellons"]]
        for i in range(5):
            if user in sfide[i]:
                sfide[i].remove(user)
                avversario = sfide[i][0]
        # Variabili
        formazione_utente = Moto_formazione.objects.get(giornata=id, utente_id=utente)
        user_punti = Moto_punti.objects.get(utente_id=utente)
        avv_punti = Moto_punti.objects.get(username=avversario)
        # Se formazione avversaria già controllata aggiungi il risultato dello scontro
        try:
            formazione_avversario = Moto_formazione.objects.get(giornata=id, username=avversario)
            p_avversario = formazione_avversario.p_totali
            user_punti = Moto_punti.objects.get(utente_id=utente)
            avv_punti = Moto_punti.objects.get(username=avversario)
            differenza_punti = p_totali - p_avversario
            # Sconfitta
            if p_totali < p_avversario:
                formazione_utente.risultato = 0
                formazione_avversario.risultato = 1
                avv_punti.p_scontri += 3
            # Vittoria
            elif p_totali > p_avversario:
                formazione_utente.risultato = 1
                formazione_avversario.risultato = 0
                user_punti.p_scontri += 3
            # Pareggio
            elif p_totali == p_avversario:
                formazione_utente.risultato = 2
                formazione_avversario.risultato = 2
                user_punti.p_scontri += 1
                avv_punti.p_scontri += 1
            user_punti.differenza += differenza_punti
            avv_punti.differenza -= differenza_punti
            user_punti.p_generali += p_totali
            avv_punti.p_generali += p_avversario
            formazione_avversario.save()
            user_punti.save()
            avv_punti.save()
        # Se non controllata aggiungi solo i tuoi punti
        except:
            pass
        formazione_utente.p_totali = p_totali
        formazione_utente.save()
        return HttpResponseRedirect(reverse("fantamoto/calcolo_scelta"))



################################### FORMULA 1/2 #######################################
@login_required
def formula_home(request):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    now = timezone.localtime()
    alldates = Formula_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    nextgara = Formula_giornata.objects.get(data=nextdate)
    return render(request, "fantaformula/home.html", {
        "nextgara": nextgara
    })


@login_required
def formula_classscontri(request):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    ranking = Formula_punti.objects.order_by("-p_scontri", "-differenza")
    return render(request, "fantaformula/classifica_scontri.html", {
        "ranking": ranking
    })


@login_required
def formula_classpunti(request):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    ranking = Formula_punti.objects.order_by("-p_generali", "-differenza")
    return render(request, "fantaformula/classifica_punti.html", {
        "ranking": ranking
    })


@login_required
def formula_rose(request):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    tutti = User.objects.order_by("username")
    formula_tutti = []
    for uno in tutti:
        if uno.id != 6 and uno.id != 9:
            formula_tutti.append(uno)
    return render(request, "fantaformula/rose_totali.html", {
        "tutti": formula_tutti
    })


@login_required
def formula_rosautente(request, utente):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    piloti = Formula_piloti.objects.filter(username=utente)
    teams = Formula_team.objects.filter(username=utente)
    tm = Formula_teammanager.objects.get(username=utente)
    return render(request, "fantaformula/rosa_utente.html", {
        "utente": utente,
        "piloti": piloti,
        "teams": teams,
        "tm": tm
    })


@login_required
def formula_cal_scelta(request):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    giornate = Formula_giornata.objects.all()
    return render(request, "fantaformula/calendario.html", {
        "giornate": giornate
    })


@login_required
def formula_calendario(request, id):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    giornata = Formula_giornata.objects.get(id=id)
    if id == "1" or id == "8" or id == "15" or id == "22":
        sfida1 = ["Zanno", "Cortez Black Team"]
        sfida2 = ["Tazza", "Vettel05"]
        sfida3 = ["Cicciobirro01", "Paul Bird Motorsport"]
        sfida4 = ["Dragon trainer", "Albwin27"]
    elif id == "2" or id == "9" or id == "16":
        sfida1 = ["Tazza", "Zanno"]
        sfida2 = ["Cortez Black Team", "Cicciobirro01"]
        sfida3 = ["Vettel05", "Dragon trainer"]
        sfida4 = ["Paul Bird Motorsport", "Albwin27"]
    elif id == "3" or id == "10" or id == "17":
        sfida1 = ["Zanno", "Vettel05"]
        sfida2 = ["Cortez Black Team", "Paul Bird Motorsport"]
        sfida3 = ["Albwin27", "Tazza"]
        sfida4 = ["Cicciobirro01", "Dragon trainer"]
    elif id == "4" or id == "11" or id == "18":
        sfida1 = ["Albwin27", "Zanno"]
        sfida2 = ["Dragon trainer", "Paul Bird Motorsport"]
        sfida3 = ["Vettel05", "Cicciobirro01"]
        sfida4 = ["Tazza", "Cortez Black Team"]
    elif id == "5" or id == "12" or id == "19":
        sfida1 = ["Zanno", "Dragon trainer"]
        sfida2 = ["Albwin27", "Cicciobirro01"]
        sfida3 = ["Paul Bird Motorsport", "Tazza"]
        sfida4 = ["Vettel05", "Cortez Black Team"]
    elif id == "6" or id == "13" or id == "20":
        sfida1 = ["Paul Bird Motorsport", "Zanno"]
        sfida2 = ["Albwin27", "Vettel05"]
        sfida3 = ["Dragon trainer", "Cortez Black Team"]
        sfida4 = ["Cicciobirro01", "Tazza"]
    elif id == "7" or id == "14" or id == "21":
        sfida1 = ["Zanno", "Cicciobirro01"]
        sfida2 = ["Dragon trainer", "Tazza"]
        sfida3 = ["Cortez Black Team", "Albwin27"]
        sfida4 = ["Paul Bird Motorsport", "Vettel05"]
    return render(request, "fantaformula/giornata.html", {
        "now_id": id,
        "giornata": giornata,
        "sfida1": sfida1,
        "sfida2": sfida2,
        "sfida3": sfida3,
        "sfida4": sfida4
    })


@login_required
def formula_scontro(request, id, scontro):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    sfida = scontro.replace("_", " - ")
    sfidante1 = scontro.split("_")[0]
    sfidante2 = scontro.split("_")[1]
    id_sfidante1 = User.objects.get(username=sfidante1).id
    id_sfidante2 = User.objects.get(username=sfidante2).id
    # Ottieni formazione primo user
    try:
        formazione1 = Formula_formazione.objects.get(utente_id=id_sfidante1, giornata=id)
    except:
        formazione1 = ""
    try:
        formazione2 = Formula_formazione.objects.get(utente_id=id_sfidante2, giornata=id)
    except:
        formazione2 = ""
    try:
        piloti1 = formazione1.piloti.all()
        teams1 = formazione1.team.all()
        tm1 = formazione1.teammanager.nome
    except:
        piloti1 = ""
        teams1 = ""
        tm1 = ""
    # Ottieni formazione secondo user
    try:
        piloti2 = formazione2.piloti.all()
        teams2 = formazione2.team.all()
        tm2 = formazione2.teammanager.nome
    except:
        piloti2 = ""
        teams2 = ""
        tm2 = ""
    return render(request, "fantaformula/risultato_scontro.html", {
        "now_id": id,
        "sfida": sfida,
        "formazione1": formazione1,
        "formazione2": formazione2,
        "piloti1": piloti1,
        "piloti2": piloti2,
        "teams1": teams1,
        "teams2": teams2,
        "tm1": tm1,
        "tm2": tm2
    })


@login_required
def formula_formazione(request):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    now = timezone.localtime()
    alldates = Formula_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    nextgara = Formula_giornata.objects.get(data=nextdate)
    piloti = Formula_piloti.objects.filter(utente_id=request.user.id)
    teams = Formula_team.objects.filter(utente_id=request.user.id)
    tm = Formula_teammanager.objects.get(utente_id=request.user.id)
    return render(request, "fantaformula/scelta_formazione.html", {
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "nextgara": nextgara
    })


@login_required
def formula_schieramento(request):
    no = [6, 9]
    if request.user.id in no:
        raise Exception("Non puoi acceedere al Fanta Formula")
    if request.method == "POST":
        # Trova prossima gara
        now = timezone.localtime()
        alldates = Formula_giornata.objects.values_list('data', flat=True)
        alldates = list(alldates)
        for date in alldates:
            date = timezone.localtime(date)
            if date > now:
                nextdate = date
                break
        nextgara = Formula_giornata.objects.get(data=nextdate)
        # Variabili
        categorie_piloti = []
        categorie_teams = []
        piloti = request.POST.getlist("piloti")
        teams = request.POST.getlist("teams")
        tm = request.POST.get("tm")
        # Se non c'è la MotoE
        if nextgara.f2 == 0:
            # Check numero piloti, teams e tm
            if len(piloti) != 2:
                raise ValidationError("Devi selezionare 2 piloti (NO F2), per rifare la formazione torna indietro")
            if len(teams) != 1:
                raise ValidationError("Devi selezionare un team (NO F2), per rifare la formazione torna indietro")
            if tm is None:
                raise ValidationError("Seleziona il team manager, per rifare la formazione torna indietro")
            # Check categoria piloti
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "F1" not in categorie_piloti or "F2" in categorie_piloti:
                raise ValidationError("Scegli 2 piloti in F1, no F2")
            # Check categoria teams
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "F1" not in categorie_teams or "F2" in categorie_teams:
                raise ValidationError("Scegli un team in F1, no F2")
        # Se c'è la MotoE
        elif nextgara.f2 == 1:
            if len(piloti) != 4:
                raise ValidationError("Devi selezionare 4 piloti (CON F2), per rifare la formazione torna indietro")
            if len(teams) != 2:
                raise ValidationError("Devi selezionare 2 team (CON F2), per rifare la formazione torna indietro")
            if tm is None:
                raise ValidationError("Seleziona il team manager, per rifare la formazione torna indietro")
            # Check categoria piloti
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "F1" not in categorie_piloti or "F2" not in categorie_piloti:
                raise ValidationError("Come fai a essere qui - piloti")
            # Check categoria teams
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "F1" not in categorie_teams or "F2" not in categorie_teams:
                raise ValidationError("Come fai a essere qui - teams")
        # La formazione non ha errori
        # Se formazione già schierata, sostituiscila con quella nuova
        if Formula_formazione.objects.filter(giornata=nextgara.id, username=request.user.username):
            Formula_formazione.objects.filter(giornata=nextgara.id, username=request.user.username).delete()
        # Variabili
        formazione_giornata = nextgara.id
        formazione_data = now
        formazione_piloti = []
        formazione_teams = []
        for pilota in piloti:
            p = pilota.split(" - ")[0]
            p_id = Formula_piloti.objects.get(nome=p)
            formazione_piloti.append(p_id)
        for team in teams:
            t = team.split(" - ")[0]
            t_id = Formula_team.objects.get(nome=t)
            formazione_teams.append(t_id)
        formazione_tm = Formula_teammanager.objects.get(nome=tm)
        formazione_user = request.user
        # Salva la formazione
        formazione = Formula_formazione.objects.create(
            giornata = formazione_giornata,
            data = formazione_data,
            teammanager = formazione_tm,
            username = request.user.username,
            utente = formazione_user)
        formazione.piloti.set(formazione_piloti)
        formazione.team.set(formazione_teams)
        formazione.save()
        return HttpResponseRedirect(reverse("fantaformula/home"))


@login_required
def formula_calcscelta(request):
    autorizzati = [1, 2, 3, 4]
    if request.user.id not in autorizzati:
        raise Exception("Non sei autorizzato ad accedere al calcolo giornate")
    giornate = Formula_giornata.objects.all()
    utenti = User.objects.all()
    formula_tutti = []
    for uno in utenti:
        if uno.id != 6 and uno.id != 9:
            formula_tutti.append(uno)
    return render(request, "fantaformula/calcolo_scelta.html", {
        "giornate": giornate,
        "utenti": formula_tutti
    })


@login_required
def formula_calcformazione(request, id, utente):
    autorizzati = [1, 2, 3, 4]
    if request.user.id not in autorizzati:
        raise Exception("Non sei autorizzato ad accedere al calcolo giornate")
    if id == "0" and utente == "0":
        raise Exception("Ricordati di selezionare una giornata e un utente")
    elif utente == "0":
        raise Exception("Ricordati di selezionare un utente")
    elif id == "0":
        raise Exception("Ricordati di selezionare una giornata")
    # Variabili
    user = User.objects.get(id=utente).username
    try:
        formazione = Formula_formazione.objects.get(utente_id=utente, giornata=id)
        piloti = formazione.piloti.all()
        teams = formazione.team.all()
        tm = formazione.teammanager
        calcolata = formazione.p_totali
    except:
        now = timezone.localtime()
        giornata = Formula_giornata.objects.get(id=id).data
        if now > giornata:
            formazione = Formula_formazione.objects.create(
                giornata = id,
                data = now,
                utente_id = utente,
                username = user
            ).save()
        else:
            raise Exception("La gara non è stata ancora disputata >:(")
        return render(request, "fantaformula/calcolo_formazione.html", {
            "id": id,
            "utente": utente,
            "user": user
        })
    return render(request, "fantaformula/calcolo_formazione.html", {
        "id": id,
        "utente": utente,
        "user": user,
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "calcolata": calcolata,
        "formazione": formazione
    })


@login_required
def formula_calctotale(request, id, utente):
    autorizzati = [1, 2, 3, 4]
    if request.user.id not in autorizzati:
        raise Exception("Non sei autorizzato ad accedere al calcolo giornate")
    if request.method == "POST":
        # Calcola il punteggio totale
        p_piloti = request.POST.getlist("p_piloti")
        p_teams = request.POST.getlist("p_teams")
        p_tm = request.POST.get("p_tm")
        p_totali = 0
        for uno in p_piloti:
            p_totali += int(uno)
        for uno in p_teams:
            p_totali += int(uno)
        p_totali += int(p_tm)
        # Controlla chi è l'avversario
        user = User.objects.get(id=utente).username
        if id == "1" or id == "8" or id == "15" or id == "22":
            sfide = [["Zanno", "Cortez Black Team"], ["Tazza", "Vettel05"], ["Cicciobirro01", "Paul Bird Motorsport"], 
            ["Dragon trainer", "Albwin27"]]
        elif id == "2" or id == "9" or id == "16":
            sfide = [["Tazza", "Zanno"], ["Cortez Black Team", "Cicciobirro01"], ["Vettel05", "Dragon trainer"], 
            ["Paul Bird Motorsport", "Albwin27"]]
        elif id == "3" or id == "10" or id == "17":
            sfide = [["Zanno", "Vettel05"], ["Cortez Balck Team", "Paul Bird Motorsport"], ["Albwin27", "Tazza"], 
            ["Cicciobirro01", "Dragon trainer"]]
        elif id == "4" or id == "11" or id == "18":
            sfide = [["Albwin27", "Zanno"], ["Dragon trainer", "Paul Bird Motorsport"], ["Vettel05", "Cicciobirro01"], 
            ["Tazza", "Cortez Black Team"]]
        elif id == "5" or id == "12" or id == "19":
            sfide = [["Zanno", "Dragon trainer"], ["Albwin27", "Cicciobirro01"], ["Paul Bird Motorsport", "Tazza"], 
            ["Vettel05", "Cortez Black Team"]]
        elif id == "6" or id == "13" or id == "20":
            sfide = [["Paul Bird Motorsport", "Zanno"], ["Albwin27", "Vettel05"], ["Dragon trainer", "Cortez Black Team"], 
            ["Cicciobirro01", "Tazza"]]
        elif id == "7" or id == "14" or id == "21":
            sfide = [["Zanno", "Cicciobirro01"], ["Dragon trainer", "Tazza"], ["Cortez Black Team", "Albwin27"], 
            ["Paul Bird Motorsport", "Vettel05"]]
        for i in range(4):
            if user in sfide[i]:
                sfide[i].remove(user)
                avversario = sfide[i][0]
        # Variabili
        formazione_utente = Formula_formazione.objects.get(giornata=id, utente_id=utente)
        user_punti = Formula_punti.objects.get(utente_id=utente)
        avv_punti = Formula_punti.objects.get(username=avversario)
        # Se formazione avversaria già controllata aggiungi il risultato dello scontro
        try:
            formazione_avversario = Formula_formazione.objects.get(giornata=id, username=avversario)
            p_avversario = formazione_avversario.p_totali
            user_punti = Formula_punti.objects.get(utente_id=utente)
            avv_punti = Formula_punti.objects.get(username=avversario)
            differenza_punti = p_totali - p_avversario
            # Sconfitta
            if p_totali < p_avversario:
                formazione_utente.risultato = 0
                formazione_avversario.risultato = 1
                avv_punti.p_scontri += 3
            # Vittoria
            elif p_totali > p_avversario:
                formazione_utente.risultato = 1
                formazione_avversario.risultato = 0
                user_punti.p_scontri += 3
            # Pareggio
            elif p_totali == p_avversario:
                formazione_utente.risultato = 2
                formazione_avversario.risultato = 2
                user_punti.p_scontri += 1
                avv_punti.p_scontri += 1
            user_punti.differenza += differenza_punti
            avv_punti.differenza -= differenza_punti
            user_punti.p_generali += p_totali
            avv_punti.p_generali += p_avversario
            formazione_avversario.save()
            user_punti.save()
            avv_punti.save()
        # Se non controllata aggiungi solo i tuoi punti
        except:
            pass
        formazione_utente.p_totali = p_totali
        formazione_utente.save()
        return HttpResponseRedirect(reverse("fantaformula/calcolo_scelta"))
