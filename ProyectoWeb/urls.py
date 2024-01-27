"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppHealthy.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="Home"), 
    path("login", inicio_sesion, name="InicioSesion"),
    path("editarusuario", editar_perfil, name="EditarPerfil"),
    path("listafrutos/", ListaFrutos.as_view(), name="ListaFrutos"),
    path("listasemillas/", ListaSemillas.as_view(), name="ListaSemillas"),
    path("listaespecias/", ListaEspecias.as_view(), name="ListaEspecias"),
    path("crearfrutos", CrearFrutos.as_view(), name="CrearFrutos"),
    path("crearsemilla", CrearSemillas.as_view(), name="CrearSemillas"),
    path("crearespecias", CrearEspecias.as_view(), name="CrearEspecias"),
    path("actualizafruto/<int:pk>", ActualizaFrutos.as_view(), name="ActualizaFruto"),
    path("actualizasemilla/<int:pk>", ActualizaSemillas.as_view(), name="ActualizaSemilla"),
    path("actualizaespecia/<int:pk>", ActualizaEspecias.as_view(), name="ActualizaEspecia"),
    path("borrarfruto/<int:pk>", BorrarFrutos.as_view(), name="BorrarFruto"),
    path("borrarsemilla/<int:pk>", BorrarSemillas.as_view(), name="BorrarSemilla"),
    path("borrarespecia/<int:pk>", BorrarEspecias.as_view(), name="BorrarEspecia"),
    path("signup/", registro, name="Registrarse"),
    path("logout/", cerrar_sesion, name="CerrarSesion"),
    path("agregar/", agregarAvatar, name="Avatar1"),
    path("aboutme/", acerca, name="Acerca"),
    
    #URL para buscar datos
    path("buscarfrutoseco/", busqueda_frutoseco, name="BuscaFruto"),
    path("buscarsemilla/", busqueda_semilla, name="BuscaSemilla"),
    path("buscarespecia", busqueda_especia, name="BuscaEspecia"),
    path("resultadofrutos/", resultado_buscarfrutoseco),
    path("resultadosemilla/", resultado_buscarsemilla),
    path("resultadoespecias/", resultado_buscarespecia),

    ]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)