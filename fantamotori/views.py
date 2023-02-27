# Tutto il backend del sito, con le funzioni che verranno chiamate ad ogni azione degli utenti
# Simula Pagina Web con "python manage.py runserver"
# Termina simulazione con Ctrl+C nel terminale
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Moto_giornata, Moto_formazione, Moto_piloti, Moto_punti, Moto_team, Moto_teammanager, Moto_passato, User
from .models import Formula_giornata, Formula_formazione, Formula_piloti, Formula_punti, Formula_team, Formula_teammanager, Formula_passato

# Registra nuovi utenti
def register(request):
    if request.method == "POST":
        return render(request, "errore.html", {
            "message": "Non dovresti essere qui",
            "cat": "",
        })
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username, username, password)
        user.save()
        return render(request, "register.html", {
            "message": "Utente salvato"
        })
    return render(request, "errore.html", {
        "message": "Non dovresti essere qui",
        "cat": "",
    })
    return render(request, "register.html")


# Gestisce logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


# Gestisce login
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


# Scelta dei fanta
@login_required
def scelta(request):
    return render(request, "index.html")


def moto_test20(request):
    # Dimentica i risultati attribuiti precedentemente
    if Moto_formazione.objects.filter(giornata=20):
        Moto_formazione.objects.filter(giornata=20).delete()
    if Moto_giornata.objects.get(id=20).calcolata:
        Moto_giornata.objects.get(id=20).calcolata = 0
    for pilota in Moto_piloti.objects.all():
        if pilota.gara20:
            pilota.gara20 = None
    for team in Moto_team.objects.all():
        if team.gara20:
            team.gara20 = None
    for tm in Moto_teammanager.objects.all():
        if tm.gara20:
            tm.gara20 = None
    for user in Moto_punti.objects.all():
        user.p_generali = 0
        user.p_scontri = 0
        user.differenza = 0
    # Inserisci una nuova formazione
    # Tazza
    formazione_tazza = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Tazza",
        utente = User.objects.get(username="Tazza"),
        capitano = Moto_piloti.objects.get(nome="Surra")
    )
    formazione_tazza.piloti.set([Moto_piloti.objects.get(nome="Surra"),
    Moto_piloti.objects.get(nome="Holgado"),
    Moto_piloti.objects.get(nome="Canet"),
    Moto_piloti.objects.get(nome="Chantra"),
    Moto_piloti.objects.get(nome="Nakagami"),
    Moto_piloti.objects.get(nome="Aegerter"),
    Moto_piloti.objects.get(nome="Granado")])
    formazione_tazza.save()
    # Cortez
    formazione_cortez = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Cortez Black Team",
        utente = User.objects.get(username="Cortez Black Team"),
        capitano = Moto_piloti.objects.get(nome="Oncu")
    )
    formazione_cortez.piloti.set([Moto_piloti.objects.get(nome="Oncu"),
    Moto_piloti.objects.get(nome="Carrasco"),
    Moto_piloti.objects.get(nome="Navarro"),
    Moto_piloti.objects.get(nome="Bendsneyder"),
    Moto_piloti.objects.get(nome="Miller"),
    Moto_piloti.objects.get(nome="Zannoni"),
    Moto_piloti.objects.get(nome="Manfredi")])
    formazione_cortez.save()
    # Albwin
    formazione_albi = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Albwin27",
        utente = User.objects.get(username="Albwin27"),
        capitano = Moto_piloti.objects.get(nome="Zarco")
    )
    formazione_albi.piloti.set([Moto_piloti.objects.get(nome="Aji"),
    Moto_piloti.objects.get(nome="Ogura"),
    Moto_piloti.objects.get(nome="Aldeguer"),
    Moto_piloti.objects.get(nome="Kelly"),
    Moto_piloti.objects.get(nome="Zarco"),
    Moto_piloti.objects.get(nome="Canepa"),
    Moto_piloti.objects.get(nome="Fores")])
    formazione_albi.save()
    # Vettel
    formazione_vettel = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Vettel05",
        utente = User.objects.get(username="Vettel05"),
        capitano = Moto_piloti.objects.get(nome="Arbolino")
    )
    formazione_vettel.piloti.set([Moto_piloti.objects.get(nome="Nepa"),
    Moto_piloti.objects.get(nome="Bartolini"),
    Moto_piloti.objects.get(nome="Arbolino"),
    Moto_piloti.objects.get(nome="Vietti"),
    Moto_piloti.objects.get(nome="Bagnaia"),
    Moto_piloti.objects.get(nome="Oliveira"),
    Moto_piloti.objects.get(nome="Pons")])
    formazione_vettel.save()
    # Zanno
    formazione_zanno = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Zanno",
        utente = User.objects.get(username="Zanno"),
        capitano = Moto_piloti.objects.get(nome="Masia")
    )
    formazione_zanno.piloti.set([Moto_piloti.objects.get(nome="Masia"),
    Moto_piloti.objects.get(nome="Guevara"),
    Moto_piloti.objects.get(nome="Arenas"),
    Moto_piloti.objects.get(nome="Salac"),
    Moto_piloti.objects.get(nome="Martin"),
    Moto_piloti.objects.get(nome="Dovizioso"),
    Moto_piloti.objects.get(nome="Garzo")])
    formazione_zanno.save()
    # Team As
    formazione_as = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Team As Turbo",
        utente = User.objects.get(username="Team As Turbo"),
        capitano = Moto_piloti.objects.get(nome="Suzuki")
    )
    formazione_as.piloti.set([Moto_piloti.objects.get(nome="Suzuki"),
    Moto_piloti.objects.get(nome="Tatay"),
    Moto_piloti.objects.get(nome="Whatley"),
    Moto_piloti.objects.get(nome="Lowes"),
    Moto_piloti.objects.get(nome="Beaubier"),
    Moto_piloti.objects.get(nome="Marini"),
    Moto_piloti.objects.get(nome="Okubo")])
    formazione_as.save()
    # Ciccio
    formazione_ciccio = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Cicciobirro01",
        utente = User.objects.get(username="Cicciobirro01"),
        capitano = Moto_piloti.objects.get(nome="Quartararo")
    )
    formazione_ciccio.piloti.set([Moto_piloti.objects.get(nome="Sasaki"),
    Moto_piloti.objects.get(nome="Toba"),
    Moto_piloti.objects.get(nome="Roberts"),
    Moto_piloti.objects.get(nome="Kubo"),
    Moto_piloti.objects.get(nome="Quartararo"),
    Moto_piloti.objects.get(nome="Finello"),
    Moto_piloti.objects.get(nome="Ogden")])
    formazione_ciccio.save()
    # Drago
    formazione_drago = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Dragon trainer",
        utente = User.objects.get(username="Dragon trainer"),
        capitano = Moto_piloti.objects.get(nome="Mir")
    )
    formazione_drago.piloti.set([Moto_piloti.objects.get(nome="Garcia"),
    Moto_piloti.objects.get(nome="McPhee"),
    Moto_piloti.objects.get(nome="Ramirez"),
    Moto_piloti.objects.get(nome="Zaccone"),
    Moto_piloti.objects.get(nome="Mir"),
    Moto_piloti.objects.get(nome="Gardner"),
    Moto_piloti.objects.get(nome="Ferrari")])
    formazione_drago.save()
    # Pello
    formazione_pello = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Pellons",
        utente = User.objects.get(username="Pellons"),
        capitano = None
    )
    formazione_pello.piloti.set([Moto_piloti.objects.get(nome="Foggia"),
    Moto_piloti.objects.get(nome="Schrotter"),
    Moto_piloti.objects.get(nome="Acosta"),
    Moto_piloti.objects.get(nome="Bastianini"),
    Moto_piloti.objects.get(nome="Bezzecchi"),
    Moto_piloti.objects.get(nome="Casadei"),
    Moto_piloti.objects.get(nome="Escrig")])
    formazione_pello.save()
    # Paul
    formazione_paul = Moto_formazione.objects.create(
        giornata = 20,
        data = timezone.now(),
        username = "Paul Bird Motorsport",
        utente = User.objects.get(username="Paul Bird Motorsport"),
        capitano = Moto_piloti.objects.get(nome="Rins")
    )
    formazione_paul.piloti.set([Moto_piloti.objects.get(nome="Migno"),
    Moto_piloti.objects.get(nome="Artigas"),
    Moto_piloti.objects.get(nome="Dixon"),
    Moto_piloti.objects.get(nome="Morbidelli"),
    Moto_piloti.objects.get(nome="Rins"),
    Moto_piloti.objects.get(nome="Torres"),
    Moto_piloti.objects.get(nome="Smith")])
    formazione_paul.save()
    return HttpResponseRedirect(reverse("fantamoto"))
    


################################### MOTO #######################################
sfide_moto = [
    {"id":1, "sfida":"Cortez Black Team+Vettel05/Zanno+Cicciobirro01/Paul Bird Motorsport+Team As Turbo/Albwin27+Tazza/Dragon trainer+Alcec"},
    {"id":2, "sfida":"Tazza+Vettel05/Dragon trainer+Team As Turbo/Cicciobirro01+Alcec/Cortez Black Team+Albwin27/Paul Bird Motorsport+Zanno"},
    {"id":3, "sfida":"Vettel05+Dragon trainer/Tazza+Alcec/Team As Turbo+Albwin27/Cicciobirro01+Paul Bird Motorsport/Cortez Black Team+Zanno"},
    {"id":4, "sfida":"Albwin27+Vettel05/Alcec+Paul Bird Motorsport/Zanno+Dragon trainer/Cortez Black Team+Tazza/Team As Turbo+Cicciobirro01"},
    {"id":5, "sfida":"Vettel05+Alcec/Dragon trainer+Albwin27/Tazza+Paul Bird Motorsport/Team As Turbo+Zanno/Cicciobirro01+Cortez Black Team"},
    {"id":6, "sfida":"Team As Turbo+Vettel05/Tazza+Cicciobirro01/Dragon trainer+Cortez Black Team/Alcec+Zanno/Albwin27+Paul Bird Motorsport"},
    {"id":7, "sfida":"Zanno+Vettel05/Paul Bird Motorsport+Cortez Black Team/Albwin27+Cicciobirro01/Alcec+Team As Turbo/Dragon trainer+Tazza"},
    {"id":8, "sfida":"Paul Bird Motorsport+Vettel05/Zanno+Albwin27/Cortez Black Team+Alcec/Cicciobirro01+Dragon trainer/Team As Turbo+Tazza"},
    {"id":9, "sfida":"Vettel05+Cicciobirro01/Cortez Black Team+Team As Turbo/Zanno+Tazza/Paul Bird Motorsport+Dragon trainer/Albwin27+Alcec"},
    {"id":10, "sfida":"Cortez Black Team+Vettel05/Zanno+Cicciobirro01/Paul Bird Motorsport+Team As Turbo/Albwin27+Tazza/Dragon trainer+Alcec"},
    {"id":11, "sfida":"Tazza+Vettel05/Dragon trainer+Team As Turbo/Cicciobirro01+Alcec/Cortez Black Team+Albwin27/Paul Bird Motorsport+Zanno"},
    {"id":12, "sfida":"Vettel05+Dragon trainer/Tazza+Alcec/Team As Turbo+Albwin27/Cicciobirro01+Paul Bird Motorsport/Cortez Black Team+Zanno"},
    {"id":13, "sfida":"Albwin27+Vettel05/Alcec+Paul Bird Motorsport/Zanno+Dragon trainer/Cortez Black Team+Tazza/Team As Turbo+Cicciobirro01"},
    {"id":14, "sfida":"Vettel05+Alcec/Dragon trainer+Albwin27/Tazza+Paul Bird Motorsport/Team As Turbo+Zanno/Cicciobirro01+Cortez Black Team"},
    {"id":15, "sfida":"Team As Turbo+Vettel05/Tazza+Cicciobirro01/Dragon trainer+Cortez Black Team/Alcec+Zanno/Albwin27+Paul Bird Motorsport"},
    {"id":16, "sfida":"Zanno+Vettel05/Paul Bird Motorsport+Cortez Black Team/Albwin27+Cicciobirro01/Alcec+Team As Turbo/Dragon trainer+Tazza"},
    {"id":17, "sfida":"Paul Bird Motorsport+Vettel05/Zanno+Albwin27/Cortez Black Team+Alcec/Cicciobirro01+Dragon trainer/Team As Turbo+Tazza"},
    {"id":18, "sfida":"Vettel05+Cicciobirro01/Cortez Black Team+Team As Turbo/Zanno+Tazza/Paul Bird Motorsport+Dragon trainer/Albwin27+Alcec"},
    {"id":19, "sfida":"Cortez Black Team+Vettel05/Zanno+Cicciobirro01/Paul Bird Motorsport+Team As Turbo/Albwin27+Tazza/Dragon trainer+Alcec"},
    {"id":20, "sfida":"Tazza+Vettel05/Dragon trainer+Team As Turbo/Cicciobirro01+Alcec/Cortez Black Team+Albwin27/Paul Bird Motorsport+Zanno"},
    {"id":21, "sfida":"Vettel05+Dragon trainer/Tazza+Alcec/Team As Turbo+Albwin27/Cicciobirro01+Paul Bird Motorsport/Cortez Black Team+Zanno"},
    {"id":22, "sfida":"Albwin27+Vettel05/Alcec+Paul Bird Motorsport/Zanno+Dragon trainer/Cortez Black Team+Tazza/Team As Turbo+Cicciobirro01"},
    {"id":23, "sfida":"Vettel05+Alcec/Dragon trainer+Albwin27/Tazza+Paul Bird Motorsport/Team As Turbo+Zanno/Cicciobirro01+Cortez Black Team"},
]

team_moto = [
    {"nome": "Aprilia Racing", "piloti": "Espargaro A./Viñales M.", "cat": "motogp"},
    {"nome": "Ducati (MotoGP)", "piloti": "Bagnaia/Bastianini", "cat": "motogp"},
    {"nome": "GASGAS Racing (MotoGP)", "piloti": "Espargaro P./Fernandez A.", "cat": "motogp"},
    {"nome": "Gresini Racing (MotoGP)", "piloti": "Marquez A./Di Giannantonio", "cat": "motogp"},
    {"nome": "LCR Honda", "piloti": "Rins/Nakagami", "cat": "motogp"},
    {"nome": "Yamaha", "piloti": "Quartararo/Morbidelli", "cat": "motogp"},
    {"nome": "VR46 Racing (MotoGP)", "piloti": "Marini/Bezzecchi", "cat": "motogp"},
    {"nome": "Pramac Racing (MotoGP)", "piloti": "Zarco/Martin", "cat": "motogp"},
    {"nome": "Red Bull KTM (MotoGP)", "piloti": "Miller/Binder B.", "cat": "motogp"},
    {"nome": "Honda", "piloti": "Marquez M./Mir", "cat": "motogp"},
    {"nome": "RNF Racing (MotoGP)", "piloti": "Oliveira/Fernandez R.", "cat": "motogp"},
    {"nome": "American Racing", "piloti": "Kelly/Skinner", "cat": "moto2"},
    {"nome": "Marc VDS Racing", "piloti": "Arbolino/Lowes S.", "cat": "moto2"},
    {"nome": "Fantic Motor", "piloti": "Vietti/Gomez", "cat": "moto2"},
    {"nome": "Flexbox HP40", "piloti": "Garcia/Canet", "cat": "moto2"},
    {"nome": "GASGAS Racing (Moto2)", "piloti": "Guevara/Dixon", "cat": "moto2"},
    {"nome": "Gresini Racing (Moto2)", "piloti": "Salac/Alcoba", "cat": "moto2"},
    {"nome": "Honda Team Asia (Moto2)", "piloti": "Chantra/Ogura", "cat": "moto2"},
    {"nome": "Italtrans Racing", "piloti": "Roberts/Foggia", "cat": "moto2"},
    {"nome": "Husqvarna Intact (Moto2)", "piloti": "Tulovic/Binder D.", "cat": "moto2"},
    {"nome": "Agusta Forward", "piloti": "Escrig/Ramirez", "cat": "moto2"},
    {"nome": "SAG Team", "piloti": "Dalla Porta/Bendsneyder", "cat": "moto2"},
    {"nome": "Red Bull KTM Ajo (Moto2)", "piloti": "Acosta/Arenas", "cat": "moto2"},
    {"nome": "RW Racing", "piloti": "Baltus/Van den Goorbergh", "cat": "moto2"},
    {"nome": "Speed Up Racing", "piloti": "Lopez/Aldeguer", "cat": "moto2"},
    {"nome": "VR46 Racing (Moto2)", "piloti": "Nozane/Gonzalez", "cat": "moto2"},
    {"nome": "MTA Team", "piloti": "Ortola/Nepa", "cat": "moto3"},
    {"nome": "BOE Motorsports", "piloti": "Carrasco/Muñoz", "cat": "moto3"},
    {"nome": "Pruestel Racing", "piloti": "Artigas/Kelso", "cat": "moto3"},
    {"nome": "CIP Green Power", "piloti": "Fellon/Salvador", "cat": "moto3"},
    {"nome": "GASGAS Racing (Moto3)", "piloti": "Yamanaka/Alonso", "cat": "moto3"},
    {"nome": "Honda Team Asia (Moto3)", "piloti": "Aji/Furusato", "cat": "moto3"},
    {"nome": "Leopard Racing", "piloti": "Masia/Suzuki", "cat": "moto3"},
    {"nome": "Husqvarna Intact (Moto3)", "piloti": "Sasaki/Veijer", "cat": "moto3"},
    {"nome": "MT Helmets", "piloti": "Moreira/Azman", "cat": "moto3"},
    {"nome": "Red Bull KTM Ajo (Moto3)", "piloti": "Oncu/Rueda", "cat": "moto3"},
    {"nome": "Red Bull KTM (Moto3)", "piloti": "Farioli", "cat": "moto3"},
    {"nome": "Snipers Team", "piloti": "Bertelle/Fenati", "cat": "moto3"},
    {"nome": "SIC58 Squadra (Moto3)", "piloti": "Toba/Rossi", "cat": "moto3"},
    {"nome": "Visiontrack Racing", "piloti": "Ogden/Whatley", "cat": "moto3"},
    {"nome": "Intact GP", "piloti": "Garzo/Krummenacher", "cat": "motoe"},
    {"nome": "LCR E-Team ", "piloti": "Granado (MotoE)/Pons", "cat": "motoe"},
    {"nome": "Aspar Team", "piloti": "Torres/Herrera", "cat": "motoe"},
    {"nome": "Gresini Racing (MotoE)", "piloti": "Finello/Ferrari", "cat": "motoe"},
    {"nome": "Tech3 E-Racing", "piloti": "Zaccone/Okubo", "cat": "motoe"},
    {"nome": "RNF Racing (MotoE)", "piloti": "Mantovani/Perez", "cat": "motoe"},
    {"nome": "SIC58 Squadra (MotoE)", "piloti": "Zannoni/Manfredi", "cat": "motoe"},
    {"nome": "Pons Racing", "piloti": "Casadei/Spinelli", "cat": "motoe"},
    {"nome": "Pramac Racing (MotoE)(1)", "piloti": "Salvadori/Rabat", "cat": "motoe"},
    {"nome": "Pramac Racing (MotoE)(2)", "piloti": "Salvadori/Rabat", "cat": "motoe"},
    {"nome": "Ducati (SBK)", "piloti": "Bautista/Rinaldi", "cat": "sbk"},
    {"nome": "GoEleven", "piloti": "Oettl", "cat": "sbk"},
    {"nome": "HRC Honda", "piloti": "Lecuona/Vierge", "cat": "sbk"},
    {"nome": "Barni Spark Racing", "piloti": "Petrucci", "cat": "sbk"},
    {"nome": "Kawasaki Racing", "piloti": "Rea/Lowes A.", "cat": "sbk"},
    {"nome": "MotoXRacing Yamaha", "piloti": "Ray", "cat": "sbk"},
    {"nome": "Bonovo Action", "piloti": "Gerloff/Baz", "cat": "sbk"},
    {"nome": "GMT94 Yamaha", "piloti": "Baldassarri", "cat": "sbk"},
    {"nome": "MIE Racing Honda", "piloti": "Syahrin", "cat": "sbk"},
    {"nome": "Rokit BMW Motorrad", "piloti": "Redding/Van der Mark", "cat": "sbk"},
    {"nome": "Motocorsa Racing", "piloti": "Bassani", "cat": "sbk"},
    {"nome": "Orelac Racing", "piloti": "Konig", "cat": "sbk"},
    {"nome": "Pata Yamaha", "piloti": "Razgatlioglu/Locatelli", "cat": "sbk"},
    {"nome": "Puccetti Racing", "piloti": "Sykes", "cat": "sbk"},
    {"nome": "GYTR Yamaha", "piloti": "Gardner/Aegerter", "cat": "sbk"},
    {"nome": "Padercini Team", "piloti": "Viñales I.", "cat": "sbk"},
]

