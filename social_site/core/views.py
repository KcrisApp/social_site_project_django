from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.list import ListView
# Create your views here.
def homepage(request):
    return render(request, 'core/homepage.html')

#view per la gestione del profilo
def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    context = {"user": user}
    return render(request, "core/user_profile.html", context)

#view per la gestione degli utenti

class UserListView(ListView):
    model = User
    template_name = "core/users.html"


