# Raccolta di tutti gli url delle pagine del sito
from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("", views.scelta, name="index"),
    path("user", views.utente, name="utente"),
    # Fantamoto
    path("fantamoto", views.moto_home, name="fantamoto"),
    path("fantamoto/rose", views.moto_rose, name="fantamoto/rose"),
    path("fantamoto/rose/<utente>", views.moto_rosautente, name="fantamoto/rosautente"),
    path("fantamoto/calendario", views.moto_calendario, name="fantamoto/calendario"),
    path("fantamoto/<id>/<scontro>", views.moto_scontro, name="fantamoto/scontro"),
    path("fantamoto/albo", views.moto_albo, name="fantamoto/albo"),
    path("fantamoto/calcolo", views.moto_calcoloscelta, name="fantamoto/calcolo"),
    path("fantamoto/calcolo-<id>", views.moto_calcologara, name="fantamoto/calcolo_giornata"),
    path("fantamoto/formazione", views.moto_formazione, name="fantamoto/formazione"),
    path("fantamoto/schieramento", views.moto_schieramento, name="fantamoto/schieramento"),
    path("fantamoto/adm-piloti", views.moto_admpiloti, name="fantamoto/adm-piloti"),
    path("fantamoto/adm-team", views.moto_admteam, name="fantamoto/adm-team"),
    path("fantamoto/adm-gara", views.moto_admgara, name="fantamoto/adm-gara"),
    # Fantaformula
    path("fantaformula", views.formula_home, name="fantaformula"),
    path("fantaformula/rose", views.formula_rose, name="fantaformula/rose"),
    path("fantaformula/rose/<utente>", views.formula_rosautente, name="fantaformula/rosautente"),
    path("fantaformula/calendario", views.formula_calendario, name="fantaformula/calendario"),
    path("fantaformula/<id>/<scontro>", views.formula_scontro, name="fantaformula/scontro"),
    path("fantaformula/albo", views.formula_albo, name="fantaformula/albo"),
    path("fantaformula/calcolo", views.formula_calcoloscelta, name="fantaformula/calcolo"),
    path("fantaformula/calcolo-<id>", views.formula_calcologara, name="fantaformula/calcolo_giornata"),
    path("fantaformula/formazione", views.formula_formazione, name="fantaformula/formazione"),
    path("fantaformula/schieramento", views.formula_schieramento, name="fantaformula/schieramento"),
    path("fantaformula/adm-piloti", views.formula_admpiloti, name="fantaformula/adm-piloti"),
    path("fantaformula/adm-team", views.formula_admteam, name="fantaformula/adm-team"),
    path("fantaformula/adm-gara", views.formula_admgara, name="fantaformula/adm-gara"),
]