tm_moto = [
    {"nome": "Tardozzi (Ducati)", "piloti": "Bagnaia/Bastianini"},
    {"nome": "Borsoi (Pramac)", "piloti": "Zarco/Martin"},
    {"nome": "Rivola (Aprilia)", "piloti": "Espargaro A./Viñales M."},
    {"nome": "Guidotti (KTM)", "piloti": "Miller/Binder B."},
    {"nome": "Jarvis (Yamaha)", "piloti": "Quartararo/Morbidelli"},
    {"nome": "Nieto (VR46)", "piloti": "Marini/Bezzecchi"},
    {"nome": "Puig (Honda)", "piloti": "Marquez M./Mir"},
    {"nome": "Nadia (Gresini)", "piloti": "Marquez A./Di Giannantonio"},
    {"nome": "Cecchinello (LCR)", "piloti": "Rins/Nakagami"},
    {"nome": "Bonora (RNF)", "piloti": "Oliveira/Fernandez R."},
    {"nome": "Poncharal (GASGAS)", "piloti": "Espargaro P./Fernandez A."},
]

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
        previousgara = Moto_formazione.objects.get(giornata=ultimagara.id, username=request.user.username)
    # Ritorna posizioni in classifica
    s_ranking = Moto_punti.objects.order_by("-p_scontri", "-differenza")
    p_ranking = Moto_punti.objects.order_by("-p_generali", "-differenza")
    # Cerca se hai schierato la formazione per la prossima gara
    try:
        schierata = Moto_formazione.objects.get(giornata=nextgara.id, username=request.user)
    except:
        schierata = None
    return render(request, "fantamoto/home.html", {
        "utente": request.user,
        "ultimagara": ultimagara,
        "previousgara": previousgara,
        "nextgara": nextgara,
        "s_ranking": s_ranking,
        "p_ranking": p_ranking,
        "schierata": schierata,
        "cat": "moto"
    })


@login_required
def moto_rose(request):
    tutti = User.objects.order_by("username")
    return render(request, "fantamoto/rose.html", {
        "tutti": tutti,
        "cat": "moto"
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
        "tm": team_man,
        "cat": "moto"
    })


@login_required
def moto_calendario(request):
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
    global sfide_moto
    all_id = []
    all_sfide = []
    for sfida in sfide_moto:
        all_id.append(sfida["id"])
        scontri_lista = []
        scontri = sfida["sfida"].split("/")
        for scontro in scontri:
            scontro = scontro.split("+")
            scontri_lista.append(scontro)
        all_sfide.append(scontri_lista)
    tutti = User.objects.order_by("username")
    return render(request, "fantamoto/calendario.html", {
        "giornate": giornate,
        "ultima": ultimagara,
        "sfide": all_sfide,
        "tutti": tutti,
        "cat": "moto"
    })


@login_required
def moto_scontro(request, id, scontro):
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
    # Ottieni formazione primo user
    # Cerca tutti i piloti, team e tm schierati
    try:
        piloti1 = formazione1.piloti.all()
        teams1 = formazione1.team.all()
        tm1 = formazione1.teammanager.nome
        # Se la formazione è già stata calcolata, carica i punti ottenuti da piloti,team, tm
        # Seleziona i punteggi da Moto_piloti e consegnali in una lista
        # Fa schifo ma non ho assolutamente idea di come farlo diversamente
        punti_piloti1 = []
        for pilota1 in piloti1:
            match int(id):
                case 1: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara01
                case 2: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara02
                case 3: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara03
                case 4: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara04
                case 5: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara05
                case 6: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara06
                case 7: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara07
                case 8: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara08
                case 9: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara09
                case 10: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara10
                case 11: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara11
                case 12: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara12
                case 13: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara13
                case 14: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara14
                case 15: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara15
                case 16: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara16
                case 17: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara17
                case 18: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara18
                case 19: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara19
                case 20: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara20
                case 21: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara21
                case 22: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara22
                case 23: punti_pilota1 = Moto_piloti.objects.get(nome=pilota1.nome).gara23
            if punti_pilota1:
                punti_piloti1.append(punti_pilota1)
        # Seleziona punti dei team
        punti_teams1 = []
        for team1 in teams1:
            match int(id):
                case 1: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara01
                case 2: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara02
                case 3: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara03
                case 4: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara04
                case 5: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara05
                case 6: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara06
                case 7: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara07
                case 8: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara08
                case 9: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara09
                case 10: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara10
                case 11: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara11
                case 12: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara12
                case 13: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara13
                case 14: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara14
                case 15: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara15
                case 16: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara16
                case 17: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara17
                case 18: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara18
                case 19: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara19
                case 20: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara20
                case 21: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara21
                case 22: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara22
                case 23: punti_team1 = Moto_team.objects.get(nome=team1.nome).gara23
            if punti_team1:
                punti_teams1.append(punti_team1)
        match int(id):
            case 1: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara01
            case 2: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara02
            case 3: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara03
            case 4: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara04
            case 5: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara05
            case 6: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara06
            case 7: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara07
            case 8: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara08
            case 9: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara09
            case 10: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara10
            case 11: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara11
            case 12: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara12
            case 13: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara13
            case 14: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara14
            case 15: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara15
            case 16: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara16
            case 17: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara17
            case 18: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara18
            case 19: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara19
            case 20: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara20
            case 21: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara21
            case 22: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara22
            case 23: punti_tm1 = Moto_teammanager.objects.get(nome=tm1).gara23
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
    ################## Ripeti tutto per il secondo utente ###################
    # Se formazione è schierata
    try:
        piloti2 = formazione2.piloti.all()
        teams2 = formazione2.team.all()
        tm2 = formazione2.teammanager.nome
        punti_piloti2 = []
        for pilota2 in piloti2:
            match int(id):
                case 1: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara01
                case 2: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara02
                case 3: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara03
                case 4: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara04
                case 5: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara05
                case 6: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara06
                case 7: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara07
                case 8: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara08
                case 9: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara09
                case 10: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara10
                case 11: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara11
                case 12: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara12
                case 13: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara13
                case 14: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara14
                case 15: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara15
                case 16: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara16
                case 17: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara17
                case 18: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara18
                case 19: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara19
                case 20: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara20
                case 21: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara21
                case 22: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara22
                case 23: punti_pilota2 = Moto_piloti.objects.get(nome=pilota2.nome).gara23
            if punti_pilota2:
                punti_piloti2.append(punti_pilota2)
        punti_teams2 = []
        for team2 in teams2:
            match int(id):
                case 1: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara01
                case 2: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara02
                case 3: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara03
                case 4: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara04
                case 5: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara05
                case 6: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara06
                case 7: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara07
                case 8: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara08
                case 9: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara09
                case 10: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara10
                case 11: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara11
                case 12: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara12
                case 13: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara13
                case 14: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara14
                case 15: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara15
                case 16: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara16
                case 17: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara17
                case 18: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara18
                case 19: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara19
                case 20: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara20
                case 21: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara21
                case 22: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara22
                case 23: punti_team2 = Moto_team.objects.get(nome=team2.nome).gara23
            if punti_team2:
                punti_teams2.append(punti_team2)
        match int(id):
            case 1: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara01
            case 2: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara02
            case 3: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara03
            case 4: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara04
            case 5: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara05
            case 6: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara06
            case 7: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara07
            case 8: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara08
            case 9: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara09
            case 10: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara10
            case 11: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara11
            case 12: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara12
            case 13: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara13
            case 14: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara14
            case 15: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara15
            case 16: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara16
            case 17: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara17
            case 18: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara18
            case 19: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara19
            case 20: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara20
            case 21: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara21
            case 22: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara22
            case 23: punti_tm2 = Moto_teammanager.objects.get(nome=tm2).gara23
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
    s_ranking = Moto_passato.objects.order_by("-ex_pscontri", "-ex_differenza")
    p_ranking = Moto_passato.objects.order_by("-ex_pgenerali", "-ex_differenza")
    return render(request, "fantamoto/albodoro.html", {
        "s_ranking": s_ranking,
        "p_ranking": p_ranking,
        "cat": "moto"
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
    piloti = Moto_piloti.objects.filter(username=request.user.username)
    teams = Moto_team.objects.filter(username=request.user.username)
    tm = Moto_teammanager.objects.get(username=request.user.username)
    # Ottieni gli ultimi tre risultati
    # Altro obrobrio, ma occhio non vede cuore non duole
    ultime = [nextgara.id - 1, nextgara.id - 2, nextgara.id - 3]
    # Non prendere id giornate negativo o zero
    for i in range(3):
        if ultime[i] == 0 or ultime[i] < 0:
            ultime[i] = 0
    punti_piloti = []
    for pilota in piloti:
        punti_pilota = []
        for giornata in ultime:
            match giornata:
                case 1: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara01
                case 2: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara02
                case 3: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara03
                case 4: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara04
                case 5: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara05
                case 6: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara06
                case 7: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara07
                case 8: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara08
                case 9: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara09
                case 10: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara10
                case 11: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara11
                case 12: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara12
                case 13: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara13
                case 14: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara14
                case 15: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara15
                case 16: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara16
                case 17: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara17
                case 18: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara18
                case 19: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara19
                case 20: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara20
                case 21: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara21
                case 22: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara22
                case 23: punti_g = Moto_piloti.objects.get(nome=pilota.nome).gara23
                case _: punti_g = "-"
            # Aggiungi punti delle ultime tre giornate
            try:
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
            match giornata:
                case 1: punti_g = Moto_team.objects.get(nome=team.nome).gara01
                case 2: punti_g = Moto_team.objects.get(nome=team.nome).gara02
                case 3: punti_g = Moto_team.objects.get(nome=team.nome).gara03
                case 4: punti_g = Moto_team.objects.get(nome=team.nome).gara04
                case 5: punti_g = Moto_team.objects.get(nome=team.nome).gara05
                case 6: punti_g = Moto_team.objects.get(nome=team.nome).gara06
                case 7: punti_g = Moto_team.objects.get(nome=team.nome).gara07
                case 8: punti_g = Moto_team.objects.get(nome=team.nome).gara08
                case 9: punti_g = Moto_team.objects.get(nome=team.nome).gara09
                case 10: punti_g = Moto_team.objects.get(nome=team.nome).gara10
                case 11: punti_g = Moto_team.objects.get(nome=team.nome).gara11
                case 12: punti_g = Moto_team.objects.get(nome=team.nome).gara12
                case 13: punti_g = Moto_team.objects.get(nome=team.nome).gara13
                case 14: punti_g = Moto_team.objects.get(nome=team.nome).gara14
                case 15: punti_g = Moto_team.objects.get(nome=team.nome).gara15
                case 16: punti_g = Moto_team.objects.get(nome=team.nome).gara16
                case 17: punti_g = Moto_team.objects.get(nome=team.nome).gara17
                case 18: punti_g = Moto_team.objects.get(nome=team.nome).gara18
                case 19: punti_g = Moto_team.objects.get(nome=team.nome).gara19
                case 20: punti_g = Moto_team.objects.get(nome=team.nome).gara20
                case 21: punti_g = Moto_team.objects.get(nome=team.nome).gara21
                case 22: punti_g = Moto_team.objects.get(nome=team.nome).gara22
                case 23: punti_g = Moto_team.objects.get(nome=team.nome).gara23
                case _: punti_g = "-"
            # Aggiungi punti delle ultime tre giornate
            try:
                punti_team.append(punti_g)
            except:
                punti_team.append("-")
        # Aggiungi team ai teams
        punti_teams.append(punti_team)
    # Ripeti per team manager
    punti_tm = []
    for giornata in ultime:
        match giornata:
            case 1: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara01
            case 2: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara02
            case 3: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara03
            case 4: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara04
            case 5: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara05
            case 6: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara06
            case 7: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara07
            case 8: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara08
            case 9: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara09
            case 10: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara10
            case 11: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara11
            case 12: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara12
            case 13: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara13
            case 14: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara14
            case 15: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara15
            case 16: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara16
            case 17: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara17
            case 18: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara18
            case 19: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara19
            case 20: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara20
            case 21: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara21
            case 22: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara22
            case 23: punti_g = Moto_teammanager.objects.get(nome=tm.nome).gara23
            case _: punti_g = "-"
        try:
            punti_tm.append(punti_g)
        except:
            punti_tm.append("-")
    return render(request, "fantamoto/formazione.html", {
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "nextgara": nextgara,
        "punti_piloti": punti_piloti,
        "punti_teams": punti_teams,
        "punti_tm": punti_tm,
        "cat": "moto"
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
        # Se non c'è la MotoE e la SBK
        if nextgara.motoe == 0 and nextgara.sbk == 0:
            # Controlla se 6 piloti, 3 team e tm
            if len(piloti) != 6:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 6 PILOTI, MotoE ESCLUSA.",
                    "cat": "moto"
                })
            if len(teams) != 3:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 3 TEAM, MotoE ESCLUSA.",
                    "cat": "moto"
                })
            if tm is None:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA IL TEAM MANAGER.",
                    "cat": "moto"
                })
            # Controlla le categorie dei piloti
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti or "MotoE" in categorie_piloti or "SBK" in categorie_piloti:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN PILOTA DI OGNI CATEGORIA, MotoE ESCLUSA.",
                    "cat": "moto"
                })
            # Controlla le categorie dei team
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams or "MotoE" in categorie_teams or "SBK" in categorie_teams:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI OGNI CATEGORIA, MotoE ESCLUSA.",
                    "cat": "moto"
                })
        # Stessi controlli ma con la MotoE
        elif nextgara.motoe == 1 and nextgara.sbk == 0:
            if len(piloti) != 7:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 7 PILOTI, MotoE INCLUSA.",
                    "cat": "moto"
                })
            if len(teams) != 4:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 4 TEAM, MotoE INCLUSA.",
                    "cat": "moto"
                })
            if tm is None:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA IL TEAM MANAGER.",
                    "cat": "moto"
                })
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti or "MotoE" not in categorie_piloti or "SBK" in categorie_piloti:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN PILOTA DI OGNI CATEGORIA, MotoE INCLUSA.",
                    "cat": "moto"
                })
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams or "MotoE" not in categorie_teams or "SBK" in categorie_teams:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI OGNI CATEGORIA, MotoE INCLUSA.",
                    "cat": "moto"
                })
        # Stessi controlli ma con la SBK
        elif nextgara.motoe == 0 and nextgara.sbk == 1:
            if len(piloti) != 7:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 7 PILOTI, SBK INCLUSA.",
                    "cat": "moto"
                })
            if len(teams) != 4:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 4 TEAM, SBK INCLUSA.",
                    "cat": "moto"
                })
            if tm is None:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA IL TEAM MANAGER.",
                    "cat": "moto"
                })
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti or "MotoE" in categorie_piloti or "SBK" not in categorie_piloti:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN PILOTA DI OGNI CATEGORIA, SBK INCLUSA.",
                    "cat": "moto"
                })
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams or "MotoE" in categorie_teams or "SBK" not in categorie_teams:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI OGNI CATEGORIA, SBK INCLUSA.",
                    "cat": "moto"
                })
        # Stessi controlli ma con la MotoE e SBK
        elif nextgara.motoe == 1 and nextgara.sbk == 1:
            if len(piloti) != 8:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 8 PILOTI, MotoE e SBK INCLUSE.",
                    "cat": "moto"
                })
            if len(teams) != 5:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 5 TEAM, MotoE e SBK INCLUSA.",
                    "cat": "moto"
                })
            if tm is None:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA IL TEAM MANAGER.",
                    "cat": "moto"
                })
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "Moto3" not in categorie_piloti or "Moto2" not in categorie_piloti or "MotoGP" not in categorie_piloti or "MotoE" not in categorie_piloti or "SBK" not in categorie_piloti:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN PILOTA DI OGNI CATEGORIA, MotoE e SBK INCLUSA.",
                    "cat": "moto"
                })
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "Moto3" not in categorie_teams or "Moto2" not in categorie_teams or "MotoGP" not in categorie_teams or "MotoE" not in categorie_teams or "SBK" not in categorie_teams:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI OGNI CATEGORIA, MotoE e SBK INCLUSA.",
                    "cat": "moto"
                })
        # Controlla che il capitano scelto sia stato schierato nella formazione
        for pilota in piloti:
            check_capitano.append(pilota.split(" - ")[0])
        if capitano not in check_capitano and capitano != "0":
            return render(request, "errore.html", {
                "message": "FORMAZIONE NON SCHIERATA: CAPITANO ASSENTE DALLA FORMAZIONE SCHIERATA.",
                "cat": "moto"
            })
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
        formazione_tm = Moto_teammanager.objects.get(nome=tm)
        formazione_user = request.user
        # Seleziona il capitano (oppure trascuralo)
        if capitano != "0":
            formazione_capitano = Moto_piloti.objects.get(nome=capitano)
        else:
            formazione_capitano = None
        # Salva la formazione nel database
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
        # Rispedisci alla home
        return HttpResponseRedirect(reverse("fantamoto"))


