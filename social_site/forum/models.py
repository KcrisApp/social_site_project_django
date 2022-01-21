from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modello Sezioni che sara creato esclusivamente dagli amminstratori
class Sezione(models.Model):
    nome_sezione = models.CharField(max_length=80)
    descrizione = models.CharField(max_length=150, blank=True, null=True)
    logo_sezione = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_sezione
    
    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"