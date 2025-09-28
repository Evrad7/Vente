from django import forms
from destination.models import *




class DestinationForm(forms.Form):
    default=1

    def getChoicesPays():
        choices=[]
        for _ in Pays.objects.all():
            choices.append((_.id,_.nom))
        return choices

    def getChoicesRegion(pays=default):
        choices=[]
        for _ in Region.objects.filter(pays=pays):
            choices.append((_.id,_.nom))
        return choices

    def getChoicesVille(region=2):
        choices=[]
        for _ in Ville.objects.filter(region=region):
            choices.append((_.id,_.nom))
        return choices

    def getChoicesQuartier(ville=1):
        choices=[]
        for _ in Quartier.objects.filter(ville=ville):
            choices.append((_.id,_.nom))
        return choices


    def getChoicesAdresse(quartier=1):
        choices=[]
        for _ in Adresse.objects.filter(quartier=quartier):
            choices.append((_.id,_.nom))
        return choices





    pays=forms.ChoiceField(choices=getChoicesPays, initial="Cameroun", widget=forms.Select(attrs={"class":"form-control"}))
    region=forms.ChoiceField(choices=getChoicesRegion, widget=forms.Select(attrs={"class":"form-control"}))
    ville=forms.ChoiceField(choices=getChoicesVille, widget=forms.Select(attrs={"class":"form-control"}))
    quartier=forms.ChoiceField(choices=getChoicesQuartier, widget=forms.Select(attrs={"class":"form-control"}))
    adresse=forms.ChoiceField(choices=getChoicesAdresse, widget=forms.Select(attrs={"class":"form-control"}))
