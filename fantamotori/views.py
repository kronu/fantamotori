# Tutto il backend del sito, con le funzioni che verranno chiamate ad ogni azione degli utenti
# Simula Pagina Web con "python manage.py runserver"
# Termina simulazione con Ctrl+C nel terminale
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from datetime import datetime

from .models import Moto_giornata, Moto_formazione, Moto_piloti, Moto_punti, Moto_team, Moto_teammanager, Moto_scontri, User
from .models import Formula_giornata, Formula_formazione, Formula_piloti, Formula_punti, Formula_team, Formula_teammanager, Formula_scontri


def register(request):
    if request.user.id != 1:
        return render(request, "errore.html", {
            "message": "Non puoi creare altri profili",
            "cat": ""
        })
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
    messages.warning(request, "Effetturato il logout.")
    return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if User.objects.get(username=username).rimosso:
            return render(request, "errore.html", {
                "message": "Sei stato rimosso dal Fanta. Se credi che sia un errore contattami."
            })
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Username e/o password non corrette"
            })
    return render(request, "login.html")


@login_required
def scelta(request):
    return render(request, "index.html")


@login_required
def utente(request):
    if request.method == "POST":
        u = User.objects.get(username=request.user.username)
        if "changepassword" in request.POST:
            if u.check_password(request.POST["oldpassword"]):
                if request.POST["newpassword"] != "":
                    u.set_password(request.POST["newpassword"])
                    u.save()
                    return render(request, "utente.html", {
                        "message": "Modifiche salvate ;)"
                    })
                else:
                    return render(request, "utente.html", {
                        "message": "Inserisci una password valida."
                    })
            else:
                return render(request, "utente.html", {
                    "message": "La vecchia password non coincide con l'attuale password.",
                })
        elif "changeimg" in request.POST:
            u.immagine = request.POST["urlimmagine"]
            u.save()
            return render(request, "utente.html", {
                "message": "Immagine aggiornata."
            })
    return render(request, "utente.html", {
        "utente": request.user,
    })


def check_moto(request):
    if request.user.fanta != 0 and request.user.fanta != 1:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaMoto.",
            "cat": "moto"
        })
    

def check_formula(request):
    if request.user.fanta != 0 and request.user.fanta != 2:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })


def check_admin(request, categoria):
    autorizzati = ["Tazza", "Albwin27", "Cortez Black Team", "Cicciobirro01"]
    if request.user.username not in autorizzati:
        return render(request, "errore.html", {
            "message": "Non sei un admin. Se credi sia un errore contattami.",
            "cat": categoria,
        })


################################################################ MOTO ##########################################################################
@login_required
def moto_home(request):
    check_moto(request)
    now = timezone.localtime()
    alldates = Moto_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    # Cerca prossima gara, se finite, ritorna None
    try:
        nextgara = Moto_giornata.objects.get(data=nextdate)
    except:
        nextgara = None
    # Cerca ultimo risultato, se prima gara, ritorna None
    try:
        dataultimagara = max(data for data in alldates if data < now)
        ultimagara = Moto_giornata.objects.get(data=dataultimagara)
    except:
        ultimagara = None
        previousgara = None
    if ultimagara:
        try:
            previousgara = Moto_formazione.objects.get(giornata=ultimagara.id, username=request.user.username)
        except:
            previousgara = None
    # Ritorna posizioni in classifica
    s_ranking = Moto_punti.objects.order_by("-p_scontri", "-differenza")
    p_ranking = Moto_punti.objects.order_by("-p_generali", "-differenza")
    # Cerca se hai schierato la formazione per la prossima gara
    try:
        schierata = Moto_formazione.objects.get(giornata=nextgara.id, username=request.user)
    except:
        schierata = None
    # Categorie prossima giornata
    if nextgara:
        listacat = []
        for cat in nextgara.categ.split(","):
            match(cat):
                case "gp": listacat.append("MotoGP")
                case "2": listacat.append("Moto2")
                case "3": listacat.append("Moto3")
                case "e": listacat.append("MotoE")
                case "sbk": listacat.append("SBK")
    else:
        listacat = None
    return render(request, "fantamoto/home.html", {
        "utente": request.user,
        "ultimagara": ultimagara,
        "previousgara": previousgara,
        "nextgara": nextgara,
        "s_ranking": s_ranking,
        "p_ranking": p_ranking,
        "schierata": schierata,
        "listacat": listacat,
        "cat": "moto"
    })


@login_required
def moto_rose(request):
    check_moto(request)
    lista_utenti = []
    for utenti in User.objects.order_by("username"):
        if utenti.fanta != 2:
            lista_utenti.append(utenti)
    return render(request, "fantamoto/rose.html", {
        "tutti": lista_utenti,
        "cat": "moto"
    })


@login_required
def moto_rosautente(request, utente):
    check_moto(request)
    piloti = Moto_piloti.objects.filter(username=utente)
    teams = Moto_team.objects.filter(username=utente)
    tm = Moto_teammanager.objects.get(username=utente)
    return render(request, "fantamoto/rosa_utente.html", {
        "utente": utente,
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "cat": "moto"
    })


@login_required
def moto_calendario(request):
    check_moto(request)
    giornate = Moto_giornata.objects.all()
    now = timezone.localtime()
    alldates = Moto_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    # Se prima giornata
    if now < Moto_giornata.objects.get(id=1).data:
        ultimagara = 1
    # Se altre giornate
    else:    
        dataultimagara = max(data for data in alldates if data < now)
        ultimagara = Moto_giornata.objects.get(data=dataultimagara).id
    # Distingui giornate e scontri
    all_id = []
    all_sfide = []
    for sfida in Moto_scontri.objects.all():
        all_id.append(sfida.giornata)
        scontri_lista = []
        scontri = sfida.scontri.split("/")
        for scontro in scontri:
            scontro = scontro.split("+")
            scontri_lista.append(scontro)
        all_sfide.append(scontri_lista)
    lista_utenti = []
    for utenti in User.objects.order_by("username"):
        if utenti.fanta != 2:
            lista_utenti.append(utenti)
    return render(request, "fantamoto/calendario.html", {
        "giornate": giornate,
        "ultima": ultimagara,
        "sfide": all_sfide,
        "tutti": lista_utenti,
        "cat": "moto"
    })


@login_required
def moto_scontro(request, id, scontro):
    check_moto(request)
    posto = Moto_giornata.objects.get(id=id).posto
    # Separa i nomi nella sfida e ottieni gli utente_id
    sfidante1, sfidante2 = scontro.split("-")
    id_sfidante1 = User.objects.get(username=sfidante1).id
    id_sfidante2 = User.objects.get(username=sfidante2).id
    # Cerca se le formazioni sono state schierate
    try:
        formazione1 = Moto_formazione.objects.get(utente_id=id_sfidante1, giornata=id)
    except:
        formazione1 = None
    try:
        formazione2 = Moto_formazione.objects.get(utente_id=id_sfidante2, giornata=id)
    except:
        formazione2 = None
    # Numero gara
    if int(id) < 10:
        numerogara = f"gara0{id}"
    else:
        numerogara = f"gara{id}"
    # Ottieni formazione primo user
    try:
        piloti1 = formazione1.piloti.all()
        teams1 = formazione1.team.all()
        if Moto_giornata.objects.get(id=id).categ.count(",") != 1:
            tm1 = formazione1.teammanager.nome
        else:
            tm1 = None
        # Se la formazione è già stata calcolata, carica i punti ottenuti da piloti,team, tm
        # Seleziona i punteggi da Moto_piloti e consegnali in una lista
        punti_piloti1 = []
        for pilota1 in piloti1:
            punti_pilota1 = getattr(Moto_piloti.objects.get(nome=pilota1.nome), numerogara)
            if punti_pilota1 or punti_pilota1 == 0:
                punti_piloti1.append(punti_pilota1)
        # Seleziona punti dei team
        punti_teams1 = []
        for team1 in teams1:
            punti_team1 = getattr(Moto_team.objects.get(nome=team1.nome), numerogara)
            if punti_team1 or punti_team1 == 0:
                punti_teams1.append(punti_team1)
        # E del team manager
        if Moto_giornata.objects.get(id=id).categ.count(",") != 1:
            punti_tm1 = getattr(Moto_teammanager.objects.get(nome=tm1), numerogara)
        else:
            punti_tm1 = None
        # Se risultati ancora vuoti, non mostrare nulla
        if punti_piloti1 == [] and punti_teams1 == [] and punti_tm1 is None:
            punti_piloti1 = None
            punti_teams1 = None
    # Formazione non è stata schierata
    except:
        piloti1 = None
        teams1 = None
        tm1 = None
        punti_piloti1 = None
        punti_teams1 = None
        punti_tm1 = None
    # Cerca se il capitano è stato schierato
    try:
        capitano1 = formazione1.capitano.nome
    except:
        capitano1 = None
    # Cerca che gara del capitano
    try:
        if not formazione1.cap_gara:
            garacap1 = ""
        else:
            garacap1 = formazione1.cap_gara
    except:
        garacap1 = None
    # Secondo utente
    # Se formazione è schierata
    try:
        piloti2 = formazione2.piloti.all()
        teams2 = formazione2.team.all()
        if Moto_giornata.objects.get(id=id).categ.count(",") != 1:
            tm2 = formazione2.teammanager.nome
        else:
            tm2 = None
        # Piloti
        punti_piloti2 = []
        for pilota2 in piloti2:
            punti_pilota2 = getattr(Moto_piloti.objects.get(nome=pilota2.nome), numerogara)
            if punti_pilota2 or punti_pilota2 == 0:
                punti_piloti2.append(punti_pilota2)
        # Team
        punti_teams2 = []
        for team2 in teams2:
            punti_team2 = getattr(Moto_team.objects.get(nome=team2.nome), numerogara)
            if punti_team2 or punti_team2 == 0:
                punti_teams2.append(punti_team2)
        # Team Manager
        if Moto_giornata.objects.get(id=id).categ.count(",") != 1:
            punti_tm2 = getattr(Moto_teammanager.objects.get(nome=tm2), numerogara)
        else:
            punti_tm2 = None
        # Non mostrare nulla se vuoto
        if punti_piloti2 == [] and punti_teams2 == [] and punti_tm2 is None:
            punti_piloti2 = None
            punti_teams2 = None
    # Formazione non schierata
    except:
        piloti2 = None
        teams2 = None
        tm2 = None
        punti_piloti2 = None
        punti_teams2 = None
        punti_tm2 = None
    # Capitano
    try:
        capitano2 = formazione2.capitano.nome
    except:
        capitano2 = None
    # Gara capitano
    try:
        if formazione2.cap_gara is None:
            garacap2 = ""
        else:
            garacap2 = formazione2.cap_gara
    except:
        garacap2 = None
    return render(request, "fantamoto/risultato.html", {
        "id": id,
        "posto": posto,
        "s1": sfidante1,
        "s2": sfidante2,
        "formazione1": formazione1,
        "formazione2": formazione2,
        "piloti1": piloti1,
        "piloti2": piloti2,
        "teams1": teams1,
        "teams2": teams2,
        "tm1": tm1,
        "tm2": tm2,
        "capitano1": capitano1,
        "capitano2": capitano2,
        "garacap1": garacap1,
        "garacap2": garacap2,
        "punti_piloti1": punti_piloti1,
        "punti_teams1": punti_teams1,
        "punti_tm1": punti_tm1,
        "punti_piloti2": punti_piloti2,
        "punti_teams2": punti_teams2,
        "punti_tm2": punti_tm2,
        "cat": "moto"
    })


