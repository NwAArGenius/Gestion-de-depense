from django import forms
from .models import Depense
from .models import Revenue

class DespenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['name', 'montant', 'categorie', 'user']
        widgets = {
            'user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la dépense'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant de la dépense'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
        }


class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ['name', 'montant', 'categorie', 'user']
        widgets = {
            'user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la Revenue' }),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant de la Revenue'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
        }

        