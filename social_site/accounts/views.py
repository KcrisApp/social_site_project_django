from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.forms import FormRegistrazione

# Create your views here.
# View per la registrazione di un nuovo utente
def registrazione_view(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            User.objects.create(username=username, password=password, email=email)

            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = FormRegistrazione()
        context = {"form":form}
        return render(request, "accounts/registrazione.html", context)