@login_required
def moto_albo(request):
    check_moto(request)
    return render(request, "fantamoto/albodoro.html", {"cat": "moto"})


@login_required
def moto_formazione(request):
    check_moto(request)
    # Ottieni prossima giornata
    now = timezone.localtime()
    alldates = Moto_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    nextgara = Moto_giornata.objects.get(data=nextdate)
    # Seleziona piloti, team e tm disponibili
    piloti = Moto_piloti.objects.filter(username=request.user.username)
    teams = Moto_team.objects.filter(username=request.user.username)
    tm = Moto_teammanager.objects.get(username=request.user.username)
    # Ottieni gli ultimi tre risultati
    ultime = [nextgara.id - 1, nextgara.id - 2, nextgara.id - 3]
    # Non prendere id giornate negativo o zero
    for i in range(3):
        if ultime[i] == 0 or ultime[i] < 0:
            ultime[i] = 0
    # Punti piloti ultime 3 giornate
    punti_piloti = []
    for pilota in piloti:
        punti_pilota = []
        for giornata in ultime:
            try:
                # Ottieni ultime tre giornate
                if giornata < 10:
                    numerogara = f"gara0{giornata}"
                else:
                    numerogara = f"gara{giornata}"
                punti_g = getattr(Moto_piloti.objects.get(nome=pilota.nome), numerogara)
                punti_pilota.append(punti_g)
            except:
                punti_pilota.append("-")
        # Aggiungi pilota ai piloti
        punti_piloti.append(punti_pilota)
    # Ripeti per i team
    punti_teams = []
    for team in teams:
        punti_team = []
        for giornata in ultime:
            try:
                # Ottieni ultime tre giornate
                if giornata < 10:
                    numerogara = f"gara0{giornata}"
                else:
                    numerogara = f"gara{giornata}"
                punti_g = getattr(Moto_team.objects.get(nome=team.nome), numerogara)
                punti_team.append(punti_g)
            except:
                punti_team.append("-")
        # Aggiungi team ai teams
        punti_teams.append(punti_team)
    # Ripeti per team manager
    punti_tm = []
    for giornata in ultime:
        try:
            # Ottieni ultime tre giornate
            if giornata < 10:
                numerogara = f"gara0{giornata}"
            else:
                numerogara = f"gara{giornata}"
            punti_g = getattr(Moto_teammanager.objects.get(nome=tm.nome), numerogara)
            punti_tm.append(punti_g)
        except:
            punti_tm.append("-")
    # Trova categorie nella prossima giornata
    numcategorie = nextgara.categ.count(",")
    listacat = []
    for cat in nextgara.categ.split(","):
        match(cat):
            case "gp": listacat.append("MotoGP")
            case "2": listacat.append("Moto2")
            case "3": listacat.append("Moto3")
            case "e": listacat.append("MotoE")
            case "sbk": listacat.append("SBK")
    return render(request, "fantamoto/formazione.html", {
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "nextgara": nextgara,
        "punti_piloti": punti_piloti,
        "punti_teams": punti_teams,
        "punti_tm": punti_tm,
        "numcategorie": numcategorie,
        "listacat": listacat,
        "cat": "moto"
    })


@login_required
def moto_schieramento(request):
    check_moto(request)
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
        gara1 = request.POST.get("gara1")
        gara2 = request.POST.get("gara2")
        # Controlla capitano
        for pilota in piloti:
            check_capitano.append(pilota.split(" - ")[0])
        if capitano not in check_capitano and capitano != "0":
            message = "FORMAZIONE NON SCHIERATA: CAPITANO SELEZIONATO NON PRESENTE NELLA FORMAZIONE"
        elif capitano in check_capitano:
            pilotacapitano = Moto_piloti.objects.get(nome=capitano)
            if pilotacapitano.categoria == "MotoE" or pilotacapitano.categoria == "SBK":
                if gara1 is None and gara2 is None:
                    message = "FORMAZIONE NON SCHIERATA: GARA LUNGA NON SPECIFICATA CON PILOTA IN MotoE O SBK"
        # Controlla numero giusto piloti e team per categorie della prossima gara
        numcategorie = nextgara.categ.count(",")
        if tm is None and numcategorie != 1:
            message = "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM MANAGER"
        if numcategorie == 1:
            if len(piloti) != 2:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 2 PILOTI"
            elif len(teams) != 1:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM"
        elif numcategorie == 2:
            message = "FORMAZIONE NON SCHIERATA: NUMERO DI CATEGORIE IMPOSSIBILE"
        elif numcategorie == 3:
            if len(piloti) != 6:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 6 PILOTI"
            elif len(teams) != 3:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 3 TEAM"
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA UN PILOTA DI OGNI CATEGORIA"
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI OGNI CATEGORIA"
        elif numcategorie == 4:
            if len(piloti) != 7:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 7 PILOTI"
            elif len(teams) != 4:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 4 TEAM"
            if "e" in nextgara.categ:
                extracat = "MotoE"
            else:
                extracat = "SBK"
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti or extracat not in categorie_piloti:
                message = f"FORMAZIONE NON SCHIERATA: SELEZIONA UN PILOTA DI OGNI CATEGORIA (con {extracat})"
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams or extracat not in categorie_teams:
                message = f"FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI OGNI CATEGORIA (con {extracat})"
        elif numcategorie == 5:
            if len(piloti) != 8:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 8 PILOTI"
            elif len(teams) != 5:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 5 TEAM"
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti or "MotoE" not in categorie_piloti or "SBK" not in categorie_piloti:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA UN PILOTA DI OGNI CATEGORIA"
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams or "MotoE" not in categorie_teams or "SBK" not in categorie_teams:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI OGNI CATEGORIA"
        try:
            if message:
                return render(request, "errore.html", {"cat": "moto", "message": message})
        except:
            pass
        
        # Se arrivati fin qui, la formazione non presenta errori
        # Se una formazione è già stata schierata, elimina la vecchia
        if Moto_formazione.objects.filter(giornata=nextgara.id, username=request.user.username):
            Moto_formazione.objects.filter(giornata=nextgara.id, username=request.user.username).delete()
        # Variabili da inserire nell'oggetto Moto_formazione
        formazione_giornata = nextgara.id
        formazione_data = now
        formazione_piloti = []
        formazione_teams = []
        # Trova l'id dei piloti e dei team scelti
        for pilota in piloti:
            p = pilota.split(" - ")[0]
            p_id = Moto_piloti.objects.get(nome=p)
            formazione_piloti.append(p_id)
        for team in teams:
            t = team.split(" - ")[0]
            t_id = Moto_team.objects.get(nome=t)
            formazione_teams.append(t_id)
        try:
            formazione_tm = Moto_teammanager.objects.get(nome=tm)
        except:
            formazione_tm = None
        formazione_user = request.user
        # Seleziona il capitano (oppure trascuralo)
        if capitano != "0":
            formazione_capitano = Moto_piloti.objects.get(nome=capitano)
            if formazione_capitano.categoria == "Moto3" or formazione_capitano.categoria == "Moto2" or formazione_capitano.categoria == "MotoGP":
                garacap = 1
            elif formazione_capitano.categoria == "MotoE" or formazione_capitano.categoria == "SBK":
                garacap = 1 if gara1 else 2
        else:
            formazione_capitano = None
            garacap = None
        # Salva la formazione nel database
        formazione = Moto_formazione.objects.create(
            giornata = formazione_giornata,
            data = formazione_data,
            teammanager = formazione_tm,
            username = request.user.username,
            utente = formazione_user,
            capitano = formazione_capitano,
            cap_gara = garacap)
        formazione.piloti.set(formazione_piloti)
        formazione.team.set(formazione_teams)
        formazione.save()
        # Rispedisci alla home
        messages.success(request, 'Formazione schierata!')
        return HttpResponseRedirect("../fantamoto")


