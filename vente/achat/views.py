from django.shortcuts import render, get_object_or_404, HttpResponse
from gestion.models import Cathegorie, Article, TypeArticle, PhotosTypeArticle, Panier
from django.db.models import F, Q
from collections import OrderedDict
from django.http import JsonResponse, Http404
from achat.templatetags.format_price import *
from django.contrib.auth.models import  AnonymousUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import DestinationForm
from destination.models import Pays, Region, Ville, Quartier, Adresse

# Create your views here.


def acceuil(request):
    cathegories=Cathegorie.objects.filter(cathegorie_superieure=None)
    articles=Article.objects.annotate(prix_non_reduit=F("prix")/(1-F("reduction")*0.01))
    return render(request, "achat/acceuil.html", {"cathegories":cathegories, "articles":articles})


def details(request, pk):
    article=get_object_or_404(Article, pk=pk)
    articlePrixNonReduit=article.prix/(1-article.reduction*0.01)
    typesArticles=article.typearticle_set.order_by("-quantite_disponible")

    couleursArticles=typesArticles.values_list("couleur", flat=True).distinct()
    couleursArticles=list(OrderedDict.fromkeys(couleursArticles))
    typesArticles=typesArticles.filter(couleur=couleursArticles[0])
    articles=[]
    cathegories=article.cathegorie.all()
    for cathegorie in cathegories:
        accompagnement=cathegorie.accompagnement
        if accompagnement is not  None:
            articles=articlesAccompagnement(accompagnement, article, articles)




    #On definit la valeur par defaut selon un algorithme. Nous obtenons pour la plus grande
    #valeur du type d'article dans la base de donnée
    context={
    "article":article,
     "articles":articles,
     "types_articles":typesArticles,
     "couleurs_articles":couleursArticles,
     "article_prix_non_reduit":articlePrixNonReduit,
      }


    return render(request, "achat/details.html", context)

def articlesAccompagnement(accompagnement, article, articles=[]):
    #Algorithme qui trie les articles par convenence: marchandising
    sousCathegories=Cathegorie.objects.filter(cathegorie_superieure__pk__contains=accompagnement.pk)
    if len(sousCathegories)==0:
        articles.append(accompagnement.article_set.exclude(pk=article.pk).annotate(prix_non_reduit=F("prix")/(1-F("reduction")*0.01)))
        return articles
    else:
        for _ in sousCathegories:
            articles=(articlesAccompagnement(_, article, articles))
        return articles



def detailsAjax(request, pk):
    article=get_object_or_404(Article, pk=pk)
    q=request.GET["q"]
    typesArticles=article.typearticle_set.filter(couleur=q).order_by("-quantite_disponible")
    #On definit la valeur par defaut selon un algorithme. Nous obtenons pour la plus grande
    #valeur du type d'article dans la base de donnée
    typesArticles=list(typesArticles.values("taille", "quantite_disponible", "photos"))

    context={
     "types_articles":typesArticles,
      }
    return  JsonResponse(context)

def chargerImages(request):
    q=request.GET["q"]
    photos=get_object_or_404(PhotosTypeArticle, pk=q)
    context={"pk": photos.pk, "photo1":photos.photo1.url, "photo2":photos.photo2.url}
    try:
        context["photo3"]=photos.photo3.url

    except ValueError:
        pass

    return JsonResponse(context)


def articlesAjax(request):
    try:
        q=request.GET["q"]
        q=int(q)
        cathegorie=Cathegorie.objects.get(pk=q)
        articles=articlesParCathegorie(cathegorie, articles=[])
    except:
        articles=Article.objects.all().annotate(prix_non_reduit=F("prix")/(1-F("reduction")*0.01))
        articles=list(articles.values("pk", "photo", "nom", "prix", "reduction", "prix_non_reduit",))

    return JsonResponse({"articles": articles[:30]})





def articlesParCathegorie(cathegorie, articles=[]):
    #Retourne les articles d'une cathegorie.
    sousCathegories=Cathegorie.objects.filter(cathegorie_superieure__pk__contains=cathegorie.pk)
    articles_=Article.objects.filter(cathegorie=cathegorie).annotate(prix_non_reduit=F("prix")/(1-F("reduction")*0.01))
    articles_=list(articles_.values("pk", "photo", "nom", "prix", "reduction", "prix_non_reduit",))
    articles.extend(articles_)
    if len(sousCathegories)==0:
        return articles
    else:
        for _ in sousCathegories:
            articles=articlesParCathegorie(_, articles)
    return articles


def cathegories(request):
    context={}
    cathegories=Cathegorie.objects.all()
    print(request.GET)
    try:
        search=request.GET["search"].strip()
    except KeyError:
        articles=Article.objects.annotate(prix_non_reduit=F("prix")/(1-F("reduction")*0.01))[:30]
    else:
        articles1=Article.objects.filter(nom__contains=search)
        articles2=Article.objects.filter(cathegorie__nom__contains=search)
        articles=articles1.union(articles2)
        print(articles)
        context["search"]=search
    context["cathegories"]=cathegories
    context["articles"]=articles


    return render(request, "achat/cathegories.html", context)

@login_required()
def panier(request):
    try:
        typesArticlesPanier=request.user.panier.types_articles.through.objects.select_related("typearticle").filter(panier__user=request.user).order_by("-pk")
    except User.panier.RelatedObjectDoesNotExist:
        panier=Panier.objects.create(user=request.user)
        typesArticlesPanier=request.user.panier.types_articles.through.objects.select_related("typearticle").filter(panier__user=request.user).order_by("-pk")
    return render(request, "achat/panier.html", locals())


