from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Discussione, Post, Sezione
from .forms import DiscussioneModelForm
from .mixins import StafMixing
# Create your views here.


class CreaSezione(StafMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url ="/"
    
# Aggiungere comment
def visualizza_sezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    context ={"sezione": sezione}
    return render(request, "forum/singola_sezione.html", context)

# Aggiungere commento
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

def visualizza_discussione(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    post_discussione = Post.objects.filter(discussione=discussione)
    context = {'discussione': discussione, 'post_discussione': post_discussione}
    