@login_required
def moto_calcoloscelta(request):
    check_moto(request)
    check_admin(request, "moto")
    giornate = Moto_giornata.objects.all()
    return render(request, "fantamoto/calcolo_scelta.html", {
        "giornate": giornate,
        "cat": "moto"
    })


@login_required
def moto_admpiloti(request):
    check_moto(request)
    check_admin(request, "moto")
    # Lista piloti moto
    moto_listapiloti = []
    moto_allpilotilista = Moto_piloti.objects.all().values("nome")
    for moto_pilotalista in moto_allpilotilista:
        moto_listapiloti.append(moto_pilotalista["nome"])
    # Cambia nome al pilota e aggiungi "ex (vecchionome)"
    if request.method == "POST":
        pilota = Moto_piloti.objects.get(nome=request.POST.get("oldname"))
        nome = f"{request.POST.get('newname')} (ex {pilota.nome})"
        pilota.nome = nome
        pilota.save()
    return render(request, "fantamoto/adm_piloti.html", {
        "cat": "moto",
        "listapiloti": moto_listapiloti
    })
    

@login_required
def moto_admteam(request):
    check_moto(request)
    check_admin(request, "moto")
    # Lista piloti moto
    moto_listapiloti = []
    moto_allpilotilista = Moto_piloti.objects.all().values("nome")
    for moto_pilotalista in moto_allpilotilista:
        moto_listapiloti.append(moto_pilotalista["nome"])
    # Sostituisci oldpilota dal team selezionato con newpilota
    if request.method == "POST":
        team = request.POST["team"]
        old = Moto_piloti.objects.get(nome=request.POST["oldpilota"])
        new = Moto_piloti.objects.get(nome=request.POST["newpilota"])
        if old.team != team:
            return render(request, "errore.html", {
                "message": f"{old.nome} non è un pilota del team {team}",
                "cat": "moto"
            })
        old.team = None
        new.team = team
        old.save()
        new.save()
    return render(request, "fantamoto/adm_team.html", {
        "cat": "moto",
        "teams": Moto_team.objects.all(),
        "listapiloti": moto_listapiloti
    })


@login_required
def moto_admgara(request):
    check_moto(request)
    check_admin(request, "moto")
    if request.method == "POST":
        gara = Moto_giornata.objects.get(posto=request.POST["gara"])
        if request.POST["annullata"] == "1":
            gara.annullata = 1
            gara.save()
        else:
            # Nome
            if request.POST["nome"] != "":
                gara.posto = request.POST["nome"]
            # Cambia categorie gara
            categorie = ""
            if request.POST.get("MotoGP") != "":
                categorie += "gp,"
            if request.POST.get("Moto2") != "":
                categorie += "2,"
            if request.POST.get("Moto3") != "":
                categorie += "3,"
            if request.POST.get("MotoE") != "":
                categorie += "e,"
            if request.POST.get("SBK") != "":
                categorie += "sbk,"
            gara.categ = categorie
            # Orario
            if request.POST["orario"] != "":
                orario = request.POST["orario"].replace("T", " ")
                orario += ":00"
                orario = datetime.strptime(orario, "%Y-%m-%d %H:%M:%S")
                gara.data = orario
            gara.save()
    return render(request, "fantamoto/adm_gara.html", {
        "cat": "moto",
        "gare": Moto_giornata.objects.all()
    })


