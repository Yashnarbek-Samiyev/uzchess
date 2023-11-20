from django.contrib import admin
from .models import Main, Country, Languages, Player1, Player2, Reyting, Plays, Notice

# Register your models here.
admin.site.register(Main)
admin.site.register(Country)
admin.site.register(Languages)
admin.site.register(Player1)
admin.site.register(Player2)
admin.site.register(Reyting)
admin.site.register(Plays)
admin.site.register(Notice)
