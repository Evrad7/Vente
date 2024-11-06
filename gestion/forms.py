from django import forms
from .models import Article

class ArticleAdminForm(forms.ModelForm):

    class Meta:
        model=Article
        fields='__all__'
        widgets={
        "prix": forms.NumberInput(attrs={"min":0, "step":500}),
        "reduction":forms.NumberInput(attrs={"max":100})
        }