@login_required
def moto_calcologara(request, id):
    check_moto(request)
    check_admin(request, "moto")
    # Se si sta facendo una richiesta POST, calcola i risultati
    if request.method == "POST":
        if Moto_giornata.objects.get(id=id).calcolata:
            return render(request, "errore.html", {
                "message": "HAI GIÀ CALCOLATO QUESTA GIORNATA ._.",
                "cat": "moto"
            })
        # Ottieni tutte le formazioni (se non schierata, creane una vuota)
        formazioni = []
        for user in User.objects.all():
            if user.fanta != 2:
                try:
                    formazione = Moto_formazione.objects.get(username=user.username, giornata=id)
                except:
                    formazione = Moto_formazione.objects.create(
                        giornata = id,
                        data = timezone.localtime(),
                        username = user.username,
                        utente = user)
                    formazione.save()
                formazioni.append(formazione)
        # Distingui le info ricevute da POST e controlla se errori
        categorie = Moto_giornata.objects.get(id=id).categ
        contr_quali = []
        for cat in categorie.split(","):
            if cat == "gp":
                contr_spr = []
                contr_gp = []
                contr_flspr = 0
                contr_flfeat = 0
            elif cat == "2": 
                contr_2 = []
                contr_2fl = 0
            elif cat == "3":
                contr_3 = []
                contr_3fl = 0
            elif cat == "e":
                contr_eg1 = []
                contr_eg2 = []
                contr_efl1 = 0
                contr_efl2 = 0
            elif cat == "sbk":
                contr_sbkg1 = []
                contr_sbkg2 = []
                contr_sbksuper = []
                contr_sbkfl1 = 0
                contr_sbkfl2 = 0
        for key, value in request.POST.items():
            # Errori Qualifiche
            if "-q1" in key or "-q2" in key or "-q3" in key:
                if value != "":
                    temp_cate = key.split("-")[0]
                    contr_cate_pilota = Moto_piloti.objects.get(nome=value).categoria
                    if temp_cate == "gp" and contr_cate_pilota != "MotoGP": 
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    elif temp_cate == "2" and contr_cate_pilota != "Moto2":
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    elif temp_cate == "3" and contr_cate_pilota != "Moto3":
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    elif temp_cate == "e" and contr_cate_pilota != "MotoE":
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    elif temp_cate == "sbk" and contr_cate_pilota != "SBK":
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    if value not in contr_quali:
                        contr_quali.append(value)
                    else:
                        message = "CALCOLO ANNULLATO: UN PILOTA E' PRESENTE PIU' VOLTE NELLE QUALIFICHE"
                else:
                    message = "CALCOLO ANNULLATO: IN UNA QUALIFICA NON E' STATO SPECIFICATO UN PILOTA"
            # Errori Gare
            elif "-spr-" in key:
                if value not in contr_spr and value != "":
                    contr_quali.append(value)
                elif value in contr_spr:
                    message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (SPRINT MOTOGP)"
            elif "-feat-" in key:
                if "gp-" in key:
                    if value not in contr_gp and value != "":
                        contr_gp.append(value)
                    elif value in contr_gp:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (FEATURE MOTOGP)"
                elif "2-" in key:
                    if value not in contr_2 and value != "":
                        contr_2.append(value)
                    elif value in contr_2:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (FEATURE MOTO2)"
                elif "3-" in key:
                    if value not in contr_3 and value != "":
                        contr_3.append(value)
                    elif value in contr_3:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (FEATURE MOTO3)"
            elif "-g1-" in key:
                if "e-" in key:
                    if value not in contr_eg1 and value != "":
                        contr_eg1.append(value)
                    elif value in contr_eg1:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (GARA1 MOTOE)"
                elif "sbk-" in key:
                    if value not in contr_sbkg1 and value != "":
                        contr_sbkg1.append(value)
                    elif value in contr_sbkg1:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (GARA1 SBK)"
            elif "-g2-" in key:
                if "e-" in key:
                    if value not in contr_eg2 and value != "":
                        contr_eg2.append(value)
                    elif value in contr_eg2:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (GARA2 MOTOE)"
                elif "sbk-" in key:
                    if value not in contr_sbkg2 and value != "":
                        contr_sbkg2.append(value)
                    elif value in contr_sbkg2:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (GARA2 SBK)"
            elif "-super-" in key:
                if value not in contr_sbksuper and value != "":
                    contr_sbksuper.append(value)
                elif value in contr_sbksuper:
                    message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (SUPERPOLE SBK)"
            # Errori Fast Lap
            elif "-fl-" in key:
                if "2-" in key:
                    contr_2fl += 1
                elif "3-" in key:
                    contr_3fl += 1
            elif "-flspr-" in key:
                contr_flspr += 1
            elif "-flfeat-" in key:
                contr_flfeat += 1
            elif "-flg1-" in key:
                if "e-" in key:
                    contr_efl1 += 1
                elif "sbk-" in key:
                    contr_sbkfl1 += 1
            elif "-flg2-" in key:
                if "e-" in key:
                    contr_efl2 += 1
                elif "sbk-" in key:
                    contr_sbkfl2 += 1
        for cat in categorie.split(","):
            if cat == "gp":
                if contr_flspr != 1 or contr_flfeat != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (MOTOGP)"
            elif cat == "2":
                if contr_2fl != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (MOTO2)"
            elif cat == "3":
                if contr_3fl != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (MOTO3)"
            elif cat == "e":
                if contr_efl1 != 1 or contr_efl2 != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (MOTOE)"
            elif cat == "sbk":
                if contr_sbkfl1 != 1 or contr_sbkfl2 != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (SBK)"
        try:
            return render(request, "errore.html", {"cat": "moto", "message": message})
        except:
            print("Nessun errore")
        
        # Definiamo punteggi gare e helpers
        punti_sprint = {"1": 12, "2": 9, "3": 7, "4": 6, "5": 5, "6": 4, "7": 3, "8": 2, "9": 1}
        punti_gare = {"1": 25, "2": 20, "3": 16, "4": 13, "5": 11, "6": 10, "7": 9, "8": 8, "9": 7, "10": 6, "11": 5, "12": 4, "13": 3, "14": 2, "15": 1}
        punti_pen = {"ll": 3, "dp": 2, "js": 2, "dt": 3}
        if int(id) < 10:
            numerogara = f"gara0{id}"
        else:
            numerogara = f"gara{id}"
        zonaout = {"spr": 9, "feat": 15}
        contr_pen = []
        contr_squalifica = []
        # Cerca capitani schierati
        capitani = []
        for formazione in Moto_formazione.objects.filter(giornata=id):
            if formazione.capitano:
                pil_capitano = Moto_piloti.objects.get(nome=formazione.capitano.nome)
                garacap = formazione.cap_gara
                capitani.append(dict(nome=pil_capitano.nome, gara=garacap, risultato=""))
        # Iniziamo a calcolare piloti e team
        for key, value in request.POST.items():
            # Gare
            if "-spr-" in key or "-feat-" in key or "-g1-" in key or "-g2-" in key or "-super-" in key:
                # Calcolo punteggio team qui tra le gare se no prenderebbero i bonus piloti
                pilota = Moto_piloti.objects.get(nome=key.split("-")[2])
                team = Moto_team.objects.get(nome=pilota.team.nome)
                qualegara = "spr" if "-spr-" in key or "-super-" in key else "feat"
                if value != "" and int(value) <= zonaout[qualegara]:
                    # Controlla se capitano (bonus da assegnare alla fine)
                    for capitano in capitani:
                        if pilota.nome == capitano["nome"]:
                            if ("-feat-" in key or "-g1-" in key) and capitano["gara"] == 1:
                                capitano["risultato"] = value
                            elif "-g2-" in key and capitano["gara"] == 2:
                                capitano["risultato"] = value
                    # Continua con punti piloti e team
                    già_ppunti = getattr(pilota, numerogara)
                    già_tpunti = getattr(team, numerogara)
                    if già_ppunti is None:
                        già_ppunti = 0
                    if già_tpunti is None:
                        già_tpunti = 0
                    if "-spr-" in key or "-super-" in key:
                        già_ppunti += punti_sprint[value]
                        già_tpunti += punti_sprint[value]
                    else:
                        già_ppunti += punti_gare[value]
                        già_tpunti += punti_gare[value]
                    setattr(pilota, numerogara, già_ppunti)
                    setattr(team, numerogara, già_tpunti)
                    pilota.save()
                    team.save()
            # Qualifiche
            if "-q1" in key or "-q2" in key or "-q3" in key:
                if value != "":
                    pilota = Moto_piloti.objects.get(nome=value)
                    posiz_quali = key.split("-")[1]
                    già_punti = getattr(pilota, numerogara)
                    if già_punti is None:
                        già_punti = 0
                    match posiz_quali:
                        case "q1": già_punti += 5
                        case "q2": già_punti += 3
                        case "q3": già_punti += 1
                    setattr(pilota, numerogara, già_punti)
                    pilota.save()
            # Fast Lap
            if "-flspr-" in key or "-flfeat-" in key or "-fl-" in key or "-flg1-" in key or "-flg2-" in key:
                if value == "on":
                    pilota = Moto_piloti.objects.get(nome=key.split("-")[2])
                    già_punti = getattr(pilota, numerogara)
                    if già_punti is None:
                        già_punti = 0
                    già_punti += 2
                    setattr(pilota, numerogara, già_punti)
                    pilota.save()
            # Ricordi delle penalità per dopo
            if "-ll-" in key or "-dp-" in key or "-js-" in key or "-dt-" in key:
                if value != "":
                    contr_pen.append(dict(nome=key.split("-")[2], tipo=key.split("-")[1], molt=value))
        # Ora i team manager (qui non prenderanno le penalità del team, potrebbero ottenere risultati negativi / 2)
        for tm in Moto_teammanager.objects.all():
            corrisp_team = Moto_team.objects.get(nome=tm.team.nome)
            punti_team = getattr(corrisp_team, numerogara)
            if punti_team is None:
                punti_team = 0
            punti_tm = int(punti_team / 2)
            setattr(tm, numerogara, punti_tm)
            tm.save()
        # Penalità
        for penalità in contr_pen:
            pilota = Moto_piloti.objects.get(nome=penalità["nome"])
            team = Moto_team.objects.get(nome=pilota.team.nome)
            punti_team = getattr(team, numerogara)
            if punti_team is None:
                punti_team = 0
            if penalità["tipo"] == "squ":
                contr_squalifica.append(pilota)
            else:
                punti_team -= (punti_pen[penalità["tipo"]] * int(penalità["molt"]))
            setattr(team, numerogara, punti_team)
            team.save()
        # Infine se i punti gara sono inalterati (NULL/None), assegnagli 0
        for pilota in Moto_piloti.objects.all():
            if getattr(pilota, numerogara) is None:
                setattr(pilota, numerogara, 0)
                pilota.save()
        for team in Moto_team.objects.all():
            if getattr(team, numerogara) is None:
                setattr(team, numerogara, 0)
                team.save()
        # Assegna bonus capitano
        for capitano in capitani:
            pilota = Moto_piloti.objects.get(nome=capitano["nome"])
            già_punticap = getattr(pilota, numerogara)
            if già_punticap is None:
                già_punticap = 0
            if capitano["risultato"] == "" or int(capitano["risultato"]) > 15:
                già_punticap -= 10
            elif 15 <= int(capitano["risultato"]) < 10:
                già_punticap -= 5
            elif 10 <= int(capitano["risultato"]) < 5:
                già_punticap += 0
            elif int(capitano["risultato"]) <= 5:
                già_punticap += 10
            setattr(pilota, numerogara, già_punticap)
            pilota.save()

        # Iniziamo a calcolare le formazioni dopo aver finito l'assegno punti
        for formazione in Moto_formazione.objects.filter(giornata=id):
            totale_punti = 0
            squ_pilota = None
            if len(contr_squalifica) != 0:
                for squalificato in contr_squalifica:
                    if squalificato.utente == formazione.utente:
                        squ_pilota = squalificato
            try:
                for pilota in formazione.piloti.all():
                    form_pilota = Moto_piloti.objects.get(nome=pilota.nome)
                    if squ_pilota:
                        if squ_pilota.categoria != form_pilota.categoria:
                            totale_punti += getattr(form_pilota, numerogara)
                    else:
                        totale_punti += getattr(form_pilota, numerogara)
                for team in formazione.team.all():
                    form_team = Moto_team.objects.get(nome=team.nome)
                    if squ_pilota:
                        if squ_pilota.categoria != form_team.categoria:
                            totale_punti += getattr(form_team, numerogara)
                    else:
                        totale_punti += getattr(form_team, numerogara)
            except:
                pass
            try:
                form_tm = Moto_teammanager.objects.get(nome=formazione.teammanager.nome)
                if squ_pilota:
                    if squ_pilota.categoria != "F1":
                        totale_punti += getattr(form_tm, numerogara)
                else:
                    totale_punti += getattr(form_tm, numerogara)
            except:
                pass
            formazione.p_totali = totale_punti
            formazione.save()

        # Ottieni scontri tra utenti
        scontri = Moto_scontri.objects.get(id=id).scontri
        coppia_scontri = scontri.split("/")
        utenti_scontri = []
        for sfida in coppia_scontri:
            utenti_scontri.append(sfida.split("+"))
        for utente in utenti_scontri:
            formaz1 = Moto_formazione.objects.get(giornata=id, username=utente[0])
            formaz2 = Moto_formazione.objects.get(giornata=id, username=utente[1])
            punti1 = Moto_punti.objects.get(username=utente[0])
            punti2 = Moto_punti.objects.get(username=utente[1])
            if formaz1.p_totali > formaz2.p_totali:
                formaz1.risultato = 1
                formaz2.risultato = 0
                punti1.p_scontri += 3
            elif formaz1.p_totali < formaz2.p_totali:
                formaz1.risultato = 0
                formaz2.risultato = 1
                punti2.p_scontri += 3
            elif formaz1.p_totali == formaz2.p_totali:
                formaz1.risultato = 2
                formaz2.risultato = 2
                punti1.p_scontri += 1
                punti2.p_scontri += 1
            punti1.p_generali += formaz1.p_totali
            punti2.p_generali += formaz2.p_totali
            differenza = formaz1.p_totali - formaz2.p_totali
            punti1.differenza += differenza
            punti2.differenza -= differenza
            formaz1.save()
            formaz2.save()
            punti1.save()
            punti2.save()
        # Tutte le formazioni sono calcolate, ora segna la giornata come calcolata
        gara = Moto_giornata.objects.get(id=id)
        gara.calcolata = 1
        gara.save()
        # Reindirizza alla home
        messages.success(request, "Calcoli andati a buon fine!")
        return HttpResponseRedirect(reverse("fantamoto"))

    # Richiesta GET, mostra pagina, se gara è nel futuro mostra errore
    adesso = timezone.localtime()
    giornata = Moto_giornata.objects.get(id=id).data
    if giornata > adesso:
        return render(request, "errore.html", {
            "message": "LA GARA NON È ANCORA STATA DISPUTATA >:(",
            "cat": "moto"
        })
    # Controlla se la gara è già stata calcolata
    calcolata = Moto_giornata.objects.get(id=id).calcolata
    posto = Moto_giornata.objects.get(id=id).posto
    if not calcolata:
        piloti = Moto_piloti.objects.all()
    else:
        return render(request, "errore.html", {
            "message": f"LA GARA SELEZIONATA ({posto}) È GIÀ STATA CALCOLATA!",
            "cat": "moto"
        })
    # Helpers per display piloti
    categorie = Moto_giornata.objects.get(id=id).categ
    listacat = categorie.split(",")
    numeroquali = ["1","2","3"]
    # Lista piloti moto per il button qualifiche
    moto_listapiloti = []
    moto_allpilotilista = Moto_piloti.objects.all().values("nome")
    for moto_pilotalista in moto_allpilotilista:
        moto_listapiloti.append(moto_pilotalista["nome"])
    return render(request, "fantamoto/calcolo_gara.html", {
        "id": id,
        "posto": posto,
        "piloti": piloti,
        "listacat": listacat,
        "numeroquali": numeroquali,
        "cat": "moto",
        "listapiloti": moto_listapiloti
    })