@login_required
def moto_calcoloscelta(request):
    autorizzati = [1, 3]
    if request.user.id not in autorizzati:
        return render(request, "errore.html", {
            "message": "Non sei autorizzato al calcolo delle giornate",
            "cat": "moto",
        })
    giornate = Moto_giornata.objects.all()
    return render(request, "fantamoto/calcolo_scelta.html", {
        "giornate": giornate,
        "cat": "moto"
    })


@login_required
def moto_calcologara(request, id):
    # Se non autorizzati, mostra errore
    autorizzati = [1, 3]
    if request.user.id not in autorizzati:
        return render(request, "errore.html", {
            "message": "Non sei autorizzato al calcolo delle giornate",
            "cat": "moto",
        })

    # Se si sta facendo una richiesta POST, calcola i risultati
    # Aiutatemi che questa sarà lunga
    if request.method == "POST":
        # Se in qualche modo giornata già calcolata, manda errore
        if Moto_giornata.objects.get(id=id).calcolata:
            return render(request, "errore.html", {
                "message": "HAI GIÀ CALCOLATO QUESTA GIORNATA ._.",
                "cat": "moto"
            })
        # Ottieni tutte le formazioni schierate
        utenti = [user for user in User.objects.all()]
        formazioni = []
        for utente in utenti:
            # Ottieni formazione
            try:
                formazione = Moto_formazione.objects.get(username=utente.username, giornata=id)
            # Se non è stata schierata, creane una vuota
            except:
                print(f"manca a {utente.username}")
                formazione = Moto_formazione.objects.create(
                    giornata = id,
                    data = timezone.localtime(),
                    username = utente.username,
                    utente = utente)
                formazione.save()
            formazioni.append(formazione)
        # Prendi tutte le info ricevute da POST e dividile tra attributo e valore
        ricevuto = request.POST.items()
        se_motoe = Moto_giornata.objects.get(id=id).motoe
        se_sbk = Moto_giornata.objects.get(id=id).sbk
        var_moto3 = []
        var_moto2 = []
        var_motogp = []
        if se_motoe:
            var_motoe = []
        if se_sbk:
            var_sbk = []
        for key, value in ricevuto:
            try:
                attributi = key.split("-")
                match attributi[-2]:
                    case "3": var_moto3.append([key, value])
                    case "2": var_moto2.append([key, value])
                    case "gp": var_motogp.append([key, value])
                    case "e": var_motoe.append([key, value])
                    case "sbk": var_sbk.append([key, value])
                    case _: pass
            except:
                pass

        # Prima cerchiamo tutti gli errori possibili per ogni categoria
        check_quali3 = []
        check_feat3 = []
        fl3_count = 0
        for variabile in var_moto3:
            # Controlla che non ci siano più di un pilota qualificato alla stessa posizione
            if variabile[0].startswith("quali-"):
                if variabile[1] in check_quali3:
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In Moto3, più piloti hanno la stessa posizione in qualifica.",
                        "cat": "moto"
                    })
                else:
                    check_quali3.append(variabile[1])
            # Controlla che non ci siano più di un pilota arrivato alla stessa posizione in gara
            if variabile[0].startswith("feat-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                if variabile[1] in check_feat3 and variabile[1] != "":
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In Moto3, più piloti hanno la stessa posizione nella Feature Race.",
                        "cat": "moto"
                    })
                else:
                    check_feat3.append(variabile[1])
            # Controlla che non ci siano più Fast Lap o nessun Fast Lap
            if variabile[0].startswith("feat-fl-"):
                fl3_count += 1
        if fl3_count != 1:
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In Moto3, ci sono nessun o più Fast Lap.",
                "cat": "moto"
            })
        if not all(value in ["1", "2", "3"] for value in check_quali3):
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In Moto3, non sono state selezionate le prime 3 posizioni della qualifica.",
                "cat": "moto"
            })
        # Moto2 Errori
        check_quali2 = []
        check_feat2 = []
        fl2_count = 0
        for variabile in var_moto2:
            if variabile[0].startswith("quali-"):
                if variabile[1] in check_quali2:
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In Moto2, più piloti hanno la stessa posizione in qualifica.",
                        "cat": "moto"
                    })
                else:
                    check_quali2.append(variabile[1])
            if variabile[0].startswith("feat-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                if variabile[1] in check_feat2 and variabile[1] != "":
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In Moto2, più piloti hanno la stessa posizione nella Feature Race.",
                        "cat": "moto"
                    })
                else:
                    check_feat2.append(variabile[1])
            if variabile[0].startswith("feat-fl-"):
                fl2_count += 1
        if fl2_count != 1:
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In Moto2, ci sono nessun o più Fast Lap.",
                "cat": "moto"
            })
        if not all(value in ["1", "2", "3"] for value in check_quali2):
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In Moto2, non sono state selezionate le prime 3 posizioni della qualifica.",
                "cat": "moto"
            })
        # MotoGP Errori
        check_qualigp = []
        check_sprgp = []
        check_featgp = []
        spr_flgp_count = 0
        feat_flgp_count = 0
        for variabile in var_motogp:
            if variabile[0].startswith("quali-"):
                if variabile[1] in check_qualigp:
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In MotoGP, più piloti hanno la stessa posizione in qualifica.",
                        "cat": "moto"
                    })
                else:
                    check_qualigp.append(variabile[1])
            if variabile[0].startswith("spr-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                if variabile[1] in check_sprgp and variabile[1] != "":
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In MotoGP, più piloti hanno la stessa posizione nella Sprint Race.",
                        "cat": "moto"
                    })
                else:
                    check_sprgp.append(variabile[1])
            if variabile[0].startswith("feat-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                if variabile[1] in check_featgp and variabile[1] != "":
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In MotoGP, più piloti hanno la stessa posizione nella Feature Race.",
                        "cat": "moto"
                    })
                else:
                    check_featgp.append(variabile[1])
            if variabile[0].startswith("spr-fl"):
                spr_flgp_count += 1
            if variabile[0].startswith("feat-fl-"):
                feat_flgp_count += 1
        if spr_flgp_count != 1:
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In MotoGP, ci sono nessun o più Fast Lap nella Sprint Race.",
            })
        if feat_flgp_count != 1:
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In MotoGP, ci sono nessun o più Fast Lap nella Feature Race.",
                "cat": "moto"
            })
        if not all(value in ["1", "2", "3"] for value in check_qualigp):
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In MotoGP, non sono state selezionate le prime 3 posizioni della qualifica.",
                "cat": "moto"
            })
        # MotoE Errori
        if se_motoe:
            check_qualie = []
            check_g1e = []
            check_g2e = []
            g1_fle_count = 0
            g2_fle_count = 0
            for variabile in var_motoe:
                if variabile[0].startswith("quali-"):
                    if variabile[1] in check_qualie:
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In MotoE, più piloti hanno la stessa posizione in qualifica.",
                            "cat": "moto"
                        })
                    else:
                        check_qualie.append(variabile[1])
                if variabile[0].startswith("g1-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                    if variabile[1] in check_g1e and variabile[1] != "":
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In MotoE, più piloti hanno la stessa posizione nella Gara 1.",
                            "cat": "moto"
                        })
                    else:
                        check_g1e.append(variabile[1])
                if variabile[0].startswith("g2-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                    if variabile[1] in check_g2e and variabile[1] != "":
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In MotoE, più piloti hanno la stessa posizione nella Gara 2.",
                            "cat": "moto"
                        })
                    else:
                        check_g2e.append(variabile[1])
                if variabile[0].startswith("g1-fl"):
                    g1_fle_count += 1
                if variabile[0].startswith("g2-fl-"):
                    g2_fle_count += 1
            if g1_fle_count != 1:
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In MotoE, ci sono nessun o più Fast Lap nella Gara 1.",
                    "cat": "moto"
                })
            if g2_fle_count != 1:
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In MotoE, ci sono nessun o più Fast Lap nella Gara 2.",
                    "cat": "moto"
                })
            if not all(value in ["1", "2", "3"] for value in check_qualie):
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In MotoE, non sono state selezionate le prime 3 posizioni della qualifica.",
                    "cat": "moto"
                })
        # SBK Errori
        if se_sbk:
            check_qualisbk = []
            check_g1sbk = []
            check_supersbk = []
            check_g2sbk = []
            g1_flsbk_count = 0
            super_flsbk_count = 0
            g2_flsbk_count = 0
            for variabile in var_sbk:
                if variabile[0].startswith("quali-"):
                    if variabile[1] in check_qualisbk:
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In SBK, più piloti hanno la stessa posizione in qualifica.",
                            "cat": "moto"
                        })
                    else:
                        check_qualisbk.append(variabile[1])
                if variabile[0].startswith("g1-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                    if variabile[1] in check_g1sbk and variabile[1] != "":
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In SBK, più piloti hanno la stessa posizione nella Gara 1.",
                            "cat": "moto"
                        })
                    else:
                        check_g1sbk.append(variabile[1])
                if variabile[0].startswith("sup-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                    if variabile[1] in check_supersbk and variabile[1] != "":
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In SBK, più piloti hanno la stessa posizione nella SuperPole.",
                            "cat": "moto"
                        })
                    else:
                        check_supersbk.append(variabile[1])
                if variabile[0].startswith("g2-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                    if variabile[1] in check_g2sbk and variabile[1] != "":
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In SBK, più piloti hanno la stessa posizione nella Gara 2.",
                            "cat": "moto"
                        })
                    else:
                        check_g2sbk.append(variabile[1])
                if variabile[0].startswith("g1-fl"):
                    g1_flsbk_count += 1
                if variabile[0].startswith("sup-fl"):
                    super_flsbk_count += 1
                if variabile[0].startswith("g2-fl-"):
                    g2_flsbk_count += 1
            if g1_flsbk_count != 1:
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In SBK, ci sono nessun o più Fast Lap nella Gara 1.",
                    "cat": "moto"
                })
            if super_flsbk_count != 1:
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In SBK, ci sono nessun o più Fast Lap nella SuperPole.",
                    "cat": "moto"
                })
            if g2_flsbk_count != 1:
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In SBK, ci sono nessun o più Fast Lap nella Gara 2.",
                    "cat": "moto"
                })
            if not all(value in ["1", "2", "3"] for value in check_qualisbk):
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In SBK, non sono state selezionate le prime 3 posizioni della qualifica.",
                    "cat": "moto"
                })
        
        # Sistemiamo bene i valori ricevuti
        # Creiamo un dizionario per ogni pilota di ogni categoria e i valori corrispettivi
        tutti_piloti3 = Moto_piloti.objects.filter(categoria="Moto3").order_by("nome")
        tutti_piloti2 = Moto_piloti.objects.filter(categoria="Moto2").order_by("nome")
        tutti_pilotigp = Moto_piloti.objects.filter(categoria="MotoGP").order_by("nome")
        if se_motoe:
            tutti_pilotie = Moto_piloti.objects.filter(categoria="MotoE").order_by("nome")
        if se_sbk:
            tutti_pilotisbk = Moto_piloti.objects.filter(categoria="SBK").order_by("nome")
        # Moto3
        tutti_moto3 = []
        for pilota in tutti_piloti3:
            utente = {"nome": pilota.nome, 
                "categoria": "Moto3",
                "qualifica": 0,
                "feature": 0,
                "feature-dnf": 0,
                "feature-fl": 0,
            }
            utente.setdefault("punti", 0)
            utente.setdefault("punti_team", 0)
            for variabile in var_moto3:
                modificatore = variabile[0].split("-")
                if modificatore[-1] == pilota.nome:
                    if modificatore[0] == "quali":
                        utente["qualifica"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "gara":
                        if variabile[1] != "":
                            utente["feature"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "dnf":
                        utente["feature-dnf"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "fl":
                        utente["feature-fl"] = int(variabile[1])
            tutti_moto3.append(utente)  
        # Moto2
        tutti_moto2 = []
        for pilota in tutti_piloti2:
            utente = {"nome": pilota.nome, 
                "categoria": "Moto2",
                "qualifica": 0,
                "feature": 0,
                "feature-dnf": 0,
                "feature-fl": 0,
            }
            utente.setdefault("punti", 0)
            utente.setdefault("punti_team", 0)
            for variabile in var_moto2:
                modificatore = variabile[0].split("-")
                if modificatore[-1] == pilota.nome:
                    if modificatore[0] == "quali":
                        utente["qualifica"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "gara":
                        if variabile[1] != "":
                            utente["feature"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "dnf":
                        utente["feature-dnf"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "fl":
                        utente["feature-fl"] = int(variabile[1])
            tutti_moto2.append(utente)
        # MotoGP
        tutti_motogp = []
        for pilota in tutti_pilotigp:
            utente = {"nome": pilota.nome, 
                "categoria": "MotoGP",
                "qualifica": 0,
                "sprint": 0,
                "sprint-dnf": 0,
                "sprint-fl": 0,
                "feature": 0,
                "feature-dnf": 0,
                "feature-fl": 0,
            }
            utente.setdefault("punti", 0)
            utente.setdefault("punti_team", 0)
            for variabile in var_motogp:
                modificatore = variabile[0].split("-")
                if modificatore[-1] == pilota.nome:
                    if modificatore[0] == "quali":
                        utente["qualifica"] = int(variabile[1])
                    elif modificatore[0] == "spr" and modificatore[1] == "gara":
                        if variabile[1] != "":
                            utente["sprint"] = int(variabile[1])
                    elif modificatore[0] == "spr" and modificatore[1] == "dnf":
                        utente["sprint-dnf"] = int(variabile[1])
                    elif modificatore[0] == "spr" and modificatore[1] == "fl":
                        utente["sprint-fl"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "gara":
                        if variabile[1] != "":
                            utente["feature"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "dnf":
                        utente["feature-dnf"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "fl":
                        utente["feature-fl"] = int(variabile[1])
            tutti_motogp.append(utente)
        # MotoE
        if se_motoe:
            tutti_motoe = []
            for pilota in tutti_pilotie:
                utente = {"nome": pilota.nome, 
                    "categoria": "MotoE",
                    "qualifica": 0,
                    "gara1": 0,
                    "gara1-dnf": 0,
                    "gara1-fl": 0,
                    "gara2": 0,
                    "gara2-dnf": 0,
                    "gara2-fl": 0,
                }
                utente.setdefault("punti", 0)
                utente.setdefault("punti_team", 0)
                for variabile in var_motoe:
                    modificatore = variabile[0].split("-")
                    if modificatore[-1] == pilota.nome:
                        if modificatore[0] == "quali":
                            utente["qualifica"] = int(variabile[1])
                        elif modificatore[0] == "g1" and modificatore[1] == "gara":
                            if variabile[1] != "":
                                utente["gara1"] = int(variabile[1])
                        elif modificatore[0] == "g1" and modificatore[1] == "dnf":
                            utente["gara1-dnf"] = int(variabile[1])
                        elif modificatore[0] == "g1" and modificatore[1] == "fl":
                            utente["gara1-fl"] = int(variabile[1])
                        elif modificatore[0] == "g2" and modificatore[1] == "gara":
                            if variabile[1] != "":
                                utente["gara2"] = int(variabile[1])
                        elif modificatore[0] == "g2" and modificatore[1] == "dnf":
                            utente["gara2-dnf"] = int(variabile[1])
                        elif modificatore[0] == "g2" and modificatore[1] == "fl":
                            utente["gara2-fl"] = int(variabile[1])
                tutti_motoe.append(utente)
        # SBK
        if se_sbk:
            tutti_motosbk = []
            for pilota in tutti_pilotisbk:
                utente = {"nome": pilota.nome, 
                    "categoria": "SBK",
                    "qualifica": 0,
                    "gara1": 0,
                    "gara1-dnf": 0,
                    "gara1-fl": 0,
                    "super": 0,
                    "super-dnf": 0,
                    "super-fl": 0,
                    "gara2": 0,
                    "gara2-dnf": 0,
                    "gara2-fl": 0,
                }
                utente.setdefault("punti", 0)
                utente.setdefault("punti_team", 0)
                for variabile in var_sbk:
                    modificatore = variabile[0].split("-")
                    if modificatore[-1] == pilota.nome:
                        if modificatore[0] == "quali":
                            utente["qualifica"] = int(variabile[1])
                        elif modificatore[0] == "g1" and modificatore[1] == "gara":
                            if variabile[1] != "":
                                utente["gara1"] = int(variabile[1])
                        elif modificatore[0] == "g1" and modificatore[1] == "dnf":
                            utente["gara1-dnf"] = int(variabile[1])
                        elif modificatore[0] == "g1" and modificatore[1] == "fl":
                            utente["gara1-fl"] = int(variabile[1])
                        elif modificatore[0] == "sup" and modificatore[1] == "gara":
                            if variabile[1] != "":
                                utente["super"] = int(variabile[1])
                        elif modificatore[0] == "sup" and modificatore[1] == "dnf":
                            utente["super-dnf"] = int(variabile[1])
                        elif modificatore[0] == "sup" and modificatore[1] == "fl":
                            utente["super-fl"] = int(variabile[1])
                        elif modificatore[0] == "g2" and modificatore[1] == "gara":
                            if variabile[1] != "":
                                utente["gara2"] = int(variabile[1])
                        elif modificatore[0] == "g2" and modificatore[1] == "dnf":
                            utente["gara2-dnf"] = int(variabile[1])
                        elif modificatore[0] == "g2" and modificatore[1] == "fl":
                            utente["gara2-fl"] = int(variabile[1])
                tutti_motosbk.append(utente)
        if se_motoe and se_sbk:
            tutti = {
                "moto3": tutti_moto3,
                "moto2": tutti_moto2,
                "motogp": tutti_motogp,
                "motoe": tutti_motoe,
                "sbk": tutti_motosbk
            }
        elif se_motoe and not se_sbk:
            tutti = {
                "moto3": tutti_moto3,
                "moto2": tutti_moto2,
                "motogp": tutti_motogp,
                "motoe": tutti_motoe
            }
        elif not se_motoe and se_sbk:
            tutti = {
                "moto3": tutti_moto3,
                "moto2": tutti_moto2,
                "motogp": tutti_motogp,
                "sbk": tutti_motosbk
            }
        else:
            tutti = {
                "moto3": tutti_moto3,
                "moto2": tutti_moto2,
                "motogp": tutti_motogp
            }
        
        # È arrivato il momento di calcolare
        # Moto3
        for utente in tutti["moto3"]:
            # Se non DNF, aggiungi punti gara al pilota 
            if not utente["feature-dnf"]:
                if utente["feature"] == 1:
                    utente["punti"] += 25
                    utente["punti_team"] += 25
                elif utente["feature"] == 2:
                    utente["punti"] += 20
                    utente["punti_team"] += 20
                elif utente["feature"] == 3:
                    utente["punti"] += 16
                    utente["punti_team"] += 16
                elif utente["feature"] == 4:
                    utente["punti"] += 13
                    utente["punti_team"] += 13
                elif utente["feature"] == 5:
                    utente["punti"] += 11
                    utente["punti_team"] += 11
                elif utente["feature"] == 6:
                    utente["punti"] += 10
                    utente["punti_team"] += 10
                elif utente["feature"] == 7:
                    utente["punti"] += 9
                    utente["punti_team"] += 9
                elif utente["feature"] == 8:
                    utente["punti"] += 8
                    utente["punti_team"] += 8
                elif utente["feature"] == 9:
                    utente["punti"] += 7
                    utente["punti_team"] += 7
                elif utente["feature"] == 10:
                    utente["punti"] += 6
                    utente["punti_team"] += 6
                elif utente["feature"] == 11:
                    utente["punti"] += 5
                    utente["punti_team"] += 5
                elif utente["feature"] == 12:
                    utente["punti"] += 4
                    utente["punti_team"] += 4
                elif utente["feature"] == 13:
                    utente["punti"] += 3
                    utente["punti_team"] += 3
                elif utente["feature"] == 14:
                    utente["punti"] += 2
                    utente["punti_team"] += 2
                elif utente["feature"] == 15:
                    utente["punti"] += 1
                    utente["punti_team"] += 1
            # Se non cade, dai punti giro veloce splo al pilota
                if utente["feature-fl"]:
                    utente["punti"] += 2
            # Indifferentemente se cade o meno, assegna solo al pilota i punti della qualifica
            if utente["qualifica"] in [1, 2, 3]:
                match utente["qualifica"]:
                    case 1: utente["punti"] += 5
                    case 2: utente["punti"] += 3
                    case 3: utente["punti"] += 1
        # Moto2
        for utente in tutti["moto2"]:
            if not utente["feature-dnf"]:
                if utente["feature"] == 1:
                    utente["punti"] += 25
                    utente["punti_team"] += 25
                elif utente["feature"] == 2:
                    utente["punti"] += 20
                    utente["punti_team"] += 20
                elif utente["feature"] == 3:
                    utente["punti"] += 16
                    utente["punti_team"] += 16
                elif utente["feature"] == 4:
                    utente["punti"] += 13
                    utente["punti_team"] += 13
                elif utente["feature"] == 5:
                    utente["punti"] += 11
                    utente["punti_team"] += 11
                elif utente["feature"] == 6:
                    utente["punti"] += 10
                    utente["punti_team"] += 10
                elif utente["feature"] == 7:
                    utente["punti"] += 9
                    utente["punti_team"] += 9
                elif utente["feature"] == 8:
                    utente["punti"] += 8
                    utente["punti_team"] += 8
                elif utente["feature"] == 9:
                    utente["punti"] += 7
                    utente["punti_team"] += 7
                elif utente["feature"] == 10:
                    utente["punti"] += 6
                    utente["punti_team"] += 6
                elif utente["feature"] == 11:
                    utente["punti"] += 5
                    utente["punti_team"] += 5
                elif utente["feature"] == 12:
                    utente["punti"] += 4
                    utente["punti_team"] += 4
                elif utente["feature"] == 13:
                    utente["punti"] += 3
                    utente["punti_team"] += 3
                elif utente["feature"] == 14:
                    utente["punti"] += 2
                    utente["punti_team"] += 2
                elif utente["feature"] == 15:
                    utente["punti"] += 1
                    utente["punti_team"] += 1
                if utente["feature-fl"]:
                    utente["punti"] += 2
            if utente["qualifica"] in [1,2,3]:
                match utente["qualifica"]:
                    case 1: utente["punti"] += 5
                    case 2: utente["punti"] += 3
                    case 3: utente["punti"] += 1
        # MotoGP
        # Liste che servono per controllare i DNF e quindi i Team Manager dopo
        caduti_sprint = []
        caduti_feature = []
        for utente in tutti["motogp"]: 
            # Sprint
            if not utente["sprint-dnf"]:
                if utente["sprint"] == 1:
                    utente["punti"] += 12
                    utente["punti_team"] += 12
                elif utente["sprint"] == 2:
                    utente["punti"] += 9
                    utente["punti_team"] += 9
                elif utente["sprint"] == 3:
                    utente["punti"] += 7
                    utente["punti_team"] += 7
                elif utente["sprint"] == 4:
                    utente["punti"] += 6
                    utente["punti_team"] += 6
                elif utente["sprint"] == 5:
                    utente["punti"] += 5
                    utente["punti_team"] += 5
                elif utente["sprint"] == 6:
                    utente["punti"] += 4
                    utente["punti_team"] += 4
                elif utente["sprint"] == 7:
                    utente["punti"] += 3
                    utente["punti_team"] += 3
                elif utente["sprint"] == 8:
                    utente["punti"] += 2
                    utente["punti_team"] += 2
                elif utente["sprint"] == 9:
                    utente["punti"] += 1
                    utente["punti_team"] += 1
                if utente["sprint-fl"]:
                    utente["punti"] += 2
            else:
                caduti_sprint.append(utente["nome"])
            # Feature
            if not utente["feature-dnf"]:
                if utente["feature"] == 1:
                    utente["punti"] += 25
                    utente["punti_team"] += 25
                elif utente["feature"] == 2:
                    utente["punti"] += 20
                    utente["punti_team"] += 20
                elif utente["feature"] == 3:
                    utente["punti"] += 16
                    utente["punti_team"] += 16
                elif utente["feature"] == 4:
                    utente["punti"] += 13
                    utente["punti_team"] += 13
                elif utente["feature"] == 5:
                    utente["punti"] += 11
                    utente["punti_team"] += 11
                elif utente["feature"] == 6:
                    utente["punti"] += 10
                    utente["punti_team"] += 10
                elif utente["feature"] == 7:
                    utente["punti"] += 9
                    utente["punti_team"] += 9
                elif utente["feature"] == 8:
                    utente["punti"] += 8
                    utente["punti_team"] += 8
                elif utente["feature"] == 9:
                    utente["punti"] += 7
                    utente["punti_team"] += 7
                elif utente["feature"] == 10:
                    utente["punti"] += 6
                    utente["punti_team"] += 6
                elif utente["feature"] == 11:
                    utente["punti"] += 5
                    utente["punti_team"] += 5
                elif utente["feature"] == 12:
                    utente["punti"] += 4
                    utente["punti_team"] += 4
                elif utente["feature"] == 13:
                    utente["punti"] += 3
                    utente["punti_team"] += 3
                elif utente["feature"] == 14:
                    utente["punti"] += 2
                    utente["punti_team"] += 2
                elif utente["feature"] == 15:
                    utente["punti"] += 1
                    utente["punti_team"] += 1
                if utente["feature-fl"]:
                    utente["punti"] += 2
            else:
                caduti_feature.append(utente["nome"])
            if utente["qualifica"] in [1,2,3]:
                match utente["qualifica"]:
                    case 1: utente["punti"] += 5
                    case 2: utente["punti"] += 3
                    case 3: utente["punti"] += 1
        # MotoE
        if se_motoe:
            for utente in tutti["motoe"]: 
                # Gara 1
                if not utente["gara1-dnf"]:
                    if utente["gara1"] == 1:
                        utente["punti"] += 25
                        utente["punti_team"] += 25
                    elif utente["gara1"] == 2:
                        utente["punti"] += 20
                        utente["punti_team"] += 20
                    elif utente["gara1"] == 3:
                        utente["punti"] += 16
                        utente["punti_team"] += 16
                    elif utente["gara1"] == 4:
                        utente["punti"] += 13
                        utente["punti_team"] += 13
                    elif utente["gara1"] == 5:
                        utente["punti"] += 11
                        utente["punti_team"] += 11
                    elif utente["gara1"] == 6:
                        utente["punti"] += 10
                        utente["punti_team"] += 10
                    elif utente["gara1"] == 7:
                        utente["punti"] += 9
                        utente["punti_team"] += 9
                    elif utente["gara1"] == 8:
                        utente["punti"] += 8
                        utente["punti_team"] += 8
                    elif utente["gara1"] == 9:
                        utente["punti"] += 7
                        utente["punti_team"] += 7
                    elif utente["gara1"] == 10:
                        utente["punti"] += 6
                        utente["punti_team"] += 6
                    elif utente["gara1"] == 11:
                        utente["punti"] += 5
                        utente["punti_team"] += 5
                    elif utente["gara1"] == 12:
                        utente["punti"] += 4
                        utente["punti_team"] += 4
                    elif utente["gara1"] == 13:
                        utente["punti"] += 3
                        utente["punti_team"] += 3
                    elif utente["gara1"] == 14:
                        utente["punti"] += 2
                        utente["punti_team"] += 2
                    elif utente["gara1"] == 15:
                        utente["punti"] += 1
                        utente["punti_team"] += 1
                    if utente["gara1-fl"]:
                        utente["punti"] += 2
                # Gara 2
                if not utente["gara2-dnf"]:
                    if utente["gara2"] == 1:
                        utente["punti"] += 25
                        utente["punti_team"] += 25
                    elif utente["gara2"] == 2:
                        utente["punti"] += 20
                        utente["punti_team"] += 20
                    elif utente["gara2"] == 3:
                        utente["punti"] += 16
                        utente["punti_team"] += 16
                    elif utente["gara2"] == 4:
                        utente["punti"] += 13
                        utente["punti_team"] += 13
                    elif utente["gara2"] == 5:
                        utente["punti"] += 11
                        utente["punti_team"] += 11
                    elif utente["gara2"] == 6:
                        utente["punti"] += 10
                        utente["punti_team"] += 10
                    elif utente["gara2"] == 7:
                        utente["punti"] += 9
                        utente["punti_team"] += 9
                    elif utente["gara2"] == 8:
                        utente["punti"] += 8
                        utente["punti_team"] += 8
                    elif utente["gara2"] == 9:
                        utente["punti"] += 7
                        utente["punti_team"] += 7
                    elif utente["gara2"] == 10:
                        utente["punti"] += 6
                        utente["punti_team"] += 6
                    elif utente["gara2"] == 11:
                        utente["punti"] += 5
                        utente["punti_team"] += 5
                    elif utente["gara2"] == 12:
                        utente["punti"] += 4
                        utente["punti_team"] += 4
                    elif utente["gara2"] == 13:
                        utente["punti"] += 3
                        utente["punti_team"] += 3
                    elif utente["gara2"] == 14:
                        utente["punti"] += 2
                        utente["punti_team"] += 2
                    elif utente["gara2"] == 15:
                        utente["punti"] += 1
                        utente["punti_team"] += 1
                    if utente["gara2-fl"]:
                        utente["punti"] += 2
                if utente["qualifica"] in [1,2,3]:
                    match utente["qualifica"]:
                        case 1: utente["punti"] += 5
                        case 2: utente["punti"] += 3
                        case 3: utente["punti"] += 1
        # SBK
        if se_sbk:
            for utente in tutti["sbk"]: 
                # Gara 1
                if not utente["gara1-dnf"]:
                    if utente["gara1"] == 1:
                        utente["punti"] += 25
                        utente["punti_team"] += 25
                    elif utente["gara1"] == 2:
                        utente["punti"] += 20
                        utente["punti_team"] += 20
                    elif utente["gara1"] == 3:
                        utente["punti"] += 16
                        utente["punti_team"] += 16
                    elif utente["gara1"] == 4:
                        utente["punti"] += 13
                        utente["punti_team"] += 13
                    elif utente["gara1"] == 5:
                        utente["punti"] += 11
                        utente["punti_team"] += 11
                    elif utente["gara1"] == 6:
                        utente["punti"] += 10
                        utente["punti_team"] += 10
                    elif utente["gara1"] == 7:
                        utente["punti"] += 9
                        utente["punti_team"] += 9
                    elif utente["gara1"] == 8:
                        utente["punti"] += 8
                        utente["punti_team"] += 8
                    elif utente["gara1"] == 9:
                        utente["punti"] += 7
                        utente["punti_team"] += 7
                    elif utente["gara1"] == 10:
                        utente["punti"] += 6
                        utente["punti_team"] += 6
                    elif utente["gara1"] == 11:
                        utente["punti"] += 5
                        utente["punti_team"] += 5
                    elif utente["gara1"] == 12:
                        utente["punti"] += 4
                        utente["punti_team"] += 4
                    elif utente["gara1"] == 13:
                        utente["punti"] += 3
                        utente["punti_team"] += 3
                    elif utente["gara1"] == 14:
                        utente["punti"] += 2
                        utente["punti_team"] += 2
                    elif utente["gara1"] == 15:
                        utente["punti"] += 1
                        utente["punti_team"] += 1
                    if utente["gara1-fl"]:
                        utente["punti"] += 2
                # Gara 2
                if not utente["gara2-dnf"]:
                    if utente["gara2"] == 1:
                        utente["punti"] += 25
                        utente["punti_team"] += 25
                    elif utente["gara2"] == 2:
                        utente["punti"] += 20
                        utente["punti_team"] += 20
                    elif utente["gara2"] == 3:
                        utente["punti"] += 16
                        utente["punti_team"] += 16
                    elif utente["gara2"] == 4:
                        utente["punti"] += 13
                        utente["punti_team"] += 13
                    elif utente["gara2"] == 5:
                        utente["punti"] += 11
                        utente["punti_team"] += 11
                    elif utente["gara2"] == 6:
                        utente["punti"] += 10
                        utente["punti_team"] += 10
                    elif utente["gara2"] == 7:
                        utente["punti"] += 9
                        utente["punti_team"] += 9
                    elif utente["gara2"] == 8:
                        utente["punti"] += 8
                        utente["punti_team"] += 8
                    elif utente["gara2"] == 9:
                        utente["punti"] += 7
                        utente["punti_team"] += 7
                    elif utente["gara2"] == 10:
                        utente["punti"] += 6
                        utente["punti_team"] += 6
                    elif utente["gara2"] == 11:
                        utente["punti"] += 5
                        utente["punti_team"] += 5
                    elif utente["gara2"] == 12:
                        utente["punti"] += 4
                        utente["punti_team"] += 4
                    elif utente["gara2"] == 13:
                        utente["punti"] += 3
                        utente["punti_team"] += 3
                    elif utente["gara2"] == 14:
                        utente["punti"] += 2
                        utente["punti_team"] += 2
                    elif utente["gara2"] == 15:
                        utente["punti"] += 1
                        utente["punti_team"] += 1
                    if utente["gara2-fl"]:
                        utente["punti"] += 2
                # Super Pole
                if not utente["super-dnf"]:
                    if utente["super"] == 1:
                        utente["punti"] += 12
                        utente["punti_team"] += 12
                    elif utente["super"] == 2:
                        utente["punti"] += 9
                        utente["punti_team"] += 9
                    elif utente["super"] == 3:
                        utente["punti"] += 7
                        utente["punti_team"] += 7
                    elif utente["super"] == 4:
                        utente["punti"] += 6
                        utente["punti_team"] += 6
                    elif utente["super"] == 5:
                        utente["punti"] += 5
                        utente["punti_team"] += 5
                    elif utente["super"] == 6:
                        utente["punti"] += 4
                        utente["punti_team"] += 4
                    elif utente["super"] == 7:
                        utente["punti"] += 3
                        utente["punti_team"] += 3
                    elif utente["super"] == 8:
                        utente["punti"] += 2
                        utente["punti_team"] += 2
                    elif utente["super"] == 9:
                        utente["punti"] += 1
                        utente["punti_team"] += 1
                if utente["qualifica"] in [1,2,3]:
                    match utente["qualifica"]:
                        case 1: utente["punti"] += 5
                        case 2: utente["punti"] += 3
                        case 3: utente["punti"] += 1
        
        # I punteggi di ogni pilota (escluso modif. capitano) dovrebbe essere calcolato
        # Cerca capitani
        capitani = []
        for formazione in Moto_formazione.objects.filter(giornata=id):
            if formazione.capitano:
                capitani.append([formazione.capitano.nome, formazione.capitano.categoria])
        # Controlla bonus/malus per i capitani
        for capitano in capitani:
            for utente in tutti[capitano[1].lower()]:
                if utente["nome"] == capitano[0]:
                    # Distinguere se capitano nelle categorie principali
                    if utente["categoria"] in ["Moto3", "Moto2", "MotoGP"]:
                        # Considera solo la Feature
                        if not utente["feature-dnf"]:
                            # Se non cade e tra il primo e quinto, +10p
                            if 1 <= utente["feature"] <= 5:
                                utente["punti"] += 10
                            # Se non cade ma tra undicesimo e quindicesimo, -5p
                            elif 11 <= utente["feature"] <= 15:
                                utente["punti"] -= 5
                            # Se non cade ma dopo 15°, -10p
                            elif utente["feature"] > 15 or utente["feature"] == 0:
                                utente["punti"] -= 10
                        # Se cade, -10p
                        else:
                            utente["punti"] -= 10
                    # Oppure se capitano è in MotoE o SBK
                    elif utente["categoria"] in ["MotoE", "SBK"]:
                        # Considera solo la Gara 1
                        if not utente["gara1-dnf"]:
                            # Se non cade e tra il primo e quinto, +10p
                            if 1 <= utente["gara1"] <= 5:
                                utente["punti"] += 10
                            # Se non cade ma tra undicesimo e quindicesimo, -5p
                            elif 11 <= utente["gara1"] <= 15:
                                utente["punti"] -= 5
                            # Se non cade ma dopo 15°, -10p
                            elif utente["gara1"] > 15 or utente["gara1"] == 0:
                                utente["punti"] -= 10
                        # Se cade, -10p
                        else:
                            utente["punti"] -= 10
        
        # Assegna punteggi a Moto_piloti nella gara corrispondente
        for categoria in tutti.items():
            for utente in categoria[1]:
                pilota = Moto_piloti.objects.get(nome=utente["nome"])
                match int(id):
                    case 1: pilota.gara01 = utente["punti"]
                    case 2: pilota.gara02 = utente["punti"]
                    case 3: pilota.gara03 = utente["punti"]
                    case 4: pilota.gara04 = utente["punti"]
                    case 5: pilota.gara05 = utente["punti"]
                    case 6: pilota.gara06 = utente["punti"]
                    case 7: pilota.gara07 = utente["punti"]
                    case 8: pilota.gara08 = utente["punti"]
                    case 9: pilota.gara09 = utente["punti"]
                    case 10: pilota.gara10 = utente["punti"]
                    case 11: pilota.gara11 = utente["punti"]
                    case 12: pilota.gara12 = utente["punti"]
                    case 13: pilota.gara13 = utente["punti"]
                    case 14: pilota.gara14 = utente["punti"]
                    case 15: pilota.gara15 = utente["punti"]
                    case 16: pilota.gara16 = utente["punti"]
                    case 17: pilota.gara17 = utente["punti"]
                    case 18: pilota.gara18 = utente["punti"]
                    case 19: pilota.gara19 = utente["punti"]
                    case 20: pilota.gara20 = utente["punti"]
                    case 21: pilota.gara21 = utente["punti"]
                    case 22: pilota.gara22 = utente["punti"]
                    case 23: pilota.gara23 = utente["punti"]
                pilota.totale += utente["punti"]
                pilota.save()
        
        # Assegna i punteggi ai team e tm
        # Ai team basta sommare i due utente["punti_team"] dei due piloti
        global team_moto
        # Per ogni team in tutte le categorie
        for team in team_moto:
            team_punti = 0
            team_piloti = team["piloti"].split("/") # Ritorna ["Fernandez A.", "Gardner"]
            # Cerca Fernandez A. poi Gardner
            for pilota in team_piloti:
                # Per ogni salvataggio nella categoria giusta
                for utenza in tutti[team["cat"]]:
                    # Se il nome è Fernandez A., assegna i punti_team al team
                    if utenza["nome"] == pilota:
                        team_punti += utenza["punti_team"]
            # Assegna i punti nel database
            team_nome = Moto_team.objects.get(nome=team["nome"])
            match int(id):
                case 1: team_nome.gara01 = team_punti
                case 2: team_nome.gara02 = team_punti
                case 3: team_nome.gara03 = team_punti
                case 4: team_nome.gara04 = team_punti
                case 5: team_nome.gara05 = team_punti
                case 6: team_nome.gara06 = team_punti
                case 7: team_nome.gara07 = team_punti
                case 8: team_nome.gara08 = team_punti
                case 9: team_nome.gara09 = team_punti
                case 10: team_nome.gara10 = team_punti
                case 11: team_nome.gara11 = team_punti
                case 12: team_nome.gara12 = team_punti
                case 13: team_nome.gara13 = team_punti
                case 14: team_nome.gara14 = team_punti
                case 15: team_nome.gara15 = team_punti
                case 16: team_nome.gara16 = team_punti
                case 17: team_nome.gara17 = team_punti
                case 18: team_nome.gara18 = team_punti
                case 19: team_nome.gara19 = team_punti
                case 20: team_nome.gara20 = team_punti
                case 21: team_nome.gara21 = team_punti
                case 22: team_nome.gara22 = team_punti
                case 23: team_nome.gara23 = team_punti
            team_nome.totale += team_punti
            team_nome.save()

        # Ai tm bisogna controllare che nessuno dei sia caduto nella STESSA gara
        # Sprint e Feature sono considerate gare differenti!
        global tm_moto
        for team_manager in tm_moto:
            segna_sprint = 0
            segna_feature = 0
            posizione_sprint = []
            posizione_feature = []
            tm_punti = 0
            tm_piloti = team_manager["piloti"].split("/")
            # Cerca i piloti trovati in motogp
            for pilota in tm_piloti:
                for utenza in tutti["motogp"]:
                    if utenza["nome"] == pilota:
                        # Assicurarsi che non sia DNF
                        # Sprint e Feature sono gare distinte
                        if pilota not in caduti_sprint:
                            segna_sprint += 1
                            posizione_sprint.append(utenza["sprint"])
                        if pilota not in caduti_feature:
                            segna_feature += 1
                            posizione_feature.append(utenza["feature"])
            # Se entrambi i piloti non sono DNF, assegna i punti
            if segna_sprint == 2:
                for posizione in posizione_sprint:
                    match posizione:
                        case 1: tm_punti += 12
                        case 2: tm_punti += 9
                        case 3: tm_punti += 7
                        case 4: tm_punti += 6
                        case 5: tm_punti += 5
                        case 6: tm_punti += 4
                        case 7: tm_punti += 3
                        case 8: tm_punti += 2
                        case 9: tm_punti += 1
            if segna_feature == 2:
                for posizione in posizione_feature:
                    match posizione:
                        case 1: tm_punti += 25
                        case 2: tm_punti += 20
                        case 3: tm_punti += 16
                        case 4: tm_punti += 13
                        case 5: tm_punti += 11
                        case 6: tm_punti += 10
                        case 7: tm_punti += 9
                        case 8: tm_punti += 8
                        case 9: tm_punti += 7
                        case 10: tm_punti += 6
                        case 11: tm_punti += 5
                        case 12: tm_punti += 4
                        case 13: tm_punti += 3
                        case 14: tm_punti += 2
                        case 15: tm_punti += 1
            tm_nome = Moto_teammanager.objects.get(nome=team_manager["nome"])
            match int(id):
                case 1: tm_nome.gara01 = tm_punti
                case 2: tm_nome.gara02 = tm_punti
                case 3: tm_nome.gara03 = tm_punti
                case 4: tm_nome.gara04 = tm_punti
                case 5: tm_nome.gara05 = tm_punti
                case 6: tm_nome.gara06 = tm_punti
                case 7: tm_nome.gara07 = tm_punti
                case 8: tm_nome.gara08 = tm_punti
                case 9: tm_nome.gara09 = tm_punti
                case 10: tm_nome.gara10 = tm_punti
                case 11: tm_nome.gara11 = tm_punti
                case 12: tm_nome.gara12 = tm_punti
                case 13: tm_nome.gara13 = tm_punti
                case 14: tm_nome.gara14 = tm_punti
                case 15: tm_nome.gara15 = tm_punti
                case 16: tm_nome.gara16 = tm_punti
                case 17: tm_nome.gara17 = tm_punti
                case 18: tm_nome.gara18 = tm_punti
                case 19: tm_nome.gara19 = tm_punti
                case 20: tm_nome.gara20 = tm_punti
                case 21: tm_nome.gara21 = tm_punti
                case 22: tm_nome.gara22 = tm_punti
                case 23: tm_nome.gara23 = tm_punti
            tm_nome.totale += tm_punti
            tm_nome.save()

        # Calcola il punteggio di ogni formazione
        for formazione in formazioni:
            totale = 0
            # Piloti
            try:
                for pilota in formazione.piloti.all():
                    match int(id):
                        case 1: totale += Moto_piloti.objects.get(nome=pilota.nome).gara01
                        case 2: totale += Moto_piloti.objects.get(nome=pilota.nome).gara02
                        case 3: totale += Moto_piloti.objects.get(nome=pilota.nome).gara03
                        case 4: totale += Moto_piloti.objects.get(nome=pilota.nome).gara04
                        case 5: totale += Moto_piloti.objects.get(nome=pilota.nome).gara05
                        case 6: totale += Moto_piloti.objects.get(nome=pilota.nome).gara06
                        case 7: totale += Moto_piloti.objects.get(nome=pilota.nome).gara07
                        case 8: totale += Moto_piloti.objects.get(nome=pilota.nome).gara08
                        case 9: totale += Moto_piloti.objects.get(nome=pilota.nome).gara09
                        case 10: totale += Moto_piloti.objects.get(nome=pilota.nome).gara10
                        case 11: totale += Moto_piloti.objects.get(nome=pilota.nome).gara11
                        case 12: totale += Moto_piloti.objects.get(nome=pilota.nome).gara12
                        case 13: totale += Moto_piloti.objects.get(nome=pilota.nome).gara13
                        case 14: totale += Moto_piloti.objects.get(nome=pilota.nome).gara14
                        case 15: totale += Moto_piloti.objects.get(nome=pilota.nome).gara15
                        case 16: totale += Moto_piloti.objects.get(nome=pilota.nome).gara16
                        case 17: totale += Moto_piloti.objects.get(nome=pilota.nome).gara17
                        case 18: totale += Moto_piloti.objects.get(nome=pilota.nome).gara18
                        case 19: totale += Moto_piloti.objects.get(nome=pilota.nome).gara19
                        case 20: totale += Moto_piloti.objects.get(nome=pilota.nome).gara20
                        case 21: totale += Moto_piloti.objects.get(nome=pilota.nome).gara21
                        case 22: totale += Moto_piloti.objects.get(nome=pilota.nome).gara22
                        case 23: totale += Moto_piloti.objects.get(nome=pilota.nome).gara23
            except:
                pass 
            # Teams               
            try:
                for team in formazione.team.all():
                    match int(id):
                        case 1: totale += Moto_team.objects.get(nome=team.nome).gara01
                        case 2: totale += Moto_team.objects.get(nome=team.nome).gara02
                        case 3: totale += Moto_team.objects.get(nome=team.nome).gara03
                        case 4: totale += Moto_team.objects.get(nome=team.nome).gara04
                        case 5: totale += Moto_team.objects.get(nome=team.nome).gara05
                        case 6: totale += Moto_team.objects.get(nome=team.nome).gara06
                        case 7: totale += Moto_team.objects.get(nome=team.nome).gara07
                        case 8: totale += Moto_team.objects.get(nome=team.nome).gara08
                        case 9: totale += Moto_team.objects.get(nome=team.nome).gara09
                        case 10: totale += Moto_team.objects.get(nome=team.nome).gara10
                        case 11: totale += Moto_team.objects.get(nome=team.nome).gara11
                        case 12: totale += Moto_team.objects.get(nome=team.nome).gara12
                        case 13: totale += Moto_team.objects.get(nome=team.nome).gara13
                        case 14: totale += Moto_team.objects.get(nome=team.nome).gara14
                        case 15: totale += Moto_team.objects.get(nome=team.nome).gara15
                        case 16: totale += Moto_team.objects.get(nome=team.nome).gara16
                        case 17: totale += Moto_team.objects.get(nome=team.nome).gara17
                        case 18: totale += Moto_team.objects.get(nome=team.nome).gara18
                        case 19: totale += Moto_team.objects.get(nome=team.nome).gara19
                        case 20: totale += Moto_team.objects.get(nome=team.nome).gara20
                        case 21: totale += Moto_team.objects.get(nome=team.nome).gara21
                        case 22: totale += Moto_team.objects.get(nome=team.nome).gara22
                        case 23: totale += Moto_team.objects.get(nome=team.nome).gara23
            except:
                pass
            # Team Manager
            try:
                tm = formazione.teammanager
                match int(id):
                    case 1: totale += Moto_teammanager.objects.get(nome=tm.nome).gara01
                    case 2: totale += Moto_teammanager.objects.get(nome=tm.nome).gara02
                    case 3: totale += Moto_teammanager.objects.get(nome=tm.nome).gara03
                    case 4: totale += Moto_teammanager.objects.get(nome=tm.nome).gara04
                    case 5: totale += Moto_teammanager.objects.get(nome=tm.nome).gara05
                    case 6: totale += Moto_teammanager.objects.get(nome=tm.nome).gara06
                    case 7: totale += Moto_teammanager.objects.get(nome=tm.nome).gara07
                    case 8: totale += Moto_teammanager.objects.get(nome=tm.nome).gara08
                    case 9: totale += Moto_teammanager.objects.get(nome=tm.nome).gara09
                    case 10: totale += Moto_teammanager.objects.get(nome=tm.nome).gara10
                    case 11: totale += Moto_teammanager.objects.get(nome=tm.nome).gara11
                    case 12: totale += Moto_teammanager.objects.get(nome=tm.nome).gara12
                    case 13: totale += Moto_teammanager.objects.get(nome=tm.nome).gara13
                    case 14: totale += Moto_teammanager.objects.get(nome=tm.nome).gara14
                    case 15: totale += Moto_teammanager.objects.get(nome=tm.nome).gara15
                    case 16: totale += Moto_teammanager.objects.get(nome=tm.nome).gara16
                    case 17: totale += Moto_teammanager.objects.get(nome=tm.nome).gara17
                    case 18: totale += Moto_teammanager.objects.get(nome=tm.nome).gara18
                    case 19: totale += Moto_teammanager.objects.get(nome=tm.nome).gara19
                    case 20: totale += Moto_teammanager.objects.get(nome=tm.nome).gara20
                    case 21: totale += Moto_teammanager.objects.get(nome=tm.nome).gara21
                    case 22: totale += Moto_teammanager.objects.get(nome=tm.nome).gara22
                    case 23: totale += Moto_teammanager.objects.get(nome=tm.nome).gara23
            except:
                pass
            # Con i try dovrei aver escluso chi non ha schierato la formazione
            formazione.p_totali = totale
            formazione.save()

        # Controlla chi hai contro e vedi chi ha vinto
        global sfide_moto
        sfide_giornata = sfide_moto[1]["sfida"]
        sfide_giornata = sfide_giornata.split("/")
        scontri = []
        for i in sfide_giornata:
            scontri.append(i.split("+"))
        for scontro in scontri:
            form_user1 = Moto_formazione.objects.get(giornata=id, username=scontro[0])
            form_user2 = Moto_formazione.objects.get(giornata=id, username=scontro[1])
            punti_user1 = Moto_punti.objects.get(username=scontro[0])
            punti_user2 = Moto_punti.objects.get(username=scontro[1])
            # Se user1 vince
            if form_user1.p_totali > form_user2.p_totali:
                # Indica nella formazione chi ha vinto
                form_user1.risultato = 1
                form_user2.risultato = 0
                # Aggiungi punti scontri a chi ha vinto
                punti_user1.p_scontri += 3
                # Aggiungi punti generali 
                punti_user1.p_generali += form_user1.p_totali
                punti_user2.p_generali += form_user2.p_totali
                # Aggiorna la differenza punti
                differenza = form_user1.p_totali - form_user2.p_totali
                punti_user1.differenza += differenza
                punti_user2.differenza -= differenza
            # Se user2 vince
            elif form_user1.p_totali < form_user2.p_totali:
                # Indica nella formazione chi ha vinto
                form_user1.risultato = 0
                form_user2.risultato = 1
                # Aggiungi punti scontri a chi ha vinto
                punti_user2.p_scontri += 3
                # Aggiungi punti generali 
                punti_user1.p_generali += form_user1.p_totali
                punti_user2.p_generali += form_user2.p_totali
                # Aggiorna la differenza punti
                differenza = form_user2.p_totali - form_user1.p_totali
                punti_user1.differenza -= differenza
                punti_user2.differenza += differenza
            # Se pareggio
            else:
                # Indica nella formazione il pareggio ._.
                form_user1.risultato = 2
                form_user2.risultato = 2
                # Aggiungi punti scontri ad entrambi
                punti_user1.p_scontri += 1
                punti_user2.p_scontri += 1
                # Aggiungi punti generali 
                punti_user1.p_generali += form_user1.p_totali
                punti_user2.p_generali += form_user2.p_totali
                # Nessun cambio alla differenza punti
            form_user1.save()
            form_user2.save()
            punti_user1.save()
            punti_user2.save()
        # Una volta inseriti TUTTI i valori nel database, considera la giornata calcolata
        questa_giornata = Moto_giornata.objects.get(id=id)
        questa_giornata.calcolata = 1
        questa_giornata.save()
        # Reindirizza alla home
        return HttpResponseRedirect(reverse("fantamoto"))

    # Se si sta facendo una richiesta GET, mostra pagina
    # Se la data della gara è nel futuro, mostra errore
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
        motoe = Moto_giornata.objects.get(id=id).motoe
        sbk = Moto_giornata.objects.get(id=id).sbk
        piloti3 = Moto_piloti.objects.filter(categoria="Moto3").order_by("nome")
        piloti2 = Moto_piloti.objects.filter(categoria="Moto2").order_by("nome")
        pilotigp = Moto_piloti.objects.filter(categoria="MotoGP").order_by("nome")
        pilotie = Moto_piloti.objects.filter(categoria="MotoE").order_by("nome")
        pilotisbk = Moto_piloti.objects.filter(categoria="SBK").order_by("nome")
    else:
        return render(request, "errore.html", {
            "message": f"LA GARA SELEZIONATA ({posto}) È GIÀ STATA CALCOLATA!",
            "cat": "moto"
        })
    return render(request, "fantamoto/calcolo_gara.html", {
        "id": id,
        "posto": posto,
        "motoe": motoe,
        "sbk": sbk,
        "piloti3": piloti3,
        "piloti2": piloti2,
        "pilotigp": pilotigp,
        "pilotie": pilotie,
        "pilotisbk": pilotisbk,
        "cat": "moto"
    })



################################### FORMULA #######################################
sfide_formula = [
    {"id":1, "sfida":"Albwin27+Vettel05/Zanno+Cortez Black Team/Paul Bird Motorsport+Cicciobirro01/Tazza+Dragon trainer"},
    {"id":2, "sfida":"Zanno+Albwin27/Vettel05+Paul Bird Motorsport/Cortez Black Team+Tazza/Cicciobirro01+Dragon trainer"},
    {"id":3, "sfida":"Albwin27+Tazza/Dragon trainer+Paul Bird Motorsport/Cicciobirro01+Zanno/Cortez Black Team+Vettel05"},
    {"id":4, "sfida":"Cicciobirro01+Albwin27/Dragon trainer+Cortez Black Team/Tazza+Vettel05/Paul Bird Motorsport+Zanno"},
    {"id":5, "sfida":"Albwin27+Dragon trainer/Tazza+Cicciobirro01/Cortez Black Team+Paul Bird Motorsport/Vettel05+Zanno"},
    {"id":6, "sfida":"Cortez Black Team+Albwin27/Vettel05+Cicciobirro01/Dragon trainer+Zanno/Paul Bird Motorsport+Tazza"},
    {"id":7, "sfida":"Albwin27+Paul Bird Motorsport/Zanno+Tazza/Dragon trainer+Vettel05/Cicciobirro01+Cortez Black Team"},
    {"id":8, "sfida":"Albwin27+Vettel05/Zanno+Cortez Black Team/Paul Bird Motorsport+Cicciobirro01/Tazza+Dragon trainer"},
    {"id":9, "sfida":"Zanno+Albwin27/Vettel05+Paul Bird Motorsport/Cortez Black Team+Tazza/Cicciobirro01+Dragon trainer"},
    {"id":10, "sfida":"Albwin27+Tazza/Dragon trainer+Paul Bird Motorsport/Cicciobirro01+Zanno/Cortez Black Team+Vettel05"},
    {"id":11, "sfida":"Cicciobirro01+Albwin27/Dragon trainer+Cortez Black Team/Tazza+Vettel05/Paul Bird Motorsport+Zanno"},
    {"id":12, "sfida":"Albwin27+Dragon trainer/Tazza+Cicciobirro01/Cortez Black Team+Paul Bird Motorsport/Vettel05+Zanno"},
    {"id":13, "sfida":"Cortez Black Team+Albwin27/Vettel05+Cicciobirro01/Dragon trainer+Zanno/Paul Bird Motorsport+Tazza"},
    {"id":14, "sfida":"Albwin27+Paul Bird Motorsport/Zanno+Tazza/Dragon trainer+Vettel05/Cicciobirro01+Cortez Black Team"},
    {"id":15, "sfida":"Albwin27+Vettel05/Zanno+Cortez Black Team/Paul Bird Motorsport+Cicciobirro01/Tazza+Dragon trainer"},
    {"id":16, "sfida":"Zanno+Albwin27/Vettel05+Paul Bird Motorsport/Cortez Black Team+Tazza/Cicciobirro01+Dragon trainer"},
    {"id":17, "sfida":"Albwin27+Tazza/Dragon trainer+Paul Bird Motorsport/Cicciobirro01+Zanno/Cortez Black Team+Vettel05"},
    {"id":18, "sfida":"Cicciobirro01+Albwin27/Dragon trainer+Cortez Black Team/Tazza+Vettel05/Paul Bird Motorsport+Zanno"},
    {"id":19, "sfida":"Albwin27+Dragon trainer/Tazza+Cicciobirro01/Cortez Black Team+Paul Bird Motorsport/Vettel05+Zanno"},
    {"id":20, "sfida":"Cortez Black Team+Albwin27/Vettel05+Cicciobirro01/Dragon trainer+Zanno/Paul Bird Motorsport+Tazza"},
    {"id":21, "sfida":"Albwin27+Paul Bird Motorsport/Zanno+Tazza/Dragon trainer+Vettel05/Cicciobirro01+Cortez Black Team"},
    {"id":22, "sfida":"Albwin27+Vettel05/Zanno+Cortez Black Team/Paul Bird Motorsport+Cicciobirro01/Tazza+Dragon trainer"},
    {"id":23, "sfida":"Zanno+Albwin27/Vettel05+Paul Bird Motorsport/Cortez Black Team+Tazza/Cicciobirro01+Dragon trainer"},
]

team_formula = [
    {"nome": "Red Bull", "piloti": "Verstappen/Perez", "cat": "f1"},
    {"nome": "Ferrari", "piloti": "Leclerc C./Sainz", "cat": "f1"},
    {"nome": "Mercedes", "piloti": "Russell/Hamilton", "cat": "f1"},
    {"nome": "Alpine", "piloti": "Ocon/Gasly", "cat": "f1"},
    {"nome": "McLaren", "piloti": "Piastri/Norris", "cat": "f1"},
    {"nome": "Alfa Romeo", "piloti": "Bottas/Zhou", "cat": "f1"},
    {"nome": "Aston Martin", "piloti": "Alonso/Stroll", "cat": "f1"},
    {"nome": "Haas", "piloti": "Magnussen/Hulkenberg", "cat": "f1"},
    {"nome": "Alpha Tauri", "piloti": "Tsunoda/De Vries", "cat": "f1"},
    {"nome": "Williams", "piloti": "Sargeant/Albon", "cat": "f1"},
    {"nome": "MP Motorsport", "piloti": "Hauger/Daruvala", "cat": "f2"},
    {"nome": "Rodin Carlin", "piloti": "Maloney/Fittipaldi", "cat": "f2"},
    {"nome": "ART", "piloti": "Pourchaire/Martins", "cat": "f2"},
    {"nome": "Prema Racing", "piloti": "Vesti/Bearman", "cat": "f2"},
    {"nome": "HiTech", "piloti": "Crawford/Hadjar", "cat": "f2"},
    {"nome": "DAMS", "piloti": "Iwasa/Leclerc A.", "cat": "f2"},
    {"nome": "Virtuosi Racing", "piloti": "Doohan/Cordeel", "cat": "f2"},
    {"nome": "PHM Racing", "piloti": "Nissany/Benavides", "cat": "f2"},
    {"nome": "Trident", "piloti": "Stanek/Novalak", "cat": "f2"},
    {"nome": "Van Amersfoort Racing", "piloti": "Verschoor/Correa", "cat": "f2"},
    {"nome": "Campos Racing", "piloti": "Maini/Boschung", "cat": "f2"},
]

tm_formula = [
    {"nome": "Horner (Red Bull)", "piloti": "Verstappen/Perez"},
    {"nome": "Vasseur (Ferrari)", "piloti": "Leclerc C./Sainz"},
    {"nome": "Wolff (Mercedes)", "piloti": "Russell/Hamilton"},
    {"nome": "Szafnauer (Alpine)", "piloti": "Ocon/Gasly"},
    {"nome": "Stella (McLaren)", "piloti": "Piastri/Norris"},
    {"nome": "Alunni Bravi (Alfa Romeo)", "piloti": "Bottas/Zhou"},
    {"nome": "Krack (Aston Martin)", "piloti": "Alonso/Stroll"},
    {"nome": "Steiner (Haas)", "piloti": "Magnussen/Hulkenberg"},
    {"nome": "Tost (Alpha Tauri)", "piloti": "Tsunoda/De Vries"},
    {"nome": "Vowles (Williams)", "piloti": "Sargeant/Albon"},
]

@login_required
def formula_home(request):
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
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
        previousgara = Formula_formazione.objects.get(giornata=ultimagara.id, username=request.user.username)
    # Ritorna posizioni in classifica
    s_ranking = Formula_punti.objects.order_by("-p_scontri", "-differenza")
    p_ranking = Formula_punti.objects.order_by("-p_generali", "-differenza")
    # Cerca se hai schierato la formazione per la prossima gara
    try:
        schierata = Formula_formazione.objects.get(giornata=nextgara.id, username=request.user)
    except:
        schierata = None
    return render(request, "fantaformula/home.html", {
        "utente": request.user,
        "ultimagara": ultimagara,
        "previousgara": previousgara,
        "nextgara": nextgara,
        "s_ranking": s_ranking,
        "p_ranking": p_ranking,
        "schierata": schierata,
        "cat": "formula"
    })


@login_required
def formula_rose(request):
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
    tutti = User.objects.order_by("username")
    formula_tutti = []
    for uno in tutti:
        if uno.id != 6 and uno.id != 10:
            formula_tutti.append(uno)
    return render(request, "fantaformula/rose.html", {
        "tutti": formula_tutti,
        "cat": "formula"
    })


@login_required
def formula_rosautente(request, utente):
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
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
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
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
    global sfide_formula
    all_id = []
    all_sfide = []
    for sfida in sfide_formula:
        all_id.append(sfida["id"])
        scontri_lista = []
        scontri = sfida["sfida"].split("/")
        for scontro in scontri:
            scontro = scontro.split("+")
            scontri_lista.append(scontro)
        all_sfide.append(scontri_lista)
    tutti = User.objects.order_by("username")
    formula_tutti = []
    for uno in tutti:
        if uno.id != 6 and uno.id != 10:
            formula_tutti.append(uno)
    return render(request, "fantaformula/calendario.html", {
        "giornate": giornate,
        "ultima": ultimagara,
        "sfide": all_sfide,
        "tutti": formula_tutti,
        "cat": "formula"
    })


@login_required
def formula_scontro(request, id, scontro):
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
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
    # Ottieni formazione primo user
    # Cerca tutti i piloti, team e tm schierati
    try:
        piloti1 = formazione1.piloti.all()
        teams1 = formazione1.team.all()
        tm1 = formazione1.teammanager.nome
        # Se la formazione è già stata calcolata, carica i punti ottenuti da piloti,team, tm
        # Seleziona i punteggi da Formula_piloti e consegnali in una lista
        # Fa schifo ma non ho assolutamente idea di come farlo diversamente
        punti_piloti1 = []
        for pilota1 in piloti1:
            match int(id):
                case 1: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara01
                case 2: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara02
                case 3: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara03
                case 4: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara04
                case 5: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara05
                case 6: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara06
                case 7: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara07
                case 8: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara08
                case 9: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara09
                case 10: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara10
                case 11: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara11
                case 12: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara12
                case 13: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara13
                case 14: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara14
                case 15: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara15
                case 16: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara16
                case 17: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara17
                case 18: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara18
                case 19: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara19
                case 20: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara20
                case 21: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara21
                case 22: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara22
                case 23: punti_pilota1 = Formula_piloti.objects.get(nome=pilota1.nome).gara23
            if punti_pilota1:
                punti_piloti1.append(punti_pilota1)
        # Seleziona punti dei team
        punti_teams1 = []
        for team1 in teams1:
            match int(id):
                case 1: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara01
                case 2: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara02
                case 3: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara03
                case 4: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara04
                case 5: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara05
                case 6: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara06
                case 7: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara07
                case 8: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara08
                case 9: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara09
                case 10: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara10
                case 11: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara11
                case 12: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara12
                case 13: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara13
                case 14: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara14
                case 15: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara15
                case 16: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara16
                case 17: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara17
                case 18: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara18
                case 19: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara19
                case 20: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara20
                case 21: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara21
                case 22: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara22
                case 23: punti_team1 = Formula_team.objects.get(nome=team1.nome).gara23
            if punti_team1:
                punti_teams1.append(punti_team1)
        match int(id):
            case 1: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara01
            case 2: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara02
            case 3: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara03
            case 4: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara04
            case 5: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara05
            case 6: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara06
            case 7: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara07
            case 8: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara08
            case 9: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara09
            case 10: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara10
            case 11: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara11
            case 12: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara12
            case 13: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara13
            case 14: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara14
            case 15: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara15
            case 16: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara16
            case 17: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara17
            case 18: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara18
            case 19: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara19
            case 20: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara20
            case 21: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara21
            case 22: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara22
            case 23: punti_tm1 = Formula_teammanager.objects.get(nome=tm1).gara23
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
    ################## Ripeti tutto per il secondo utente ###################
    # Se formazione è schierata
    try:
        piloti2 = formazione2.piloti.all()
        teams2 = formazione2.team.all()
        tm2 = formazione2.teammanager.nome
        punti_piloti2 = []
        for pilota2 in piloti2:
            match int(id):
                case 1: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara01
                case 2: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara02
                case 3: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara03
                case 4: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara04
                case 5: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara05
                case 6: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara06
                case 7: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara07
                case 8: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara08
                case 9: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara09
                case 10: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara10
                case 11: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara11
                case 12: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara12
                case 13: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara13
                case 14: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara14
                case 15: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara15
                case 16: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara16
                case 17: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara17
                case 18: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara18
                case 19: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara19
                case 20: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara20
                case 21: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara21
                case 22: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara22
                case 23: punti_pilota2 = Formula_piloti.objects.get(nome=pilota2.nome).gara23
            if punti_pilota2:
                punti_piloti2.append(punti_pilota2)
        punti_teams2 = []
        for team2 in teams2:
            match int(id):
                case 1: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara01
                case 2: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara02
                case 3: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara03
                case 4: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara04
                case 5: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara05
                case 6: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara06
                case 7: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara07
                case 8: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara08
                case 9: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara09
                case 10: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara10
                case 11: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara11
                case 12: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara12
                case 13: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara13
                case 14: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara14
                case 15: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara15
                case 16: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara16
                case 17: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara17
                case 18: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara18
                case 19: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara19
                case 20: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara20
                case 21: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara21
                case 22: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara22
                case 23: punti_team2 = Formula_team.objects.get(nome=team2.nome).gara23
            if punti_team2:
                punti_teams2.append(punti_team2)
        match int(id):
            case 1: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara01
            case 2: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara02
            case 3: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara03
            case 4: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara04
            case 5: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara05
            case 6: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara06
            case 7: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara07
            case 8: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara08
            case 9: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara09
            case 10: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara10
            case 11: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara11
            case 12: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara12
            case 13: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara13
            case 14: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara14
            case 15: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara15
            case 16: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara16
            case 17: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara17
            case 18: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara18
            case 19: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara19
            case 20: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara20
            case 21: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara21
            case 22: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara22
            case 23: punti_tm2 = Formula_teammanager.objects.get(nome=tm2).gara23
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
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
    s_ranking = Formula_passato.objects.order_by("-ex_pscontri", "-ex_differenza")
    p_ranking = Formula_passato.objects.order_by("-ex_pgenerali", "-ex_differenza")
    return render(request, "fantaformula/albodoro.html", {
        "s_ranking": s_ranking,
        "p_ranking": p_ranking,
        "cat": "formula"
    })


@login_required
def formula_formazione(request):
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
    now = timezone.localtime()
    alldates = Formula_giornata.objects.values_list('data', flat=True)
    alldates = list(alldates)
    for date in alldates:
        date = timezone.localtime(date)
        if date > now:
            nextdate = date
            break
    nextgara = Formula_giornata.objects.get(data=nextdate)
    piloti = Formula_piloti.objects.filter(username=request.user.username)
    teams = Formula_team.objects.filter(username=request.user.username)
    tm = Formula_teammanager.objects.get(username=request.user.username)
    # Ottieni gli ultimi tre risultati
    # Altro obrobrio, ma occhio non vede cuore non duole
    ultime = [nextgara.id - 1, nextgara.id - 2, nextgara.id - 3]
    # Non prendere id giornate negativo o zero
    for i in range(3):
        if ultime[i] == 0 or ultime[i] < 0:
            ultime[i] = 0
    punti_piloti = []
    for pilota in piloti:
        punti_pilota = []
        for giornata in ultime:
            match giornata:
                case 1: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara01
                case 2: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara02
                case 3: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara03
                case 4: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara04
                case 5: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara05
                case 6: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara06
                case 7: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara07
                case 8: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara08
                case 9: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara09
                case 10: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara10
                case 11: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara11
                case 12: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara12
                case 13: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara13
                case 14: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara14
                case 15: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara15
                case 16: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara16
                case 17: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara17
                case 18: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara18
                case 19: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara19
                case 20: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara20
                case 21: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara21
                case 22: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara22
                case 23: punti_g = Formula_piloti.objects.get(nome=pilota.nome).gara23
                case _: punti_g = "-"
            # Aggiungi punti delle ultime tre giornate
            try:
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
            match giornata:
                case 1: punti_g = Formula_team.objects.get(nome=team.nome).gara01
                case 2: punti_g = Formula_team.objects.get(nome=team.nome).gara02
                case 3: punti_g = Formula_team.objects.get(nome=team.nome).gara03
                case 4: punti_g = Formula_team.objects.get(nome=team.nome).gara04
                case 5: punti_g = Formula_team.objects.get(nome=team.nome).gara05
                case 6: punti_g = Formula_team.objects.get(nome=team.nome).gara06
                case 7: punti_g = Formula_team.objects.get(nome=team.nome).gara07
                case 8: punti_g = Formula_team.objects.get(nome=team.nome).gara08
                case 9: punti_g = Formula_team.objects.get(nome=team.nome).gara09
                case 10: punti_g = Formula_team.objects.get(nome=team.nome).gara10
                case 11: punti_g = Formula_team.objects.get(nome=team.nome).gara11
                case 12: punti_g = Formula_team.objects.get(nome=team.nome).gara12
                case 13: punti_g = Formula_team.objects.get(nome=team.nome).gara13
                case 14: punti_g = Formula_team.objects.get(nome=team.nome).gara14
                case 15: punti_g = Formula_team.objects.get(nome=team.nome).gara15
                case 16: punti_g = Formula_team.objects.get(nome=team.nome).gara16
                case 17: punti_g = Formula_team.objects.get(nome=team.nome).gara17
                case 18: punti_g = Formula_team.objects.get(nome=team.nome).gara18
                case 19: punti_g = Formula_team.objects.get(nome=team.nome).gara19
                case 20: punti_g = Formula_team.objects.get(nome=team.nome).gara20
                case 21: punti_g = Formula_team.objects.get(nome=team.nome).gara21
                case 22: punti_g = Formula_team.objects.get(nome=team.nome).gara22
                case 23: punti_g = Formula_team.objects.get(nome=team.nome).gara23
                case _: punti_g = "-"
            # Aggiungi punti delle ultime tre giornate
            try:
                punti_team.append(punti_g)
            except:
                punti_team.append("-")
        # Aggiungi team ai teams
        punti_teams.append(punti_team)
    # Ripeti per team manager
    punti_tm = []
    for giornata in ultime:
        match giornata:
            case 1: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara01
            case 2: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara02
            case 3: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara03
            case 4: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara04
            case 5: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara05
            case 6: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara06
            case 7: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara07
            case 8: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara08
            case 9: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara09
            case 10: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara10
            case 11: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara11
            case 12: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara12
            case 13: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara13
            case 14: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara14
            case 15: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara15
            case 16: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara16
            case 17: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara17
            case 18: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara18
            case 19: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara19
            case 20: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara20
            case 21: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara21
            case 22: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara22
            case 23: punti_g = Formula_teammanager.objects.get(nome=tm.nome).gara23
            case _: punti_g = "-"
        try:
            punti_tm.append(punti_g)
        except:
            punti_tm.append("-")
    return render(request, "fantaformula/formazione.html", {
        "piloti": piloti,
        "teams": teams,
        "tm": tm,
        "nextgara": nextgara,
        "punti_piloti": punti_piloti,
        "punti_teams": punti_teams,
        "punti_tm": punti_tm,
        "cat": "formula"
    })


@login_required
def formula_schieramento(request):
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
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
        # Se non c'è la Formula2
        if nextgara.f2 == 0:
            # Controlla se 2 piloti, un team e tm
            if len(piloti) != 2:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 2 PILOTI, Formula2 ESCLUSA.",
                    "cat": "formula"
                })
            if len(teams) != 1:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM, Formula2 ESCLUSA.",
                    "cat": "formula"
                })
            if tm is None:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA IL TEAM MANAGER.",
                    "cat": "formula"
                })
            # Controlla le categorie dei piloti
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "F1" not in categorie_piloti and "F2" in categorie_piloti:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA SOLO PILOTI DI Formula1.",
                    "cat": "formula"
                })
            # Controlla le categorie dei team
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "F1" not in categorie_teams and "F2" in categorie_teams:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI Formula1.",
                    "cat": "formula"
                })
        # Stessi controlli ma con la Formula2
        elif nextgara.f2 == 1:
            if len(piloti) != 4:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 4 PILOTI, Formula2 INCLUSA.",
                    "cat": "formula"
                })
            if len(teams) != 2:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA 2 TEAM, Formula2 INCLUSA.",
                    "cat": "formula"
                })
            if tm is None:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA IL TEAM MANAGER.",
                    "cat": "formula"
                })
            for pilota in piloti:
                categorie_piloti.append(pilota.split(" - ")[1])
            if "F1" not in categorie_piloti and "F2" not in categorie_piloti:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN PILOTA DI OGNI CATEGORIA, Formula2 INCLUSA.",
                    "cat": "formula"
                })
            for team in teams:
                categorie_teams.append(team.split(" - ")[1])
            if "F1" not in categorie_teams and "F2" not in categorie_teams:
                return render(request, "errore.html", {
                    "message": "FORMAZIONE NON SCHIERATA: SELEZIONA UN TEAM DI OGNI CATEGORIA, Formula2 INCLUSA.",
                    "cat": "formula"
                })
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
        formazione_tm = Formula_teammanager.objects.get(nome=tm)
        formazione_user = request.user
        # Salva la formazione nel database
        formazione = Formula_formazione.objects.create(
            giornata = formazione_giornata,
            data = formazione_data,
            teammanager = formazione_tm,
            username = request.user.username,
            utente = formazione_user)
        formazione.piloti.set(formazione_piloti)
        formazione.team.set(formazione_teams)
        formazione.save()
        # Rispedisci alla home
        return HttpResponseRedirect(reverse("fantaformula"))


