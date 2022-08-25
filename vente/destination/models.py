from django.db import models

# Create your models here.



class Pays(models.Model):
    nom=models.CharField(max_length=50)

    class Meta:
        verbose_name="pays"
        verbose_name_plural="pays"

    def __str__(self):
        return self.nom

class Region(models.Model):
    nom=models.CharField(max_length=50)
    pays=models.ForeignKey(Pays, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.pays.nom}__{self.nom}"

class Ville(models.Model):
    nom=models.CharField(max_length=50)
    region=models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.region.pays.nom}__{self.region.nom}__{self.nom}"

class Quartier(models.Model):
    nom=models.CharField(max_length=50)
    ville=models.ForeignKey(Ville, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ville.region.pays.nom}__{self.ville.region.nom}__{self.ville.nom}__{self.nom}"

class Adresse(models.Model):
    nom=models.CharField(max_length=50)
    quartier=models.ForeignKey(Quartier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quartier.ville.region.pays.nom}__{self.quartier.ville.region.nom}__{self.quartier.ville.nom}__{self.quartier.nom}__{self.nom}"
