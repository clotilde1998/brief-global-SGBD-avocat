from django.contrib import admin

from .models import Clients, Personnels, Dossiers, Conseils, Redactions

admin.site.register(Clients)
admin.site.register(Personnels)
admin.site.register(Dossiers)
admin.site.register(Conseils)
admin.site.register(Redactions)

# Register your models here.
