from cProfile import label
from dataclasses import fields
from django import forms
from .models import Discussione

# Creo form per la discussione a partire dal modello
# Aggiungo il campo contenuto che servira a creare il primo post
# Con Meta aggiungo i campi da visualizare e cambio tipo i widgets
        
class DiscussioneModelForm(forms.ModelForm):
    contenuto = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Di cosa vuoi parlare?"
        }),
        max_length=4000,
        label="Primo messaggio"
    )

    class Meta:
        model = Discussione
        fields = ["titolo", "contenuto"]
        widget = {
            "titolo":forms.TextInput(attrs={"placeholder":"Titolo della discussione"})
        }