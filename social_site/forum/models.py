from turtle import onclick, ondrag
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# Modello Sezioni che sara creato esclusivamente dagli amminstratori
class Sezione(models.Model):
    nome_sezione = models.CharField(max_length=80)
    descrizione = models.CharField(max_length=150, blank=True, null=True)
    logo_sezione = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_sezione

    def get_absolute_url(self):
        return reverse("sezione_view", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"

# Models per le discussioni
class Discussione(models.Model):
    titolo = models.CharField(max_length=120)
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_discussione = models.ForeignKey(User, on_delete=models.CASCADE)
    sezione_appartenenza = models.ForeignKey(Sezione, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo
    
    
    
    class Meta:
        verbose_name = "Discussione"
        verbose_name_plural= "Discussioni"


#model per i post
class Post(models.Model):
    autore_post = models.ForeignKey(User,on_delete=models.CASCADE, related_name="post")

    contenuto =models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    discussione = models.ForeignKey(Discussione, on_delete=models.CASCADE)

    def __str__(self):
        return self.autore_post.username
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"