############################################################# FORMULA ###################################################################
@login_required
def formula_home(request):
    check_formula(request)
    now = timezone.localtime()
    alldates = Formula_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    # Cerca prossima gara, se finite, ritorna None
    try:
        nextgara = Formula_giornata.objects.get(data=nextdate)
    except:
        nextgara = None
    # Cerca ultimo risultato, se prima gara, ritorna None
    try:
        dataultimagara = max(data for data in alldates if data < now)
        ultimagara = Formula_giornata.objects.get(data=dataultimagara)
    except:
        ultimagara = None
        previousgara = None
    if ultimagara:
        try:
            previousgara = Formula_formazione.objects.get(giornata=ultimagara.id, username=request.user.username)
        except:
            previousgara = None
    # Ritorna posizioni in classifica
    s_ranking = Formula_punti.objects.order_by("-p_scontri", "-differenza")
    p_ranking = Formula_punti.objects.order_by("-p_generali", "-differenza")
    # Cerca se hai schierato la formazione per la prossima gara
    try:
        schierata = Formula_formazione.objects.get(giornata=nextgara.id, username=request.user)
    except:
        schierata = None
    # Categorie prossima giornata
    if nextgara:
        listacat = []
        for cat in nextgara.categ.split(","):
            match cat:
                case "f1": listacat.append("F1")
                case "f2": listacat.append("F2")
                case "f3": listacat.append("F3")
                case "indy": listacat.append("IndyCar")
    else:
        listacat = None
    return render(request, "fantaformula/home.html", {
        "utente": request.user,
        "ultimagara": ultimagara,
        "previousgara": previousgara,
        "nextgara": nextgara,
        "s_ranking": s_ranking,
        "p_ranking": p_ranking,
        "schierata": schierata,
        "listacat": listacat,
        "cat": "formula"
    })


@login_required
def formula_rose(request):
    check_formula(request)
    lista_utenti = []
    for utenti in User.objects.order_by("username"):
        if utenti.fanta != 1:
            lista_utenti.append(utenti)
    return render(request, "fantaformula/rose.html", {
        "tutti": lista_utenti,
        "cat": "formula"
    })


@login_required
def formula_rosautente(request, utente):
    check_formula(request)
    piloti = Formula_piloti.objects.filter(username=utente)
    teams = Formula_team.objects.filter(username=utente)
    tm = Formula_teammanager.objects.get(username=utente)
    return render(request, "fantaformula/rosa_utente.html", {
        "utente": utente,
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "cat": "formula"
    })


@login_required
def formula_calendario(request):
    check_formula(request)
    giornate = Formula_giornata.objects.all()
    now = timezone.localtime()
    alldates = Formula_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    # Se prima gara
    if now < Formula_giornata.objects.get(id=1).data:
        ultimagara = 1
    # Se altre giornate
    else:
        dataultimagara = max(data for data in alldates if data < now)
        ultimagara = Formula_giornata.objects.get(data=dataultimagara).id
    # Distingui giornate e scontri
    all_id = []
    all_sfide = []
    for sfida in Formula_scontri.objects.all():
        all_id.append(sfida.giornata)
        scontri_lista = []
        scontri = sfida.scontri.split("/")
        for scontro in scontri:
            scontro = scontro.split("+")
            scontri_lista.append(scontro)
        all_sfide.append(scontri_lista)
    lista_utenti = []
    for utenti in User.objects.order_by("username"):
        if utenti.fanta != 1:
            lista_utenti.append(utenti)
    return render(request, "fantaformula/calendario.html", {
        "giornate": giornate,
        "ultima": ultimagara,
        "sfide": all_sfide,
        "tutti": lista_utenti,
        "cat": "formula"
    })


@login_required
def formula_scontro(request, id, scontro):
    check_formula(request)
    posto = Formula_giornata.objects.get(id=id).posto
    # Separa i nomi nella sfida e ottieni gli utente_id
    sfidante1, sfidante2 = scontro.split("-")
    id_sfidante1 = User.objects.get(username=sfidante1).id
    id_sfidante2 = User.objects.get(username=sfidante2).id
    # Cerca se le formazioni sono state schierate
    try:
        formazione1 = Formula_formazione.objects.get(utente_id=id_sfidante1, giornata=id)
    except:
        formazione1 = None
    try:
        formazione2 = Formula_formazione.objects.get(utente_id=id_sfidante2, giornata=id)
    except:
        formazione2 = None
    # Numero gara
    if int(id) < 10:
        numerogara = f"gara0{id}"
    else:
        numerogara = f"gara{id}"
    # Ottieni formazione primo user
    try:
        piloti1 = formazione1.piloti.all()
        teams1 = formazione1.team.all()
        if Formula_giornata.objects.get(id=id).categ.count(",") != 1:
            tm1 = formazione1.teammanager.nome
        else:
            tm1 = None
        # Se la formazione è già stata calcolata, carica i punti ottenuti da piloti,team, tm
        # Seleziona i punteggi da Formula_piloti e consegnali in una lista
        punti_piloti1 = []
        for pilota1 in piloti1:
            punti_pilota1 = getattr(Formula_piloti.objects.get(nome=pilota1.nome), numerogara)
            if punti_pilota1 or punti_pilota1 == 0:
                punti_piloti1.append(punti_pilota1)
        # Seleziona punti del team
        punti_teams1 = []
        for team1 in teams1:
            punti_team1 = getattr(Formula_team.objects.get(nome=team1.nome), numerogara)
            if punti_team1 or punti_team1 == 0:
                punti_teams1.append(punti_team1)
        # E del team manager
        if Formula_giornata.objects.get(id=id).categ.count(",") != 1:
            punti_tm1 = getattr(Formula_teammanager.objects.get(nome=tm1), numerogara)
        else:
            punti_tm1 = None
        # Se risultati ancora vuoti, non mostrare nulla
        if punti_piloti1 == [] and punti_teams1 == [] and punti_tm1 is None:
            punti_piloti1 = None
            punti_teams1 = None
    # Formazione non è stata schierata
    except:
        piloti1 = None
        teams1 = None
        tm1 = None
        punti_piloti1 = None
        punti_teams1 = None
        punti_tm1 = None
    # Cerca se il capitano è stato schierato
    try:
        capitano1 = formazione1.capitano.nome
    except:
        capitano1 = None
    # Cerca che gara del capitano
    try:
        if not formazione1.cap_gara:
            garacap1 = ""
        else:
            garacap1 = formazione1.cap_gara
    except:
        garacap1 = None
    # Secondo utente
    # Se formazione è schierata
    try:
        piloti2 = formazione2.piloti.all()
        teams2 = formazione2.team.all()
        if Formula_giornata.objects.get(id=id).categ.count(",") != 1:
            tm2 = formazione2.teammanager.nome
        else:
            tm2 = None
        # Piloti
        punti_piloti2 = []
        for pilota2 in piloti2:
            punti_pilota2 = getattr(Formula_piloti.objects.get(nome=pilota2.nome), numerogara)
            if punti_pilota2 or punti_pilota2 == 0:
                punti_piloti2.append(punti_pilota2)
        # Team
        punti_teams2 = []
        for team2 in teams2:
            punti_team2 = getattr(Formula_team.objects.get(nome=team2.nome), numerogara)
            if punti_team2 or punti_team2 == 0:
                punti_teams2.append(punti_team2)
        # Team Manager
        if Formula_giornata.objects.get(id=id).categ.count(",") != 1:
            punti_tm2 = getattr(Formula_teammanager.objects.get(nome=tm2), numerogara)
        else:
            punti_tm2 = None
        # Non mostrare nulla se vuoto
        if punti_piloti2 == [] and punti_teams2 == [] and punti_tm2 is None:
            punti_piloti2 = None
            punti_teams2 = None
    except:
        piloti2 = None
        teams2 = None
        tm2 = None
        punti_piloti2 = None
        punti_teams2 = None
        punti_tm2 = None
    # Capitano
    try:
        capitano2 = formazione2.capitano.nome
    except:
        capitano2 = None
    # Gara capitano
    try:
        if formazione2.cap_gara is None:
            garacap2 = ""
        else:
            garacap2 = formazione2.cap_gara
    except:
        garacap2 = None
    return render(request, "fantaformula/risultato.html", {
        "id": id,
        "posto": posto,
        "s1": sfidante1,
        "s2": sfidante2,
        "formazione1": formazione1,
        "formazione2": formazione2,
        "piloti1": piloti1,
        "piloti2": piloti2,
        "teams1": teams1,
        "teams2": teams2,
        "tm1": tm1,
        "tm2": tm2,
        "capitano1": capitano1,
        "capitano2": capitano2,
        "garacap1": garacap1,
        "garacap2": garacap2,
        "punti_piloti1": punti_piloti1,
        "punti_teams1": punti_teams1,
        "punti_tm1": punti_tm1,
        "punti_piloti2": punti_piloti2,
        "punti_teams2": punti_teams2,
        "punti_tm2": punti_tm2,
        "cat": "formula"
    })


