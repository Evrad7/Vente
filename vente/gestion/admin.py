from django.contrib import admin
from. models import Article, Cathegorie, TypeArticle, Panier, PhotosTypeArticle, Panier
from .forms import ArticleAdminForm

# Register your models here.

class TypeArticleInline(admin.TabularInline):
    model=TypeArticle
    fields=["photos", "couleur", "taille", "quantite_disponible"]
    extra=2



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form=ArticleAdminForm
    exclude=[]
    list_display=["nom", "photo",  "prix", "reduction", "like", "origine"]
    inlines=[TypeArticleInline]
    list_search=["nom", "prix", "like"]
    list_filter=["cathegorie", ]




@admin.register(Cathegorie)
class CathegorieAdmin(admin.ModelAdmin):

    exclude=[]

@admin.register(PhotosTypeArticle)
class PhotosTypeArticleAdmin(admin.ModelAdmin):
    exclude=[]

@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    exclude=[]
