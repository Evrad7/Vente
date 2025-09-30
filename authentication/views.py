from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import InscriptionForm
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CompteModificationForm
from django.http import JsonResponse
from gestion.models import Panier


# Create your views here.


class Login(LoginView):
    template_name="authentication/connexion.html"

class Logout(LogoutView):
    pass


def inscription(request):
    if request.method=="POST":
        form=InscriptionForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password1=form.cleaned_data["password1"]
            password2=form.cleaned_data["password2"]
            if password1!=password2:
                error="Les mots deux mots de passe sont differents"
                return render(request, "authentication/inscription.html", {"form":form, "error":error})
            else:
                try:
                    user=User.objects.create_user(username=username, email=email, password=password1)
                except IntegrityError:
                    error="Nom utilisateur déja occupé."
                    return render(request, "authentication/inscription.html", {"form":form, "error":error})


        
            return redirect(reverse("achat:acceuil"))
        return render(request, "authentication/inscription.html", {"form":form})

    else:
        form=InscriptionForm()
        return render(request, "authentication/inscription.html", {"form":form})


def compteModification(request):

    if request.method=="POST":
        form=CompteModificationForm(request.POST, instance=request.user)
        if form.is_valid():
            if form.cleaned_data["email"]=="":
                form.errors["email"]="Ce champ est obligatoire"
                return JsonResponse({"errors":form.errors})
            form.save()
            return JsonResponse({})
        return JsonResponse({"errors":form.errors})

    form=CompteModificationForm(instance=request.user)
    context={"form":form}
    return render(request, "authentication/compte-modification.html", context)


@login_required()
def compte(request):
    return render(request, "authentication/compte.html", locals())

