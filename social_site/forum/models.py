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

    def get_last_discussions(self):
        return Discussione.objects.filter(sezione_appartenenza=self).order_by("-data_creazione")[:2]

    def get_number_of_posts_in_sections(self):
        return Post.objects.filter(discussione__sezione_appartenenza=self).count()

    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"

# Models per le discussioni
class Discussione(models.Model):
    titolo = models.CharField(max_length=120)
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_discussione = models.ForeignKey(User, on_delete=models.CASCADE,related_name="discussioni")
    sezione_appartenenza = models.ForeignKey(Sezione, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = "Discussione"
        verbose_name_plural= "Discussioni"
    
    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("singola_discussione", kwargs={"pk": self.pk})

   




#model per i post
class Post(models.Model):
    autore_post = models.ForeignKey(User,on_delete=models.CASCADE, related_name="posts")

    contenuto =models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    discussione = models.ForeignKey(Discussione, on_delete=models.CASCADE)

    def __str__(self):
        return self.autore_post.username
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"