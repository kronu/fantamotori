from django.contrib import admin
from .models import Moto_giornata, Moto_formazione, Moto_piloti, Moto_punti, Moto_team, Moto_teammanager, User, Formula_giornata, Formula_formazione, Formula_piloti, Formula_punti, Formula_team, Formula_teammanager

admin.site.register(User)
admin.site.register(Moto_giornata)
admin.site.register(Moto_formazione)
admin.site.register(Moto_piloti)
admin.site.register(Moto_team)
admin.site.register(Moto_teammanager)
admin.site.register(Moto_punti)
admin.site.register(Formula_giornata)
admin.site.register(Formula_formazione)
admin.site.register(Formula_piloti)
admin.site.register(Formula_team)
admin.site.register(Formula_teammanager)
admin.site.register(Formula_punti)