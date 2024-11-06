from django.urls import path
from .views import acceuil, details, detailsAjax, chargerImages,  cathegories, articlesAjax,\
panier, ajoutPanier, commanderAjax, commande, supprimerArticlePanierAjax, destinationPaysAjax,\
 destinationRegionAjax, destinationVilleAjax, destinationQuartierAjax, searchAjax


urlpatterns=[
 path("acceuil/", acceuil, name="acceuil"),
 path("articles/ajax/", articlesAjax, name="articles_ajax"),
 path("details/<int:pk>/", details, name="details"),
 path("details/<int:pk>/ajax/", detailsAjax, name="details_ajax"),
 path("details/charger_images/", chargerImages, name="charger_images"),
 path("cathegories/", cathegories, name="cathegories"),
 path("panier/", panier, name="panier"),
 path("details/<int:pk>/ajout_panier/", ajoutPanier, name="ajout_panier"),
 path("panier/commander_ajax/", commanderAjax, name="commander_ajax"),
 path("commande/", commande, name="commande"),
 path("commande/destination_pays_ajax/", destinationPaysAjax),
 path("commande/destination_region_ajax/", destinationRegionAjax),
 path("commande/destination_ville_ajax/", destinationVilleAjax),
 path("commande/destination_quartier_ajax/", destinationQuartierAjax),
 path("panier/supprimer_article_panier_ajax", supprimerArticlePanierAjax),
 path("search_ajax/", searchAjax),
]