@login_required
def formula_calcoloscelta(request):
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
    autorizzati = [1, 3]
    if request.user.id not in autorizzati:
        return render(request, "errore.html", {
            "message": "Non sei autorizzato al calcolo delle giornate",
            "cat": "formula",
        })
    giornate = Formula_giornata.objects.all()
    utenti = User.objects.all()
    formula_tutti = []
    for uno in utenti:
        if uno.id != 6 and uno.id != 10:
            formula_tutti.append(uno)
    return render(request, "fantaformula/calcolo_scelta.html", {
        "giornate": giornate,
        "utenti": formula_tutti,
        "cat": "formula"
    })


@login_required
def formula_calcologara(request, id):
    # Escludi chi non partecipa
    if not request.user.fantaformula:
        return render(request, "errore.html", {
            "message": "Non partecipi al FantaFormula.",
            "cat": "formula"
        })
    # Accesso solo agli autorizzati
    autorizzati = [1, 3]
    if request.user.id not in autorizzati:
        return render(request, "errore.html", {
            "message": "Non sei autorizzato al calcolo delle giornate",
            "cat": "formula",
        })
    
    # Se si sta facendo una richiesta POST, calcola i risultati
    # Aiutatemi che questa sarà lunga 2: LA VENDETTA
    if request.method == "POST":
        # Se in qualche modo giornata già calcolata, manda errore
        if Formula_giornata.objects.get(id=id).calcolata:
            return render(request, "errore.html", {
                "message": f"HAI GIÀ CALCOLATO QUESTA GIORNATA ._.",
                "cat": "formula"
            })
        # Ottieni tutte le formazioni schierate
        utenti = [user for user in User.objects.all()]
        formula_tutti = []
        for uno in utenti:
            if uno.id != 6 and uno.id != 10:
                formula_tutti.append(uno)
        # Cambia la variabile che mi scoccia cambiare tutte le istanze di "utenti"
        utenti = formula_tutti
        formazioni = []
        for utente in utenti:
            # Ottieni formazione
            try:
                formazione = Formula_formazione.objects.get(username=utente.username, giornata=id)
            # Se non è stata schierata, creane una vuota
            except:
                print(f"manca a {utente.username}")
                formazione = Formula_formazione.objects.create(
                    giornata = id,
                    data = timezone.localtime(),
                    username = utente.username,
                    utente = utente)
                formazione.save()
            formazioni.append(formazione)
        # Prendi tutte le info ricevute da POST e dividile tra attributo e valore
        ricevuto = request.POST.items()
        se_sprint = Formula_giornata.objects.get(id=id).sprint
        se_f2 = Formula_giornata.objects.get(id=id).f2
        var_f1 = []
        if se_f2:
            var_f2 = []
        for key, value in ricevuto:
            try:
                attributi = key.split("-")
                match attributi[-2]:
                    case "1": var_f1.append([key, value])
                    case "2": var_f2.append([key, value])
                    case _: pass
            except:
                pass

        # Prima cerchiamo tutti gli errori possibili per ogni categoria
        # Formula1 Errori
        check_quali1 = []
        check_feat1 = []
        feat_fl1_count = 0
        # Check nell'eventuale sprint
        if se_sprint:
            check_spr1 = []
            spr_fl1_count = 0
            for variabile in var_f1:
                if variabile[0].startswith("spr-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                    if variabile[1] in check_spr1 and variabile[1] != "":
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In Formula1, più piloti hanno la stessa posizione nella Sprint Race.",
                            "cat": "formula"
                        })
                    else:
                        check_spr1.append(variabile[1])
                if variabile[0].startswith("spr-fl"):
                    spr_fl1_count += 1
            if spr_fl1_count != 1:
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In Formula1, ci sono nessun o più Fast Lap nella Sprint Race.",
                    "cat": "formula"                
                })
        # Check nella feature
        for variabile in var_f1:
            if variabile[0].startswith("quali-"):
                if variabile[1] in check_quali1:
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In Formula1, più piloti hanno la stessa posizione in qualifica.",
                        "cat": "formula"
                    })
                else:
                    check_quali1.append(variabile[1])
            if variabile[0].startswith("feat-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                if variabile[1] in check_feat1 and variabile[1] != "":
                    return render(request, "errore.html", {
                        "message": "GIORNATA NON CALCOLATA: In Formula1, più piloti hanno la stessa posizione nella Feature Race.",
                        "cat": "formula"
                    })
                else:
                    check_feat1.append(variabile[1])
            if variabile[0].startswith("feat-fl-"):
                feat_fl1_count += 1
        if feat_fl1_count != 1:
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In Formula1, ci sono nessun o più Fast Lap nella Feature Race.",
                "cat": "formula"
            })
        if not all(value in ["1", "2", "3"] for value in check_quali1):
            return render(request, "errore.html", {
                "message": "GIORNATA NON CALCOLATA: In Formula1, non sono state selezionate le prime 3 posizioni della qualifica.",
                "cat": "formula"
            })
        # Formula2 Errori
        if se_f2:
            check_quali2 = []
            check_spr2 = []
            check_feat2 = []
            spr_fl2_count = 0
            feat_fl2_count = 0
            for variabile in var_f2:
                if variabile[0].startswith("quali-"):
                    if variabile[1] in check_quali2:
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In Formula2, più piloti hanno la stessa posizione in qualifica.",
                            "cat": "formula"
                        })
                    else:
                        check_quali2.append(variabile[1])
                if variabile[0].startswith("spr-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                    if variabile[1] in check_spr2 and variabile[1] != "":
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In Formula2, più piloti hanno la stessa posizione nella Sprint Race.",
                            "cat": "formula"
                        })
                    else:
                        check_spr2.append(variabile[1])
                if variabile[0].startswith("feat-gara") and (variabile[1].isnumeric() or variabile[1] == ""):
                    if variabile[1] in check_feat2 and variabile[1] != "":
                        return render(request, "errore.html", {
                            "message": "GIORNATA NON CALCOLATA: In Formula2, più piloti hanno la stessa posizione nella Feature Race.",
                            "cat": "formula"
                        })
                    else:
                        check_feat2.append(variabile[1])
                if variabile[0].startswith("spr-fl"):
                    spr_fl2_count += 1
                if variabile[0].startswith("feat-fl-"):
                    feat_fl2_count += 1
            if spr_fl2_count != 1:
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In Formula2, ci sono nessun o più Fast Lap nella Sprint Race.",
                    "cat": "formula"
                })
            if feat_fl2_count != 1:
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In Formula2, ci sono nessun o più Fast Lap nella Feature Race.",
                    "cat": "formula"
                })
            if not all(value in ["1", "2", "3"] for value in check_quali2):
                return render(request, "errore.html", {
                    "message": "GIORNATA NON CALCOLATA: In Formula2, non sono state selezionate le prime 3 posizioni della qualifica.",
                    "cat": "formula"
                })
        
        # Sistemiamo bene i valori ricevuti
        # Creiamo un dizionario per ogni pilota di ogni categoria e i valori corrispettivi
        tutti_piloti1 = Formula_piloti.objects.filter(categoria="F1").order_by("nome")
        if se_f2:
            tutti_piloti2 = Formula_piloti.objects.filter(categoria="F2").order_by("nome")
        # Formula1
        tutti_f1 = []
        for pilota in tutti_piloti1:
            utente = {"nome": pilota.nome, 
                "categoria": "F1",
                "qualifica": 0,
                "sprint": 0,
                "sprint-dnf": 0,
                "sprint-fl": 0,
                "feature": 0,
                "feature-dnf": 0,
                "feature-fl": 0,
            }
            utente.setdefault("punti", 0)
            utente.setdefault("punti_team", 0)
            for variabile in var_f1:
                modificatore = variabile[0].split("-")
                if modificatore[-1] == pilota.nome:
                    if modificatore[0] == "quali":
                        utente["qualifica"] = int(variabile[1])
                    elif modificatore[0] == "spr" and modificatore[1] == "gara":
                        if variabile[1] != "":
                            utente["sprint"] = int(variabile[1])
                    elif modificatore[0] == "spr" and modificatore[1] == "dnf":
                        utente["sprint-dnf"] = int(variabile[1])
                    elif modificatore[0] == "spr" and modificatore[1] == "fl":
                        utente["sprint-fl"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "gara":
                        if variabile[1] != "":
                            utente["feature"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "dnf":
                        utente["feature-dnf"] = int(variabile[1])
                    elif modificatore[0] == "feat" and modificatore[1] == "fl":
                        utente["feature-fl"] = int(variabile[1])
            tutti_f1.append(utente)
        # Formula2
        if se_f2:
            tutti_f2 = []
            for pilota in tutti_piloti2:
                utente = {"nome": pilota.nome, 
                    "categoria": "F2",
                    "qualifica": 0,
                    "sprint": 0,
                    "sprint-dnf": 0,
                    "sprint-fl": 0,
                    "feature": 0,
                    "feature-dnf": 0,
                    "feature-fl": 0,
                }
                utente.setdefault("punti", 0)
                utente.setdefault("punti_team", 0)
                for variabile in var_f2:
                    modificatore = variabile[0].split("-")
                    if modificatore[-1] == pilota.nome:
                        if modificatore[0] == "quali":
                            utente["qualifica"] = int(variabile[1])
                        elif modificatore[0] == "spr" and modificatore[1] == "gara":
                            if variabile[1] != "":
                                utente["sprint"] = int(variabile[1])
                        elif modificatore[0] == "spr" and modificatore[1] == "dnf":
                            utente["sprint-dnf"] = int(variabile[1])
                        elif modificatore[0] == "spr" and modificatore[1] == "fl":
                            utente["sprint-fl"] = int(variabile[1])
                        elif modificatore[0] == "feat" and modificatore[1] == "gara":
                            if variabile[1] != "":
                                utente["feature"] = int(variabile[1])
                        elif modificatore[0] == "feat" and modificatore[1] == "dnf":
                            utente["feature-dnf"] = int(variabile[1])
                        elif modificatore[0] == "feat" and modificatore[1] == "fl":
                            utente["feature-fl"] = int(variabile[1])
                tutti_f2.append(utente)
            tutti = {
                "f1": tutti_f1,
                "f2": tutti_f2
            }
        else:
            tutti = {
                "f1": tutti_f1
            }
        
        # È arrivato il momento di calcolare
        # Formula1, liste per controllare i DNF e quindi i Team Manager
        fuori_sprint = []
        fuori_feature = []
        for utente in tutti["f1"]: 
            # Sprint
            if not utente["sprint-dnf"]:
                if utente["sprint"] == 1:
                    utente["punti"] += 8
                    utente["punti_team"] += 8
                elif utente["sprint"] == 2:
                    utente["punti"] += 7
                    utente["punti_team"] += 7
                elif utente["sprint"] == 3:
                    utente["punti"] += 6
                    utente["punti_team"] += 6
                elif utente["sprint"] == 4:
                    utente["punti"] += 5
                    utente["punti_team"] += 5
                elif utente["sprint"] == 5:
                    utente["punti"] += 4
                    utente["punti_team"] += 4
                elif utente["sprint"] == 6:
                    utente["punti"] += 3
                    utente["punti_team"] += 3
                elif utente["sprint"] == 7:
                    utente["punti"] += 2
                    utente["punti_team"] += 2
                elif utente["sprint"] == 8:
                    utente["punti"] += 1
                    utente["punti_team"] += 1
                if utente["sprint-fl"]:
                    utente["punti"] += 1
            else:
                fuori_sprint.append(utente["nome"])
            # Feature
            if not utente["feature-dnf"]:
                if utente["feature"] == 1:
                    utente["punti"] += 25
                    utente["punti_team"] += 25
                elif utente["feature"] == 2:
                    utente["punti"] += 18
                    utente["punti_team"] += 18
                elif utente["feature"] == 3:
                    utente["punti"] += 15
                    utente["punti_team"] += 15
                elif utente["feature"] == 4:
                    utente["punti"] += 12
                    utente["punti_team"] += 12
                elif utente["feature"] == 5:
                    utente["punti"] += 10
                    utente["punti_team"] += 10
                elif utente["feature"] == 6:
                    utente["punti"] += 8
                    utente["punti_team"] += 8
                elif utente["feature"] == 7:
                    utente["punti"] += 6
                    utente["punti_team"] += 6
                elif utente["feature"] == 8:
                    utente["punti"] += 4
                    utente["punti_team"] += 4
                elif utente["feature"] == 9:
                    utente["punti"] += 2
                    utente["punti_team"] += 2
                elif utente["feature"] == 10:
                    utente["punti"] += 1
                    utente["punti_team"] += 1
                if utente["feature-fl"]:
                    utente["punti"] += 1
            else:
                fuori_feature.append(utente["nome"])
            if utente["qualifica"] in [1,2,3]:
                match utente["qualifica"]:
                    case 1: utente["punti"] += 5
                    case 2: utente["punti"] += 3
                    case 3: utente["punti"] += 1
        # Formula2
        if se_f2:
            for utente in tutti["f2"]: 
                # Sprint
                if not utente["sprint-dnf"]:
                    if utente["sprint"] == 1:
                        utente["punti"] += 10
                        utente["punti_team"] += 10
                    elif utente["sprint"] == 2:
                        utente["punti"] += 8
                        utente["punti_team"] += 8
                    elif utente["sprint"] == 3:
                        utente["punti"] += 6
                        utente["punti_team"] += 6
                    elif utente["sprint"] == 4:
                        utente["punti"] += 5
                        utente["punti_team"] += 5
                    elif utente["sprint"] == 5:
                        utente["punti"] += 4
                        utente["punti_team"] += 4
                    elif utente["sprint"] == 6:
                        utente["punti"] += 3
                        utente["punti_team"] += 3
                    elif utente["sprint"] == 7:
                        utente["punti"] += 2
                        utente["punti_team"] += 2
                    elif utente["sprint"] == 8:
                        utente["punti"] += 1
                        utente["punti_team"] += 1
                    if utente["sprint-fl"]:
                        utente["punti"] += 1
                # Feature
                if not utente["feature-dnf"]:
                    if utente["feature"] == 1:
                        utente["punti"] += 25
                        utente["punti_team"] += 25
                    elif utente["feature"] == 2:
                        utente["punti"] += 18
                        utente["punti_team"] += 18
                    elif utente["feature"] == 3:
                        utente["punti"] += 15
                        utente["punti_team"] += 15
                    elif utente["feature"] == 4:
                        utente["punti"] += 12
                        utente["punti_team"] += 12
                    elif utente["feature"] == 5:
                        utente["punti"] += 10
                        utente["punti_team"] += 10
                    elif utente["feature"] == 6:
                        utente["punti"] += 8
                        utente["punti_team"] += 8
                    elif utente["feature"] == 7:
                        utente["punti"] += 6
                        utente["punti_team"] += 6
                    elif utente["feature"] == 8:
                        utente["punti"] += 4
                        utente["punti_team"] += 4
                    elif utente["feature"] == 9:
                        utente["punti"] += 2
                        utente["punti_team"] += 2
                    elif utente["feature"] == 10:
                        utente["punti"] += 1
                        utente["punti_team"] += 1
                    if utente["feature-fl"]:
                        utente["punti"] += 1
                if utente["qualifica"] in [1,2,3]:
                    match utente["qualifica"]:
                        case 1: utente["punti"] += 5
                        case 2: utente["punti"] += 3
                        case 3: utente["punti"] += 1
        
        # Assegna punteggi a Formula_piloti nella gara corrispondente
        for categoria in tutti.items():
            for utente in categoria[1]:
                pilota = Formula_piloti.objects.get(nome=utente["nome"])
                match int(id):
                    case 1: pilota.gara01 = utente["punti"]
                    case 2: pilota.gara02 = utente["punti"]
                    case 3: pilota.gara03 = utente["punti"]
                    case 4: pilota.gara04 = utente["punti"]
                    case 5: pilota.gara05 = utente["punti"]
                    case 6: pilota.gara06 = utente["punti"]
                    case 7: pilota.gara07 = utente["punti"]
                    case 8: pilota.gara08 = utente["punti"]
                    case 9: pilota.gara09 = utente["punti"]
                    case 10: pilota.gara10 = utente["punti"]
                    case 11: pilota.gara11 = utente["punti"]
                    case 12: pilota.gara12 = utente["punti"]
                    case 13: pilota.gara13 = utente["punti"]
                    case 14: pilota.gara14 = utente["punti"]
                    case 15: pilota.gara15 = utente["punti"]
                    case 16: pilota.gara16 = utente["punti"]
                    case 17: pilota.gara17 = utente["punti"]
                    case 18: pilota.gara18 = utente["punti"]
                    case 19: pilota.gara19 = utente["punti"]
                    case 20: pilota.gara20 = utente["punti"]
                    case 21: pilota.gara21 = utente["punti"]
                    case 22: pilota.gara22 = utente["punti"]
                    case 23: pilota.gara23 = utente["punti"]
                pilota.save()
        
        # Assegna i punteggi ai team e tm
        # Ai team basta sommare i due utente["punti_team"] dei due piloti
        global team_formula
        # Per ogni team in tutte le categorie
        for team in team_formula:
            team_punti = 0
            team_piloti = team["piloti"].split("/") # Ritorna ["Bottas", "Zhou"]
            # Cerca Bottas poi Zhou
            for pilota in team_piloti:
                # Per ogni salvataggio nella categoria giusta
                for utenza in tutti[team["cat"]]:
                    # Se il nome è Bottas, assegna i punti_team al team
                    if utenza["nome"] == pilota:
                        team_punti += utenza["punti_team"]
            # Assegna i punti nel database
            team_nome = Formula_team.objects.get(nome=team["nome"])
            match int(id):
                case 1: team_nome.gara01 = team_punti
                case 2: team_nome.gara02 = team_punti
                case 3: team_nome.gara03 = team_punti
                case 4: team_nome.gara04 = team_punti
                case 5: team_nome.gara05 = team_punti
                case 6: team_nome.gara06 = team_punti
                case 7: team_nome.gara07 = team_punti
                case 8: team_nome.gara08 = team_punti
                case 9: team_nome.gara09 = team_punti
                case 10: team_nome.gara10 = team_punti
                case 11: team_nome.gara11 = team_punti
                case 12: team_nome.gara12 = team_punti
                case 13: team_nome.gara13 = team_punti
                case 14: team_nome.gara14 = team_punti
                case 15: team_nome.gara15 = team_punti
                case 16: team_nome.gara16 = team_punti
                case 17: team_nome.gara17 = team_punti
                case 18: team_nome.gara18 = team_punti
                case 19: team_nome.gara19 = team_punti
                case 20: team_nome.gara20 = team_punti
                case 21: team_nome.gara21 = team_punti
                case 22: team_nome.gara22 = team_punti
                case 23: team_nome.gara23 = team_punti
            team_nome.totale += team_punti
            team_nome.save()

        # Ai tm bisogna controllare che nessuno dei due sia DNF nella STESSA gara
        # Sprint e Feature sono considerate gare differenti!
        global tm_formula
        for team_manager in tm_formula:
            segna_sprint = 0
            segna_feature = 0
            posizione_sprint = []
            posizione_feature = []
            tm_punti = 0
            tm_piloti = team_manager["piloti"].split("/")
            # Cerca i piloti trovati in formula1
            for pilota in tm_piloti:
                for utenza in tutti["f1"]:
                    if utenza["nome"] == pilota:
                        # Assicurarsi che non sia DNF
                        # Sprint e Feature sono gare distinte
                        if pilota not in fuori_sprint:
                            segna_sprint += 1
                            posizione_sprint.append(utenza["sprint"])
                        if pilota not in fuori_feature:
                            segna_feature += 1
                            posizione_feature.append(utenza["feature"])
            # Se entrambi i piloti non sono DNF, assegna i punti
            if segna_sprint == 2:
                for posizione in posizione_sprint:
                    match posizione:
                        case 1: tm_punti += 8
                        case 2: tm_punti += 7
                        case 3: tm_punti += 6
                        case 4: tm_punti += 5
                        case 5: tm_punti += 4
                        case 6: tm_punti += 3
                        case 7: tm_punti += 2
                        case 8: tm_punti += 1
            if segna_feature == 2:
                for posizione in posizione_feature:
                    match posizione:
                        case 1: tm_punti += 25
                        case 2: tm_punti += 18
                        case 3: tm_punti += 15
                        case 4: tm_punti += 12
                        case 5: tm_punti += 10
                        case 6: tm_punti += 8
                        case 7: tm_punti += 6
                        case 8: tm_punti += 4
                        case 9: tm_punti += 2
                        case 10: tm_punti += 1
            tm_nome = Formula_teammanager.objects.get(nome=team_manager["nome"])
            match int(id):
                case 1: tm_nome.gara01 = tm_punti
                case 2: tm_nome.gara02 = tm_punti
                case 3: tm_nome.gara03 = tm_punti
                case 4: tm_nome.gara04 = tm_punti
                case 5: tm_nome.gara05 = tm_punti
                case 6: tm_nome.gara06 = tm_punti
                case 7: tm_nome.gara07 = tm_punti
                case 8: tm_nome.gara08 = tm_punti
                case 9: tm_nome.gara09 = tm_punti
                case 10: tm_nome.gara10 = tm_punti
                case 11: tm_nome.gara11 = tm_punti
                case 12: tm_nome.gara12 = tm_punti
                case 13: tm_nome.gara13 = tm_punti
                case 14: tm_nome.gara14 = tm_punti
                case 15: tm_nome.gara15 = tm_punti
                case 16: tm_nome.gara16 = tm_punti
                case 17: tm_nome.gara17 = tm_punti
                case 18: tm_nome.gara18 = tm_punti
                case 19: tm_nome.gara19 = tm_punti
                case 20: tm_nome.gara20 = tm_punti
                case 21: tm_nome.gara21 = tm_punti
                case 22: tm_nome.gara22 = tm_punti
                case 23: tm_nome.gara23 = tm_punti
            tm_nome.totale += tm_punti
            tm_nome.save()

        # Calcola il punteggio di ogni formazione
        for formazione in formazioni:
            totale = 0
            # Piloti
            try:
                for pilota in formazione.piloti.all():
                    match int(id):
                        case 1: totale += Formula_piloti.objects.get(nome=pilota.nome).gara01
                        case 2: totale += Formula_piloti.objects.get(nome=pilota.nome).gara02
                        case 3: totale += Formula_piloti.objects.get(nome=pilota.nome).gara03
                        case 4: totale += Formula_piloti.objects.get(nome=pilota.nome).gara04
                        case 5: totale += Formula_piloti.objects.get(nome=pilota.nome).gara05
                        case 6: totale += Formula_piloti.objects.get(nome=pilota.nome).gara06
                        case 7: totale += Formula_piloti.objects.get(nome=pilota.nome).gara07
                        case 8: totale += Formula_piloti.objects.get(nome=pilota.nome).gara08
                        case 9: totale += Formula_piloti.objects.get(nome=pilota.nome).gara09
                        case 10: totale += Formula_piloti.objects.get(nome=pilota.nome).gara10
                        case 11: totale += Formula_piloti.objects.get(nome=pilota.nome).gara11
                        case 12: totale += Formula_piloti.objects.get(nome=pilota.nome).gara12
                        case 13: totale += Formula_piloti.objects.get(nome=pilota.nome).gara13
                        case 14: totale += Formula_piloti.objects.get(nome=pilota.nome).gara14
                        case 15: totale += Formula_piloti.objects.get(nome=pilota.nome).gara15
                        case 16: totale += Formula_piloti.objects.get(nome=pilota.nome).gara16
                        case 17: totale += Formula_piloti.objects.get(nome=pilota.nome).gara17
                        case 18: totale += Formula_piloti.objects.get(nome=pilota.nome).gara18
                        case 19: totale += Formula_piloti.objects.get(nome=pilota.nome).gara19
                        case 20: totale += Formula_piloti.objects.get(nome=pilota.nome).gara20
                        case 21: totale += Formula_piloti.objects.get(nome=pilota.nome).gara21
                        case 22: totale += Formula_piloti.objects.get(nome=pilota.nome).gara22
                        case 23: totale += Formula_piloti.objects.get(nome=pilota.nome).gara23
            except:
                pass 
            # Teams               
            try:
                for team in formazione.team.all():
                    match int(id):
                        case 1: totale += Formula_team.objects.get(nome=team.nome).gara01
                        case 2: totale += Formula_team.objects.get(nome=team.nome).gara02
                        case 3: totale += Formula_team.objects.get(nome=team.nome).gara03
                        case 4: totale += Formula_team.objects.get(nome=team.nome).gara04
                        case 5: totale += Formula_team.objects.get(nome=team.nome).gara05
                        case 6: totale += Formula_team.objects.get(nome=team.nome).gara06
                        case 7: totale += Formula_team.objects.get(nome=team.nome).gara07
                        case 8: totale += Formula_team.objects.get(nome=team.nome).gara08
                        case 9: totale += Formula_team.objects.get(nome=team.nome).gara09
                        case 10: totale += Formula_team.objects.get(nome=team.nome).gara10
                        case 11: totale += Formula_team.objects.get(nome=team.nome).gara11
                        case 12: totale += Formula_team.objects.get(nome=team.nome).gara12
                        case 13: totale += Formula_team.objects.get(nome=team.nome).gara13
                        case 14: totale += Formula_team.objects.get(nome=team.nome).gara14
                        case 15: totale += Formula_team.objects.get(nome=team.nome).gara15
                        case 16: totale += Formula_team.objects.get(nome=team.nome).gara16
                        case 17: totale += Formula_team.objects.get(nome=team.nome).gara17
                        case 18: totale += Formula_team.objects.get(nome=team.nome).gara18
                        case 19: totale += Formula_team.objects.get(nome=team.nome).gara19
                        case 20: totale += Formula_team.objects.get(nome=team.nome).gara20
                        case 21: totale += Formula_team.objects.get(nome=team.nome).gara21
                        case 22: totale += Formula_team.objects.get(nome=team.nome).gara22
                        case 23: totale += Formula_team.objects.get(nome=team.nome).gara23
            except:
                pass
            # Team Manager
            try:
                tm = formazione.teammanager
                match int(id):
                    case 1: totale += Formula_teammanager.objects.get(nome=tm.nome).gara01
                    case 2: totale += Formula_teammanager.objects.get(nome=tm.nome).gara02
                    case 3: totale += Formula_teammanager.objects.get(nome=tm.nome).gara03
                    case 4: totale += Formula_teammanager.objects.get(nome=tm.nome).gara04
                    case 5: totale += Formula_teammanager.objects.get(nome=tm.nome).gara05
                    case 6: totale += Formula_teammanager.objects.get(nome=tm.nome).gara06
                    case 7: totale += Formula_teammanager.objects.get(nome=tm.nome).gara07
                    case 8: totale += Formula_teammanager.objects.get(nome=tm.nome).gara08
                    case 9: totale += Formula_teammanager.objects.get(nome=tm.nome).gara09
                    case 10: totale += Formula_teammanager.objects.get(nome=tm.nome).gara10
                    case 11: totale += Formula_teammanager.objects.get(nome=tm.nome).gara11
                    case 12: totale += Formula_teammanager.objects.get(nome=tm.nome).gara12
                    case 13: totale += Formula_teammanager.objects.get(nome=tm.nome).gara13
                    case 14: totale += Formula_teammanager.objects.get(nome=tm.nome).gara14
                    case 15: totale += Formula_teammanager.objects.get(nome=tm.nome).gara15
                    case 16: totale += Formula_teammanager.objects.get(nome=tm.nome).gara16
                    case 17: totale += Formula_teammanager.objects.get(nome=tm.nome).gara17
                    case 18: totale += Formula_teammanager.objects.get(nome=tm.nome).gara18
                    case 19: totale += Formula_teammanager.objects.get(nome=tm.nome).gara19
                    case 20: totale += Formula_teammanager.objects.get(nome=tm.nome).gara20
                    case 21: totale += Formula_teammanager.objects.get(nome=tm.nome).gara21
                    case 22: totale += Formula_teammanager.objects.get(nome=tm.nome).gara22
                    case 23: totale += Formula_teammanager.objects.get(nome=tm.nome).gara23
            except:
                pass
            # Con i try dovrei aver escluso chi non ha schierato la formazione
            formazione.p_totali = totale
            formazione.save()

        # Controlla chi hai contro e vedi chi ha vinto
        global sfide_formula
        sfide_giornata = sfide_formula[1]["sfida"]
        sfide_giornata = sfide_giornata.split("/")
        scontri = []
        for i in sfide_giornata:
            scontri.append(i.split("+"))
        for scontro in scontri:
            form_user1 = Formula_formazione.objects.get(giornata=id, username=scontro[0])
            form_user2 = Formula_formazione.objects.get(giornata=id, username=scontro[1])
            punti_user1 = Formula_punti.objects.get(username=scontro[0])
            punti_user2 = Formula_punti.objects.get(username=scontro[1])
            # Se user1 vince
            if form_user1.p_totali > form_user2.p_totali:
                # Indica nella formazione chi ha vinto
                form_user1.risultato = 1
                form_user2.risultato = 0
                # Aggiungi punti scontri a chi ha vinto
                punti_user1.p_scontri += 3
                # Aggiungi punti generali 
                punti_user1.p_generali += form_user1.p_totali
                punti_user2.p_generali += form_user2.p_totali
                # Aggiorna la differenza punti
                differenza = form_user1.p_totali - form_user2.p_totali
                punti_user1.differenza += differenza
                punti_user2.differenza -= differenza
            # Se user2 vince
            elif form_user1.p_totali < form_user2.p_totali:
                # Indica nella formazione chi ha vinto
                form_user1.risultato = 0
                form_user2.risultato = 1
                # Aggiungi punti scontri a chi ha vinto
                punti_user2.p_scontri += 3
                # Aggiungi punti generali 
                punti_user1.p_generali += form_user1.p_totali
                punti_user2.p_generali += form_user2.p_totali
                # Aggiorna la differenza punti
                differenza = form_user2.p_totali - form_user1.p_totali
                punti_user1.differenza -= differenza
                punti_user2.differenza += differenza
            # Se pareggio
            else:
                # Indica nella formazione il pareggio ._.
                form_user1.risultato = 2
                form_user2.risultato = 2
                # Aggiungi punti scontri ad entrambi
                punti_user1.p_scontri += 1
                punti_user2.p_scontri += 1
                # Aggiungi punti generali 
                punti_user1.p_generali += form_user1.p_totali
                punti_user2.p_generali += form_user2.p_totali
                # Nessun cambio alla differenza punti
            form_user1.save()
            form_user2.save()
            punti_user1.save()
            punti_user2.save()
    
        # Una volta inseriti TUTTI i valori nel database, considera la giornata calcolata
        questa_giornata = Formula_giornata.objects.get(id=id)
        questa_giornata.calcolata = 1
        questa_giornata.save()
        # Reindirizza alla home
        return HttpResponseRedirect(reverse("fantaformula"))

    # Se si sta facendo una richiesta GET, mostra pagina
    # Se la data della gara è nel futuro, mostra errore
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
        sprint = Formula_giornata.objects.get(id=id).sprint
        f2 = Formula_giornata.objects.get(id=id).f2
        piloti1 = Formula_piloti.objects.filter(categoria="F1").order_by("nome")
        piloti2 = Formula_piloti.objects.filter(categoria="F2").order_by("nome")
    else:
        return render(request, "errore.html", {
            "message": f"LA GARA SELEZIONATA ({posto}) È GIÀ STATA CALCOLATA!",
            "cat": "formula"
        })
    return render(request, "fantaformula/calcolo_gara.html", {
        "id": id,
        "posto": posto,
        "sprint": sprint,
        "f2": f2,
        "piloti1": piloti1,
        "piloti2": piloti2,
        "cat": "formula"
    })

