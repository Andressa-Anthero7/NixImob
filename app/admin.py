from django.contrib import admin
from .models import Proposta, Perfil, Anuncio, Imagens

# Register your models here.

admin.site.register(Proposta)
admin.site.register(Perfil)
admin.site.register(Anuncio)
admin.site.register(Imagens)