@login_required
def formula_albo(request):
    check_formula(request)
    return render(request, "fantaformula/albodoro.html", {"cat": "formula"})


@login_required
def formula_formazione(request):
    check_formula(request)
    # Ottieni prossima giornata
    now = timezone.localtime()
    alldates = Formula_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    nextgara = Formula_giornata.objects.get(data=nextdate)
    # Seleziona piloti, team e tm disponibili
    piloti = Formula_piloti.objects.filter(username=request.user.username)
    teams = Formula_team.objects.filter(username=request.user.username)
    tm = Formula_teammanager.objects.get(username=request.user.username)
    # Ottieni gli ultimi tre risultati
    ultime = [nextgara.id - 1, nextgara.id - 2, nextgara.id - 3]
    # Non prendere id giornate negativo o zero
    for i in range(3):
        if ultime[i] == 0 or ultime[i] < 0:
            ultime[i] = 0
    # Punti piloti ultime 3 giornate
    punti_piloti = []
    for pilota in piloti:
        punti_pilota = []
        for giornata in ultime:
            try:
                # Ottieni ultime 3 giornate
                if giornata < 10:
                    numerogara = f"gara0{giornata}"
                else:
                    numerogara = f"gara{giornata}"
                punti_g = getattr(Formula_piloti.objects.get(nome=pilota.nome), numerogara)
                punti_pilota.append(punti_g)
            except:
                punti_pilota.append("-")
        # Aggiungi pilota ai piloti
        punti_piloti.append(punti_pilota)
    # Ripeti per i team
    punti_teams = []
    for team in teams:
        punti_team = []
        for giornata in ultime:
            try:
                # Ottieni ultime 3 giornate
                if giornata < 10:
                    numerogara = f"gara0{giornata}"
                else:
                    numerogara = f"gara{giornata}"
                punti_g = getattr(Formula_team.objects.get(nome=team.nome), numerogara)
                punti_team.append(punti_g)
            except:
                punti_team.append("-")
        # Aggiungi team ai teams
        punti_teams.append(punti_team)
    # Ripeti per team manager
    punti_tm = []
    for giornata in ultime:
        try:
            # Ottieni ultime 3 giornate
            if giornata < 10:
                numerogara = f"gara0{giornata}"
            else:
                numerogara = f"gara{giornata}"
            punti_g = getattr(Formula_teammanager.objects.get(nome=tm.nome), numerogara)
            punti_tm.append(punti_g)
        except:
            punti_tm.append("-")
    # Trova categorie nella prossima giornata
    listacat = []
    for cat in nextgara.categ.split(","):
        match(cat):
            case "f1": listacat.append("F1")
            case "f2": listacat.append("F2")
            case "f3": listacat.append("F3")
            case "indy": listacat.append("Indy")
    numcategorie = len(listacat)
    return render(request, "fantaformula/formazione.html", {
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "nextgara": nextgara,
        "punti_piloti": punti_piloti,
        "punti_teams": punti_teams,
        "punti_tm": punti_tm,
        "numcategorie": numcategorie,
        "listacat": listacat,
        "cat": "formula"
    })


@login_required
def formula_schieramento(request):
    check_formula(request)
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
        check_capitano = []
        piloti = request.POST.getlist("piloti")
        teams = request.POST.getlist("teams")
        tm = request.POST.get("tm")
        capitano = request.POST["capitan"]
        gara1 = request.POST.get("gara1")
        gara2 = request.POST.get("gara2")
        # Controlla capitano
        for pilota in piloti:
            check_capitano.append(pilota.split(" - ")[0])
        if capitano not in check_capitano and capitano != "0":
            message = "FORMAZIONE NON SCHIERATA: CAPITANO SELEZIONATO NON PRESENTE NELLA FORMAZIONE"
        # Controlla numero giusto piloti e team per categorie della prossima gara
        listacat = []
        for cat in nextgara.categ.split(","):
            match(cat):
                case "f1": listacat.append("F1")
                case "f2": listacat.append("F2")
                case "f3": listacat.append("F3")
                case "indy": listacat.append("IndyCar")
        numcategorie = len(listacat)
        if (tm is None and numcategorie != 1) or (tm is None and numcategorie == 1 and "indy" not in nextgara.categ):
            message = "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM MANAGER"
        if numcategorie == 1:
            if len(piloti) != 2:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 2 PILOTI"
            elif len(teams) != 1:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM"
        elif numcategorie == 2:
            if len(piloti) != 4:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 4 PILOTI"
            elif len(teams) != 2:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 2 TEAM"
        elif numcategorie == 3:
            if len(piloti) != 6:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 6 PILOTI"
            elif len(teams) != 3:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 3 TEAM"
        elif numcategorie == 4:
            if len(piloti) != 8:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 8 PILOTI"
            elif len(teams) != 4:
                message = "FORMAZIONE NON SCHIERATA: SELEZIONA 4 TEAM"
        elif numcategorie > 4:
            message = f"{numcategorie}"
        try:
            if message:
                return render(request, "errore.html", {"cat": "formula", "message": message})
        except:
            pass
            
        # Se arrivati fin qui, la formazione non presenta errori
        # Se una formazione è già stata schierata, elimina la vecchia
        if Formula_formazione.objects.filter(giornata=nextgara.id, username=request.user.username):
            Formula_formazione.objects.filter(giornata=nextgara.id, username=request.user.username).delete()
        # Variabili da inserire nell'oggetto Formula_formazione
        formazione_giornata = nextgara.id
        formazione_data = now
        formazione_piloti = []
        formazione_teams = []
        # Trova l'id dei piloti e dei team scelti
        for pilota in piloti:
            p = pilota.split(" - ")[0]
            p_id = Formula_piloti.objects.get(nome=p)
            formazione_piloti.append(p_id)
        for team in teams:
            t = team.split(" - ")[0]
            t_id = Formula_team.objects.get(nome=t)
            formazione_teams.append(t_id)
        try:
            formazione_tm = Formula_teammanager.objects.get(nome=tm)
        except:
            formazione_tm = None
        formazione_user = request.user
        # Seleziona il capitano
        if capitano != "0":
            formazione_capitano = Formula_piloti.objects.get(nome=capitano)
            if formazione_capitano.categoria != "IndyCar":
                garacap = 1
            else:
                garacap = 1 if gara1 else 2
        else:
            formazione_capitano = None
            garacap = None
        # Salva la formazione nel database
        formazione = Formula_formazione.objects.create(
            giornata = formazione_giornata,
            data = formazione_data,
            teammanager = formazione_tm,
            username = request.user.username,
            utente = formazione_user,
            capitano = formazione_capitano,
            cap_gara = garacap)
        formazione.piloti.set(formazione_piloti)
        formazione.team.set(formazione_teams)
        formazione.save()
        # Rispedisci alla home
        messages.success(request, "Formazione schierata!")
        return HttpResponseRedirect(reverse("fantaformula"))


@login_required
def formula_calcoloscelta(request):
    check_formula(request)
    check_admin(request, "formula")
    giornate = Formula_giornata.objects.all()
    return render(request, "fantaformula/calcolo_scelta.html", {
        "giornate": giornate,
        "cat": "formula"
    })


@login_required
def formula_admpiloti(request):
    check_formula(request)
    check_admin(request, "formula")
    # Lista piloti formula
    formula_listapiloti = []
    formula_allpilotilista = Formula_piloti.objects.all().values("nome")
    for formula_pilotalista in formula_allpilotilista:
        formula_listapiloti.append(formula_pilotalista["nome"])
    # Cambia nome al pilota e aggiungi "ex (vecchionome)"
    if request.method == "POST":
        pilota = Formula_piloti.objects.get(nome=request.POST.get("oldname"))
        nome = f"{request.POST.get('newname')} (ex {pilota.nome})"
        pilota.nome = nome
        pilota.save()
    return render(request, "fantaformula/adm_piloti.html", {
        "cat": "formula",
        "listapiloti": formula_listapiloti
    })


@login_required
def formula_admteam(request):
    check_formula(request)
    check_admin(request, "formula")
    # Lista piloti formula
    formula_listapiloti = []
    formula_allpilotilista = Formula_piloti.objects.all().values("nome")
    for formula_pilotalista in formula_allpilotilista:
        formula_listapiloti.append(formula_pilotalista["nome"])
    # Sostituisci oldpilota dal team selezionato con newpilota
    if request.method == "POST":
        team = request.POST["team"]
        old = Formula_piloti.objects.get(nome=request.POST["oldpilota"])
        new = Formula_piloti.objects.get(nome=request.POST["newpilota"])
        if old.team != team:
            return render(request, "errore.html", {
                "message": f"{old.nome} non è un pilota del team {team}",
                "cat": "formula"
            })
        old.team = None
        new.team = team
        old.save()
        new.save()
    return render(request, "fantamoto/adm_team.html", {
        "cat": "formula",
        "teams": Formula_team.objects.all(),
        "listapiloti": formula_listapiloti
    })
    

@login_required
def formula_admgara(request):
    check_formula(request)
    check_admin(request, "formula")
    if request.method == "POST":
        gara = Formula_giornata.objects.get(posto=request.POST["gara"])
        if request.POST["annullata"] == "1":
            gara.annullata = 1
            gara.save()
        else:
            # Nome
            if request.POST["nome"] != "":
                gara.posto = request.POST["nome"]
            # Cambia categorie gara
            categorie = ""
            if request.POST.get("Sprint") != "":
                categorie += "sprint,"
            if request.POST.get("F1") != "":
                categorie += "f1,"
            if request.POST.get("F2") != "":
                categorie += "f2,"
            if request.POST.get("F3") != "":
                categorie += "f3,"
            if request.POST.get("IndyCar") != "":
                categorie += "indy,"
            if request.POST.get("I2") != "":
                categorie += "i2,"
            gara.categ = categorie
            # Orario
            if request.POST["orario"] != "":
                orario = request.POST["orario"].replace("T", " ")
                orario += ":00"
                orario = datetime.strptime(orario, "%Y-%m-%d %H:%M:%S")
                gara.data = orario
            gara.save()
    return render(request, "fantaformula/adm_gara.html", {
        "cat": "formula",
        "gare": Formula_giornata.objects.all()
    })


