from django.urls import path
from . import views

urlpatterns = [
    path("", views.sceltafanta, name="sceltafanta"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    # Fantamoto
    path("fantamoto/home", views.moto_home, name="fantamoto/home"),
    path("fantamoto/classifica_scontri", views.moto_classscontri, name="fantamoto/classifica_scontri"),
    path("fantamoto/classifica_punti", views.moto_classpunti, name="fantamoto/classifica_punti"),
    path("fantamoto/rose", views.moto_rose, name="fantamoto/rose"),
    path("fantamoto/rosa_<utente>", views.moto_rosautente, name="moto_rosautente"),
    path("fantamoto/calendario", views.moto_cal_scelta, name="fantamoto/calendario"),
    path("fantamoto/calendario/<id>", views.moto_calendario, name="moto_calendario"),
    path("fantamoto/calendario/<id>/<scontro>", views.moto_scontro, name="moto_scontro"),
    path("fantamoto/scelta_formazione", views.moto_formazione, name="fantamoto/scelta_formazione"),
    path("fantamoto/schieramento", views.moto_schieramento, name="fantamoto/schieramento"),
    path("fantamoto/calcolo_scelta", views.moto_calcscelta, name="fantamoto/calcolo_scelta"),
    path("fantamoto/calcolo_formazione/<id>/<utente>", views.moto_calcformazione, name="fantamoto/calcolo_formazione"),
    path("fantamoto/calcolo_formazione/<id>/<utente>/calcolo", views.moto_calctotale, name="moto_calcolo"),
    # Fantaformula
    path("fantaformula/home", views.formula_home, name="fantaformula/home"),
    path("fantaformula/classifica_scontri", views.formula_classscontri, name="fantaformula/classifica_scontri"),
    path("fantaformula/classifica_punti", views.formula_classpunti, name="fantaformula/classifica_punti"),
    path("fantaformula/rose", views.formula_rose, name="fantaformula/rose"),
    path("fantaformula/rosa_<utente>", views.formula_rosautente, name="formula_rosautente"),
    path("fantaformula/calendario", views.formula_cal_scelta, name="fantaformula/calendario"),
    path("fantaformula/calendario/<id>", views.formula_calendario, name="formula_calendario"),
    path("fantaformula/calendario/<id>/<scontro>", views.formula_scontro, name="formula_scontro"),
    path("fantaformula/scelta_formazione", views.formula_formazione, name="fantaformula/scelta_formazione"),
    path("fantaformula/schieramento", views.formula_schieramento, name="fantaformula/schieramento"),
    path("fantaformula/calcolo_scelta", views.formula_calcscelta, name="fantaformula/calcolo_scelta"),
    path("fantaformula/calcolo_formazione/<id>/<utente>", views.formula_calcformazione, name="fantaformula/calcolo_formazione"),
    path("fantaformula/calcolo_formazione/<id>/<utente>/calcolo", views.formula_calctotale, name="formula_calcolo"),
]