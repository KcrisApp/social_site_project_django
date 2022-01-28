from audioop import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .models import Discussione, Post, Sezione
from .forms import DiscussioneModelForm, PostModelForm
from .mixins import StafMixing
from django.urls import reverse

# Create your views here.

# Creo una nuova sezione usando le generic View
class CreaSezione(StafMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url ="/"
    
# View per la visualizzazione delle sezioni
def visualizza_sezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    discussione_sezione = Discussione.objects.filter(sezione_appartenenza=sezione).order_by("-data_creazione")
    context ={"sezione": sezione, "discussioni": discussione_sezione}
    return render(request, "forum/singola_sezione.html", context)

# View per creare una discussione
# la view deve prender i dati della sezione in quanto una discussione e legata ad una sezione
# se il metodo della richiesta e post allore prendo i dati dal form ma non li salvo subito
# inserisco la sezione di appartenenza l'utente che l'ha creata e salvo
# devo poi creare un post prendendo dal form il contenuto, discussione e autore da request
#se tutto e andato a buon fine faccio la ridirect
# Soloun utente loggato puo creare una discussione, uso il decoratore login_require che fa ridirect a login in caso l'utente non sia loggato 

@login_required
def crea_discussione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)

    if request.method == "POST":
        form = DiscussioneModelForm(request.POST)

        if form.is_valid():
            discussione = form.save(commit=False)
            discussione.sezione_appartenenza = sezione
            discussione.autore_discussione = request.user
            discussione.save()

            primo_post = Post.objects.create(discussione=discussione, autore_post=request.user, contenuto = form.cleaned_data['contenuto'])
            return HttpResponseRedirect(discussione.get_absolute_url())
    else:
        form = DiscussioneModelForm()

    context = {"form": form, "sezione":sezione}
    return render(request, "forum/crea_discussione.html", context)

def visualizza_discussione(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    posts_discussione = Post.objects.filter(discussione=discussione)
    form_risposta = PostModelForm()
    context = {'discussione': discussione, 'post_discussione': posts_discussione, 'form_risposta':form_risposta}
    
    return render(request,"forum/singola_discussione.html", context)

@login_required
def aggiungi_risposta(request, pk):
    
    discussione = get_object_or_404(Discussione, pk=pk)
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.discussione = discussione
            form.instance.autore_post = request.user
            form.save()

            url_discussione = reverse("singola_discussione", kwargs={"pk": pk})
            return HttpResponseRedirect(url_discussione)
    else:
        return HttpResponseBadRequest()
    
