from django.contrib import admin
from .models import *


class AdresseInline(admin.TabularInline):
    model=Adresse
    fields=["nom"]
    extra=1

class QuartierInline(admin.TabularInline):
    model=Quartier
    fields=["nom"]
    extra=1

class VilleInline(admin.TabularInline):
    model=Ville
    extra=1
    fields=["nom"]

class RegionInline(admin.TabularInline):
    model=Region
    extra=1
    fields=["nom"]


@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    fields=["nom"]
    inlines=[RegionInline]

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    #readonly_fields=["nom"]
    fields=["nom"]
    list_display=["nom", "pays"]
    search_fields=["nom", "pays"]
    list_filter=["pays"]

    inlines=[VilleInline]

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    fields=["nom"]
    list_display=["nom", "region"]
    search_fields=["nom", "region__nom"]
    list_filter=["region__pays", "region"]
    inlines=[QuartierInline]

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Quartier)
class QuartierAdmin(admin.ModelAdmin):
    fields=["nom"]
    list_display=["nom", "ville"]
    search_fields=["nom", "ville__nom", "ville__region__nom"]
    list_filter=["ville__region__pays", "ville__region", "ville"]
    inlines=[AdresseInline]

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Adresse)
class AdresseAdmin(admin.ModelAdmin):
    fields=["nom"]
    list_display=["nom", "quartier"]
    search_fields=["nom", "quartier__nom", "quartier__nom__ville"]
    list_filter=["quartier__ville__region__pays", "quartier__ville__region", "quartier__ville"]

    def has_add_permission(self, request, obj=None):
        return False
