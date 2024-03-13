from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
# MIXIN SE PONE EN LAS CLASES QUE QUIERO FILTRAR SI NO SE ESTA
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "ComicsIO/index.html")


def Tupost(request):
    return render(request, "ComicsIO/Tupost.html")

def Opinion(request):
    return render(request, "ComicsIO/Opinion.html")

def BuscarComic(request):
    return render(request, "ComicsIO/BuscarComic.html")

#crear entrada y html por cada uno de mis modelos

#___________________MIS FUNCIONES

class ComicCreate(CreateView):
    model = Comic
    fields = ["comic", "precio", "FechaDePublicacion"]
    success_url = reverse_lazy("home")

class PostCreate(CreateView):
    model = el_post
    fields = ["Titulo", "Texto", "fechaCreacion"]
    success_url = reverse_lazy("home")

class OpinaCreate(CreateView):
    model = OpinionDelComic
    fields = ["nombreDelcomic", "autor", "La_opinion"]
    success_url = reverse_lazy("miopinion")


class BuscarCreate(CreateView):
    model = BuscarComic
    fields = ["nombreDelcomic", "autor", "La_opinion"]
    success_url = reverse_lazy("miopinion")

#________ Login, Logout, Authentication, Registration
    
def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "ComicsIO/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AuthenticationForm()

    return render(request, "ComicsIO/login.html", {"form": miForm} )

def RegisterOne(request):         
    if request.method == "POST":
        elForm = RegistroForm(request.POST)
        if elForm.is_valid():
            usuario = elForm.cleaned_data.get("username")
            elForm.save()
            return redirect(reverse_lazy('register'))
    else:
    # __ Si ingresa en el else es la primera vez 
        elForm = AuthenticationForm()

    return render(request, "ComicsIO/login.html", {"form": elForm} )