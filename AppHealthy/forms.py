from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppHealthy.models import Avatar

class FrutosecoFormulario(forms.Form):
    nombre=forms.CharField()
    presentacion=forms.CharField()
    precio=forms.FloatField()
    
class SemillaFormulario(forms.Form):
    nombre=forms.CharField()
    presentacion=forms.CharField()
    precio=forms.FloatField()

class EspeciaFormulario(forms.Form):
    nombre=forms.CharField()
    presentacion=forms.CharField()
    precio=forms.FloatField()

class RegistrarUsuario(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Ingrese Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingrese Password", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingrese Nombre")
    last_name = forms.CharField(label="Ingrese Apellido")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]

class EditarUsuario(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Ingrese Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingrese Password", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingrese Nombre")
    last_name = forms.CharField(label="Ingrese Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = [ "imagen"]