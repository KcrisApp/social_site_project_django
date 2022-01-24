from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Sezione
from .forms import DiscussioneModelForm
from .mixins import StafMixing
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
    context ={"sezione": sezione}
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
            return HttpResponseRedirect("/admin")
    else:
        form = DiscussioneModelForm()

    context = {"form": form, "sezione":sezione}
    return render(request, "forum/crea_discussione.html", context)