@login_required()
def commanderAjax(request):
    print(request.session.keys())
    print(request.POST)
    error=False
    request.session["commande"]={}
    for pk, quantite  in request.POST.items():
        try:
            pk=int(pk)
            quantite=int(quantite)
            typeArticle=get_object_or_404(TypeArticle, pk=pk)
            if quantite>0 & quantite<typeArticle.quantite_disponible:
                request.session["commande"][pk]=quantite
            else:
                raise ValueError
        except:error=True
    return JsonResponse({"error":error})

@login_required()
def commande(request):
    form=DestinationForm(label_suffix="")
    print(form["pays"].label_tag())
    prixTotal=0
    commandeNulle=False
    try:
        commande=request.session["commande"]
    except KeyError:
        commandeNulle=True
    else:

        for pk, quantite in commande.items():
            typeArticle=TypeArticle.objects.get(pk=int(pk))
            prixTotal+=typeArticle.article.prix*int(quantite)
        if prixTotal==0:
            commandeNulle=True

    context={
    "commande_nulle":commandeNulle,
    "prix_total":prixTotal,
    "form":form,
    }

    return render(request, "achat/commande.html", context )

def destinationPaysAjax(request):
    response=False
    if request.method=="POST":
        try:
            pays=Pays.objects.get(pk=int(request.POST["pays"]))
        except:
            response=False
        else:
            response={}
            regions=DestinationForm.getChoicesRegion(pays=pays.pk)
            if len(regions)!=0:
                response["regions"]=regions
                villes=DestinationForm.getChoicesVille(region=regions[0][0])
                if len(villes)!=0:
                    response["villes"]=villes
                    quartiers=DestinationForm.getChoicesQuartier(ville=villes[0][0])
                    if len(quartiers)!=0:
                        response["quartiers"]=quartiers
                        adresses=DestinationForm.getChoicesAdresse(quartier=quartiers[0][0])
                        if len(adresses)!=0:
                            response["adresses"]=adresses
    return JsonResponse({"response":response})

def destinationRegionAjax(request):
    response=False
    if request.method=="POST":
        try:
            region=Region.objects.get(pk=int(request.POST["region"]))
        except:
            response=False
        else:
            response={}
            villes=DestinationForm.getChoicesVille(region=region)
            if len(villes)!=0:
                response["villes"]=villes
                quartiers=DestinationForm.getChoicesQuartier(ville=villes[0][0])
                if len(quartiers)!=0:
                    response["quartiers"]=quartiers
                    adresses=DestinationForm.getChoicesAdresse(quartier=quartiers[0][0])
                    if len(adresses)!=0:
                        response["adresses"]=adresses
    return JsonResponse({"response":response})

def destinationVilleAjax(request):
    response=False
    if request.method=="POST":
        try:
            ville=Ville.objects.get(pk=int(request.POST["ville"][0]))
        except:
            response=False
        else:
            response={}
            quartiers=DestinationForm.getChoicesQuartier(ville=ville)
            if len(quartiers)!=0:
                response["quartiers"]=quartiers
                adresses=DestinationForm.getChoicesAdresse(quartier=quartiers[0][0])
                if len(adresses)!=0:
                    response["adresses"]=adresses
    return JsonResponse({"response":response})

def destinationQuartierAjax(request):
    response=False
    if request.method=="POST":
        try:
            quartier=Quartier.objects.get(pk=int(request.POST["quartier"]))
        except:
            response=False
        else:
            response={}
            adresses=DestinationForm.getChoicesAdresse(quartier=quartier)
            if len(adresses)!=0:
                response["adresses"]=adresses

    return JsonResponse({"response":response})









def ajoutPanier(request, pk):
    if request.user.is_authenticated:
        article=get_object_or_404(Article, pk=pk)
        try:
            couleur=request.GET["c"]
            taille=request.GET["t"]
        except:
            raise Http404
        typeArticle=get_object_or_404(TypeArticle, article=article, couleur=couleur, taille=taille)
        try:
            count=request.user.panier.types_articles.filter(pk=typeArticle.pk).count()
        except Panier.DoesNotExist:
            panier=Panier.objects.create()
            panier.user=request.user
            panier.save()
            count=0

        if count==0:
            request.user.panier.types_articles.add(typeArticle)
            request.user.save()
            response={"exists":False}
        else:
            response={"exists":True}

    else:
        response={"error":True}
    return JsonResponse(response)


def supprimerArticlePanierAjax(request):
    error=False
    try:
        pk=int(request.GET["pk"])
        typeArticle=TypeArticle.objects.get(pk=pk)
        request.user.panier.types_articles.remove(typeArticle)
        request.user.panier.save()
        count=request.user.panier.types_articles.count()
    except:
        error=True

    return JsonResponse({"error":error, "count":count})


def searchAjax(request):
    error=False
    propositions=[]
    try:
        search=request.GET["q"].strip()
    except:
        error=True
    if search!="":
        articles=Article.objects.filter(nom__startswith=search)
        cathegories=Cathegorie.objects.filter(nom__startswith=search)
        propositions.extend(list(articles.values_list("nom")))
        propositions.extend(list(cathegories.values_list("nom")))

    return JsonResponse({"error":error, "propositions":propositions})
