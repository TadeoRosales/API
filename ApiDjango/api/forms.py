from django import forms
from .models import RegistroCliente

class Registro_Cliente(forms.ModelForm):
    class Meta:
        model = RegistroCliente
        fields = ['Nombre','Apellidos','Usuario','password','Correo','CP','Telefono','Direccion']
