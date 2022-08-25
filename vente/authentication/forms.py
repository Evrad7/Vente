from django import forms
from django.contrib.auth.models import User


class InscriptionForm(forms.ModelForm):
    password1=forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"mot de passe"}))
    password2=forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"confirmer le mot de passe"}))

    class Meta:
        model=User
        fields=["username","email"]
        widgets={
        "username":forms.TextInput(attrs={"class":"form-control", "placeholder":"nom utilisateur"}),
        "email":forms.EmailInput(attrs={"class":"form-control", "placeholder":"email"}),
        }



class CompteModificationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"class":"form-control"})
        self.fields["email"].widget.attrs.update({"class":"form-control"})



    class Meta:
        model=User
        fields=["username", "email"]
