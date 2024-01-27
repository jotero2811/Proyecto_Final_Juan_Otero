from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from AppHealthy.models import Frutosecos, Semillas, Especias
from AppHealthy.forms import FrutosecoFormulario, SemillaFormulario, EspeciaFormulario, RegistrarUsuario
from AppHealthy.forms import EditarUsuario, AvatarFormulario
from AppHealthy.views import *
from django.contrib.auth.models import User
from AppHealthy.models import Avatar


# Create your views here.


def inicio(request):
    
    return render(request, "AppHealthy/inicio.html")

def acerca(request):
    
    return render(request, "AppHealthy/about_me.html")

#vistas de register/login/logout

def inicio_sesion(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            usuario = info["username"]
            contra = info["password"]

            usuario_actual = authenticate(username=usuario, password=contra)

            if usuario_actual is not None:
                login(request, usuario_actual)

                return render(request, "AppHealthy/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
        else:

            return render(request, "AppHealthy/inicio.html", {"mensaje":f"Error, datos incorrectos"})
    else:

        formulario = AuthenticationForm()

    return render(request, "registro/inicio_sesion.html", {"formu":formulario})

def registro(request):

    if request.method == "POST":
        
        formulario = RegistrarUsuario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario = info["first_name"]

            formulario.save()

            return render(request, "AppHealthy/inicio.html", {"mensaje":f"Usuario creado : {usuario}"})
    
    else:

        formulario = RegistrarUsuario()

    return render(request, "registro/registrar_usuario.html", {"formu":formulario})

def editar_perfil(request):
    
    usuario_actual = request.user

    if request.method == "POST":
    
        formulario = EditarUsuario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario_actual.first_name = info["first_name"]
            usuario_actual.last_name = info["last_name"]
            usuario_actual.email = info["email"]

            usuario_actual.set_password(info["password1"])


            usuario_actual.save()

            return render(request, "AppHealthy/inicio.html")
        
    else:
        formulario = EditarUsuario(initial={"first_name":usuario_actual.first_name,
                                                "last_name":usuario_actual.last_name,
                                                "email":usuario_actual.email,})
        
    return render(request, "registro/editar_usuario.html", {"formu":formulario})


def cerrar_sesion(request):
        
    logout(request)

    return render(request, "registro/cerrar_sesion.html")

    
def busqueda_frutoseco(request):

    return render(request, "AppHealthy/busqueda_frutoseco.html")

def resultado_buscarfrutoseco(request):

    if request.method == "GET":

        nombre_buscado = request.GET["buscafruto"]
        
        resultados_frutoseco = Frutosecos.objects.filter(nombre__icontains=nombre_buscado)
    
        return render(request, "AppHealthy/busqueda_frutoseco.html", {"frutos":resultados_frutoseco})

    else:
        return render(request, "AppHealthy/busqueda_frutoseco.html")
    

def busqueda_semilla(request):

    return render(request, "AppHealthy/busqueda_semilla.html")

def resultado_buscarsemilla(request):

    if request.method == "GET":

        nombre_buscado = request.GET["buscasemilla"]
        
        resultados_semillas = Semillas.objects.filter(nombre__icontains=nombre_buscado)
    
        return render(request, "AppHealthy/busqueda_semilla.html", {"semilla": resultados_semillas})

    else:
        return render(request, "AppHealthy/busqueda_semilla.html")

def busqueda_especia(request):

    return render(request, "AppHealthy/busqueda_especias.html")

def resultado_buscarespecia(request):

    if request.method == "GET":

        nombre_buscado = request.GET["buscaespecia"]
        
        resultados_especias = Especias.objects.filter(nombre__icontains=nombre_buscado)
    
        return render(request, "AppHealthy/busqueda_especias.html", {"especia": resultados_especias})

    else:
        return render(request, "AppHealthy/busqueda_especias.html")




#CRUD READ DE PELICULAS --- LISTVIEW --- Vistas basadas en clases

class ListaFrutos(LoginRequiredMixin, ListView):

    model = Frutosecos

class ListaSemillas(LoginRequiredMixin, ListView):

    model = Semillas

class ListaEspecias(LoginRequiredMixin, ListView):

    model = Especias

#CRUD CEATE DE PELICULAS --- CREATEVIEW ---

class CrearFrutos(CreateView):

    model = Frutosecos
    template_name = "AppHealthy/crear_frutos.html"
    fields = {"nombre","presentacion","precio"}
    success_url = "/listafrutos/"

class CrearSemillas(CreateView):

    model = Semillas
    template_name = "AppHealthy/crear_semillas.html"
    fields = {"nombre","presentacion","precio"}
    success_url = "/listasemillas/"

class CrearEspecias(CreateView):

    model = Especias
    template_name = "AppHealthy/crear_especias.html"
    fields = {"nombre","presentacion","precio"}
    success_url = "/listaespecias/"


#CRUD UPDATE DE PELICULAS --- UPDATEVIEW ---

class ActualizaFrutos(UpdateView):

    model = Frutosecos
    template_name = "AppHealthy/crear_frutos.html"
    fields = {"nombre","presentacion","precio"}
    success_url = "/listafrutos/"

class ActualizaSemillas(UpdateView):

    model = Semillas
    template_name = "AppHealthy/crear_semillas.html"
    fields = {"nombre","presentacion","precio"}
    success_url = "/listasemillas/"

class ActualizaEspecias(UpdateView):

    model = Especias
    
    template_name = "AppHealthy/crear_especias.html"
    fields = {"nombre","presentacion","precio"}
    success_url = "/listaespcias/"

#CRUD ELIMINAR PELICULAS --- DELETEVIEW ---

class BorrarFrutos(DeleteView):

    model = Frutosecos
    template_name = "AppHealthy/borrar_fruto.html"
    success_url = "/listafrutos"

class BorrarSemillas(DeleteView):

    model = Semillas
    template_name = "AppHealthy/borrar_semilla.html"
    success_url = "/listasemillas"

class BorrarEspecias(DeleteView):

    model = Especias
    template_name = "AppHealthy/borrar_especia.html"
    success_url = "/listaespecias"

@login_required
def agregarAvatar(request):

    if request.method=="POST":

        form = AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppHealthy/inicio.html")
    
    else:

        form = AvatarFormulario()
    
    return render(request, "AppHealthy/agregarAvatar.html", {"formulario":form})