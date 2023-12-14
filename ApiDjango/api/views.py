from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render


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
    
