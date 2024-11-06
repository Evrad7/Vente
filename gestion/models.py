from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Cathegorie(models.Model):
    photo = models.ImageField(upload_to="image_cathegorie")
    nom = models.CharField(max_length=15)
    accompagnement = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL)
    cathegorie_superieure = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="sous_cathegories")

    def __str__(self):
        cathegories = [_.nom for _ in self.cathegorie_superieure.all()]
        if len(cathegories) == 0:
            return self.nom
        else:
            return "{}({})".format(self.nom, ",   ".join(cathegories))


class Article(models.Model):
    photo = models.ImageField(upload_to="image_article")
    nom = models.CharField(max_length=30)
    prix = models.FloatField(validators=[MinValueValidator(0)])
    reduction = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)])
    like = models.PositiveIntegerField(default=0)
    cathegorie = models.ManyToManyField(Cathegorie)
    origine = models.CharField(max_length=15, default="/")
    description = models.TextField(default="/")
    url = models.URLField(default="fdsfqffds")

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("achat:details", args=[self.pk])

        class Meta:
            verbose_name = "article"
            verbose_name_plural = "articles"


class PhotosTypeArticle(models.Model):
    nom = models.CharField(max_length=30)
    photo1 = models.ImageField(upload_to="image_type_article")
    photo2 = models.ImageField(upload_to="image_type_article")
    photo3 = models.ImageField(
        upload_to="image_type_article", null=True, blank=True)

    def __str__(self):
        return self.nom


class TypeArticle(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.SET_NULL, null=True, blank=True)
    couleur = models.CharField(max_length=15)
    taille = models.CharField(max_length=10)
    quantite_disponible = models.PositiveSmallIntegerField()
    photos = models.ForeignKey(
        PhotosTypeArticle, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        # return "{}__{}__{}".format(self.article.nom, self.couleur, self.taille)
        return f"{self.pk}"


class Panier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    types_articles = models.ManyToManyField(TypeArticle, blank=True)
