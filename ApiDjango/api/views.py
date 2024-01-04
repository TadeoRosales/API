from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import Registro_Cliente
from .models import RegistroCliente
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login

# Create your views here.

class Home (APIView):
    template_name = 'index.html'
    def get(self, request):
        return render(request,self.template_name)
    
class LoginE (APIView):
    template_name = 'Login_Empleado.html'
    def get(self, request):
        return render(request,self.template_name)
    
class LoginC (APIView):
    template_name = 'Login_Cliente.html'
    def get(self, request):
        return render(request,self.template_name)

class Registro (APIView):
    template_name = 'Registro.html'
    def get(self, request):
        return render(request,self.template_name)
    
class Problema (APIView):
    template_name = 'Problema.html'
    def get(self, request):
        return render(request,self.template_name)
    
    
    #Manejo de Formulario de registro de clientes 
class Registro_ClienteView(APIView):
    template_name = 'Registro.html'
    
    def post(self, request):
        form = Registro_Cliente(request.POST)
        if form.is_valid():
            Registro = form.save()

            #Mandar correo
            subject = 'Confirmacion de Registro'
            message = 'Gracias por ser cliente de Brokmake'
            message += f'\nNombre: {Registro.Nombre}'
            message += f'\nContraseña: {Registro.password}'
            message += f'\nCorreo: {Registro.Correo}'

            from_email = settings.EMAIL_HOST_USER
            recipient_list = [Registro.Correo] #Usar el correo del usuario

            #Enviar correo
            send_mail(
                subject, message, from_email, recipient_list,
                fail_silently=False,
            )

        return redirect('Login_Cliente')
        return render(request, self.template_name, {'form': form})
    

class LoginView(APIView):
    template_name = 'Login_Cliente.html' #Plantilla de inicio de sesion
   
    def get (self,request):
     return render (request, self.template_name)
   
    def post (self, request):
     Correo = request.POST.get('Correo')
     password = request.POST.get('password')
     
     #consulta a los usuarios ingresados en la base de datos
     try:
        Registro_c=RegistroCliente.objects.get(Correo=Correo, password=password)
     except RegistroCliente.DoesNotExist:
        Registro_c=None

     if Registro_c is not None:
        return redirect('Problema.html')
     else:
        return render(request,self.template_name,{'error_message':'Datos invalidos Intentalo nuevamente'})