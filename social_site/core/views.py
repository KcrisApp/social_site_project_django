from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from forum.models import Discussione, Sezione, Post
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# def homepage(request):
#     return render(request, 'core/homepage.html')
# Con le generic listView creo una funzione che prende tutte le sezioni dal db e ritorna una lista in home
class HomeView(ListView):
    queryset  = Sezione.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = "lista_sezioni"


#view per la gestione degli utenti
# LoginRequiredMixin per far si che solo un utente loggato possa vedere la lista
#  utenti
class UserListView(LoginRequiredMixin,ListView):
    model = User
    template_name = "core/users.html"

#view per la gestione del profilo
def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    discussioni_utente = Discussione.objects.filter(autore_discussione=user).order_by("-pk")
    context = {"user": user, "discussioni_utente":discussioni_utente}
    return render(request, "core/user_profile.html", context)


#funzione cerca
def cerca(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        print(querystring)
        if len(querystring) == 0:
            return redirect("/cerca/")
        discussioni = Discussione.objects.filter(titolo__icontains=querystring)
        posts = Post.objects.filter(contenuto__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        context = {'discussioni': discussioni, 'posts': posts, 'users':users}

        return render(request, 'core/cerca.html', context)
    else:
        return render(request,'core/cerca.html')


