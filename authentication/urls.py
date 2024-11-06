from django.urls import path
from .views import Login, inscription, compte, Logout, compteModification

urlpatterns=[
path("connexion/", Login.as_view(), name="connexion"),
path("deconnexion/", Logout.as_view(), name="deconnexion"),
path("inscription/", inscription, name="inscription"),
path("compte/", compte, name="compte"),
path("compte/modification/", compteModification, name="compte-modification"),

]