@login_required
def formula_calcologara(request, id):
    check_formula(request)
    check_admin(request, "formula")
    # Se si sta facendo una richiesta POST, calcola i risultati
    if request.method == "POST":
        if Formula_giornata.objects.get(id=id).calcolata:
            return render(request, "errore.html", {
                "message": f"HAI GIÀ CALCOLATO QUESTA GIORNATA ._.",
                "cat": "formula"
            })
        # Ottieni tutte le formazioni schierate (se non schierata, creane una vuota)
        formazioni = []
        for user in User.objects.all():
            if user.fanta != 1:
                try:
                    formazione = Formula_formazione.objects.get(username=user.username, giornata=id)
                except:
                    formazione = Formula_formazione.objects.create(
                        giornata = id,
                        data = timezone.localtime(),
                        username = user.username,
                        utente = user)
                    formazione.save()
                formazioni.append(formazione)
        # Distingui le info ricevute da POST e controlla se errori
        categorie = Formula_giornata.objects.get(id=id).categ
        contr_quali = []
        for cat in categorie.split(","):
            if cat == "sprint":
                contr_spr = []
                contr_flspr = 0
            elif cat == "f1":
                contr_feat = []
                contr_flfeat = 0
                contr_bestpilota = 0
                contr_bestpit = 0
            elif cat == "f2":
                contr_2spr = []
                contr_2flspr = 0
                contr_2feat = []
                contr_2flfeat = 0
            elif cat == "f3":
                contr_3spr = []
                contr_3flspr = 0
                contr_3feat = []
                contr_3flfeat = 0
            elif cat == "indy":
                contr_ifeat = []
                contr_iflfeat = 0
            elif cat == "i2":
                contr_i2feat = []
                contr_i2flfeat = 0
        for key, value in request.POST.items():
            # Errori Qualifiche
            if "-q1" in key or "-q2" in key or "-q3" in key:
                if value != "":
                    temp_cate = key.split("-")[0]
                    contr_cate_pilota = Formula_piloti.objects.get(nome=value).categoria
                    if temp_cate == "f1" and contr_cate_pilota != "F1":
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    elif temp_cate == "f2" and contr_cate_pilota != "F2":
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    elif temp_cate == "f3" and contr_cate_pilota != "F3":
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    elif temp_cate == "indy" and contr_cate_pilota != "IndyCar":
                        message = "CALCOLO ANNULLATO: SCELTO PILOTA IN QUALIFICA NON APPARTENENTE ALLA SUA CATEGORIA"
                    if value not in contr_quali:
                        contr_quali.append(value)
                    else:
                        message = "CALCOLO ANNULLATO: UN PILOTA E' PRESENTE PIU' VOLTE NELLE QUALIFICHE"
                else:
                    message = "CALCOLO ANNULLATO: IN UNA QUALIFICA NON E' STATO SPECIFICATO UN PILOTA"
            # Errori Gare
            elif "-spr-" in key:
                if "f1-" in key:
                    if value not in contr_spr and value != "":
                        contr_spr.append(value)
                    elif value in contr_spr:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (SPRINT F1)"
                elif "f2-" in key:
                    if value not in contr_2spr and value != "":
                        contr_2spr.append(value)
                    elif value in contr_2spr:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (SPRINT F2)"
                elif "f3-" in key:
                    if value not in contr_3spr and value != "":
                        contr_3spr.append(value)
                    elif value in contr_3spr:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (SPRINT F3)"
            elif "-feat-" in key:
                if "f1-" in key:
                    if value not in contr_feat and value != "":
                        contr_feat.append(value)
                    elif value in contr_feat:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (FEATURE F1)"
                elif "f2-" in key:
                    if value not in contr_2feat and value != "":
                        contr_2feat.append(value)
                    elif value in contr_2feat:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (FEATURE F2)"
                elif "f3-" in key:
                    if value not in contr_3feat and value != "":
                        contr_3feat.append(value)
                    elif value in contr_3feat:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (FEATURE F3)"
                elif "indy-" in key:
                    if value not in contr_ifeat and value != "":
                        contr_ifeat.append(value)
                    elif value in contr_ifeat:
                        message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (FEATURE IndyCar)"
            elif "-feat2-" in key:
                if value not in contr_i2feat and value != "":
                    contr_i2feat.append(value)
                elif value in contr_i2feat:
                    message = "CALCOLO ANNULLATO: DUE PILOTI HANNO LA STESSA POSIZIONE (FEATURE2 IndyCar)"
            # Errori Fast Lap
            elif "-flspr-" in key:
                if "f1-" in key:
                    contr_flspr += 1
                elif "f2-" in key:
                    contr_2flspr += 1
                elif "f3-" in key:
                    contr_3flspr += 1
            elif "-flfeat-" in key:
                if "f1-" in key:
                    contr_flfeat += 1
                elif "f2-" in key:
                    contr_2flfeat += 1
                elif "f3-" in key:
                    contr_3flfeat += 1
                elif "indy-" in key:
                    contr_iflfeat += 1
            elif "-flfeat2-" in key:
                contr_i2flfeat += 1
            # Errori miglior pilota/pit
            elif "-bestpilot-" in key:
                contr_bestpilota += 1
            elif "-bestpit-" in key:
                contr_bestpit += 1
        for cat in categorie.split(","):
            if cat == "f1":
                if contr_flfeat != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (FEATURE F1)"
                elif contr_bestpilota != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI SONO I MIGLIORI DELLA GIORNATA/NESSUN PILOTA COME MIGLIORE DELLA GIORNATA"
                elif contr_bestpit != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO IL MIGLIOR PIT/NESSUN PILOTA HA IL MIGLIOR PIT"
            elif cat == "sprint":
                if contr_flspr != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (SPRINT F1)"
            elif cat == "f2":
                if contr_2flspr != 1 or contr_2flfeat != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (F2)"
            elif cat == "f3":
                if contr_3flspr != 1 or contr_3flfeat != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (F3)"
            elif cat == "indy":
                if contr_iflfeat != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (IndyCar)"
            elif cat == "i2":
                if contr_i2flfeat != 1:
                    message = "CALCOLO ANNULLATO: PIU' PILOTI HANNO LO STESSO FAST LAP/NESSUN FAST LAP ASSEGNATO (IndyCar Feat2)"
        try:
            return render(request, "errore.html", {"cat": "formula", "message": message})
        except:
            print("Nessun errore")
        
        # Definiamo punteggi gare e helpers
        punti_feat12 = {"1": 25, "2": 18, "3": 15, "4": 12, "5": 10, "6": 8, "7": 6, "8": 4, "9": 2, "10": 1}
        punti_spr12 = {"1": 10, "2": 8, "3": 6, "4": 5, "5": 4, "6": 3, "7": 2, "8": 1}
        punti_feat3i = {"1": 15, "2": 14, "3": 13, "4": 12, "5": 11, "6": 10, "7": 9, "8": 8, "9": 7, "10": 6, "11": 5, "12": 4, "13": 3, "14": 2, "15": 1}
        punti_spr3i = {"1": 10, "2": 9, "3": 8, "4": 7, "5": 6, "6": 5, "7": 4, "8": 3, "9": 2, "10": 1}
        if int(id) < 10:
            numerogara = f"gara0{id}"
        else:
            numerogara = f"gara{id}"
        zonaout = {"spr12": 8, "feat12": 10, "spr3i": 10, "feat3i": 15}
        contr_pen = []
        contr_squalifica = []
        # Cerca capitani schierati
        capitani = []
        for formazione in Formula_formazione.objects.filter(giornata=id):
            if formazione.capitano:
                pil_capitano = Formula_piloti.objects.get(nome=formazione.capitano.nome)
                garacap = formazione.cap_gara
                capitani.append(dict(nome=pil_capitano.nome, gara=garacap, risultato=""))
        # Iniziamo a calcolare piloti e team
        for key, value in request.POST.items():
            # Gare
            if "-spr-" in key or "-feat-" in key or "-feat2-" in key:
                # Calcolo punteggio team va qui se no prende bonus piloti
                pilota = Formula_piloti.objects.get(nome=key.split("-")[2])
                team = Formula_team.objects.get(nome=pilota.team.nome)
                if "f1-spr" in key or "f2-spr" in key:
                    qualegara = "spr12"
                elif "f1-feat" in key or "f2-feat" in key:
                    qualegara = "feat12"
                elif "f3-spr" in key:
                    qualegara = "spr3i"
                elif "f3-feat" in key or "indy-feat" in key or "indy-feat2" in key:
                    qualegara = "feat3i"
                if value != "" and int(value) <= zonaout[qualegara]:
                    # Controlla se capitano (bonus da assegnare alla fine)
                    for capitano in capitani:
                        if pilota.nome == capitano["nome"]:
                            if "-feat-" in key and capitano["gara"] == 1:
                                capitano["risultato"] = value
                            elif "-feat2-" in key and capitano["gara"] == 2:
                                capitano["risultato"] = value
                    # Continua con punti piloti e team
                    già_ppunti = getattr(pilota, numerogara)
                    già_tpunti = getattr(team, numerogara)
                    if già_ppunti is None:
                        già_ppunti = 0
                    if già_tpunti is None:
                        già_tpunti = 0
                    if "-spr-" in key:
                        if "f1-" in key or "f2-" in key:
                            già_ppunti += punti_spr12[value]
                            già_tpunti += punti_spr12[value]
                        elif "f3-" in key:
                            già_ppunti += punti_spr3i[value]
                            già_tpunti += punti_spr3i[value]
                    elif "-feat" in key:
                        if "f1-" in key or "f2-" in key:
                            già_ppunti += punti_feat12[value]
                            già_tpunti += punti_feat12[value]
                        elif "f3-" in key or "indy-" in key:
                            già_ppunti += punti_feat3i[value]
                            già_tpunti += punti_feat3i[value]
                    setattr(pilota, numerogara, già_ppunti)
                    setattr(team, numerogara, già_tpunti)
                    pilota.save()
                    team.save()
            # Qualifiche
            elif "-q1" in key or "-q2" in key or "-q3" in key:
                if value != "":
                    pilota = Formula_piloti.objects.get(nome=value)
                    posiz_quali = key.split("-")[1]
                    già_punti = getattr(pilota, numerogara)
                    if già_punti is None:
                        già_punti = 0
                    match posiz_quali:
                        case "q1": già_punti += 5
                        case "q2": già_punti += 3
                        case "q3": già_punti += 1
                    setattr(pilota, numerogara, già_punti)
                    pilota.save()
            # Fast Lap
            elif "-flspr-" in key or "-flfeat-" in key or "-flfeat2-" in key:
                if value == "on":
                    pilota = Formula_piloti.objects.get(nome=key.split("-")[2])
                    già_punti = getattr(pilota, numerogara)
                    if già_punti is None:
                        già_punti = 0
                    già_punti += 1
                    setattr(pilota, numerogara, già_punti)
                    pilota.save()
            # Miglior pilota
            elif "-bestpilot-" in key:
                if value == "on":
                    pilota = Formula_piloti.objects.get(nome=key.split("-")[2])
                    già_punti = getattr(pilota, numerogara)
                    if già_punti is None:
                        già_punti = 0
                    già_punti += 3
                    setattr(pilota, numerogara, già_punti)
                    pilota.save()
            # Ricordi di bonus/penalità team per dopo
            elif "-bestpit-" in key:
                if value == "on":
                    contr_pen.append(dict(nome=key.split("-")[2], tipo="bestpit", molt="1"))
            elif "-5s-" in key or "-dt-" in key or "-squ-" in key:
                if value != "":
                    contr_pen.append(dict(nome=key.split("-")[2], tipo=key.split("-")[1], molt=value))
        # Ora i team manager (qui non prenderanno bonus/malus del team)
        for tm in Formula_teammanager.objects.all():
            corrisp_team = Formula_team.objects.get(nome=tm.team.nome)
            punti_team = getattr(corrisp_team, numerogara)
            if punti_team is None:
                punti_team = 0
            punti_tm = int(punti_team / 2)
            setattr(tm, numerogara, punti_tm)
            tm.save()
        # Penalità
        for penalità in contr_pen:
            pilota = Formula_piloti.objects.get(nome=penalità["nome"])
            team = Formula_team.objects.get(nome=pilota.team.nome)
            punti_team = getattr(team, numerogara)
            if punti_team is None:
                punti_team = 0
            if penalità["tipo"] == "bestpit":
                punti_team += 3
            elif penalità["tipo"] == "5s":
                punti_team = punti_team - (2 * int(penalità["molt"]))
            elif penalità["tipo"] == "dt":
                punti_team = punti_team - (10 * int(penalità["molt"]))
            elif penalità["tipo"] == "squ":
                contr_squalifica.append(pilota)
            setattr(team, numerogara, punti_team)
            team.save()
        # Se punti gara sono None, assegna 0
        for pilota in Formula_piloti.objects.all():
            if getattr(pilota, numerogara) is None:
                setattr(pilota, numerogara, 0)
                pilota.save()
        for team in Formula_team.objects.all():
            if getattr(team, numerogara) is None:
                setattr(team, numerogara, 0)
                team.save()
        # Assegna bonus capitano
        for capitano in capitani:
            pilota = Formula_piloti.objects.get(nome=capitano["nome"])
            già_punticap = getattr(pilota, numerogara)
            if già_punticap is None:
                già_punticap = 0
            if capitano["risultato"] == "" or int(capitano["risultato"]) > 10:
                già_punticap -= 10
            elif 10 <= int(capitano["risultato"]) < 7:
                già_punticap -= 5
            elif 7 <= int(capitano["risultato"]) < 5:
                già_punticap += 0
            elif 5 <= int(capitano["risultato"]) < 3:
                già_punticap += 5
            elif int(capitano["risultato"]) <= 3:
                già_punticap += 10
            setattr(pilota, numerogara, già_punticap)
            pilota.save()
        
        # Iniziamo a calcolare le formazioni dopo aver finito l'assegno punti
        for formazione in Formula_formazione.objects.filter(giornata=id):
            totale_punti = 0
            squ_pilota = None
            if len(contr_squalifica) != 0:
                for squalificato in contr_squalifica:
                    if squalificato.utente == formazione.utente:
                        squ_pilota = squalificato
            try:
                for pilota in formazione.piloti.all():
                    form_pilota = Formula_piloti.objects.get(nome=pilota.nome)
                    if squ_pilota:
                        if squ_pilota.categoria != form_pilota.categoria:
                            totale_punti += getattr(form_pilota, numerogara)
                    else:
                        totale_punti += getattr(form_pilota, numerogara)
                for team in formazione.team.all():
                    form_team = Formula_team.objects.get(nome=team.nome)
                    if squ_pilota:
                        if squ_pilota.categoria != form_team.categoria:
                            totale_punti += getattr(form_team, numerogara)
                    else:
                        totale_punti += getattr(form_team, numerogara)
            except:
                pass
            try:
                form_tm = Formula_teammanager.objects.get(nome=formazione.teammanager.nome)
                if squ_pilota:
                    if squ_pilota.categoria != "F1":
                        totale_punti += getattr(form_tm, numerogara)
                else:
                    totale_punti += getattr(form_tm, numerogara)
            except:
                pass
            formazione.p_totali = totale_punti
            formazione.save()
        
       # Ottieni scontri tra utenti
        scontri = Formula_scontri.objects.get(id=id).scontri
        coppia_scontri = scontri.split("/")
        utenti_scontri = []
        for sfida in coppia_scontri:
            utenti_scontri.append(sfida.split("+"))
        for utente in utenti_scontri:
            formaz1 = Formula_formazione.objects.get(giornata=id, username=utente[0])
            formaz2 = Formula_formazione.objects.get(giornata=id, username=utente[1])
            punti1 = Formula_punti.objects.get(username=utente[0])
            punti2 = Formula_punti.objects.get(username=utente[1])
            if formaz1.p_totali > formaz2.p_totali:
                formaz1.risultato = 1
                formaz2.risultato = 0
                punti1.p_scontri += 3
            elif formaz1.p_totali < formaz2.p_totali:
                formaz1.risultato = 0
                formaz2.risultato = 1
                punti2.p_scontri += 3
            elif formaz1.p_totali == formaz2.p_totali:
                formaz1.risultato = 2
                formaz2.risultato = 2
                punti1.p_scontri += 1
                punti2.p_scontri += 1
            punti1.p_generali += formaz1.p_totali
            punti2.p_generali += formaz2.p_totali
            differenza = formaz1.p_totali - formaz2.p_totali
            punti1.differenza += differenza
            punti2.differenza -= differenza
            formaz1.save()
            formaz2.save()
            punti1.save()
            punti2.save()
        # Tutte le formazioni sono calcolate, ora segna la giornata come calcolata
        gara = Formula_giornata.objects.get(id=id)
        gara.calcolata = 1
        gara.save()
        # Reindirizza alla home
        messages.success(request, "Calcoli andati a buon fine!")
        return HttpResponseRedirect(reverse("fantaformula"))

    # Richiesta GET, mostra pagina, se gara è nel futuro mostra errore
    adesso = timezone.localtime()
    giornata = Formula_giornata.objects.get(id=id).data
    if giornata > adesso:
        return render(request, "errore.html", {
            "message": "LA GARA NON È ANCORA STATA DISPUTATA >:(",
            "cat": "formula"
        })
    # Controlla se la gara è già stata calcolata
    calcolata = Formula_giornata.objects.get(id=id).calcolata
    posto = Formula_giornata.objects.get(id=id).posto
    if not calcolata:
        piloti = Formula_piloti.objects.all()
    else:
        return render(request, "errore.html", {
            "message": f"LA GARA SELEZIONATA ({posto}) È GIÀ STATA CALCOLATA!",
            "cat": "formula"
        })
    # Helpers per display piloti
    categorie = Formula_giornata.objects.get(id=id).categ
    listacat = categorie.split(",")
    numeroquali = ["1", "2", "3"]
    # Lista piloti formula per il button qualifiche
    formula_listapiloti = []
    formula_allpilotilista = Formula_piloti.objects.all().values("nome")
    for formula_pilotalista in formula_allpilotilista:
        formula_listapiloti.append(formula_pilotalista["nome"])
    return render(request, "fantaformula/calcolo_gara.html", {
        "id": id,
        "posto": posto,
        "piloti": piloti,
        "listacat": listacat,
        "numeroquali": numeroquali,
        "cat": "formula",
        "listapiloti": formula_listapiloti
    })

