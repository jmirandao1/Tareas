
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render
from .models import Estudiante

from .forms import ClienteForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'


class CrearClienteView(CreateView):
    template_name= 'crear.html'
    form_class= ClienteForm   
    success_url= reverse_lazy('home:home')


class EstudianteView(TemplateView):
    template_name='estudiante.html'
class AdministradoresView(TemplateView):
    template_name='administradores.html'
class AcercaDeView(TemplateView):
    template_name='acercade.html'
class ListarEstudiante(ListView):
    template_name = 'listar_est.html'
    model = Estudiante

    def get_queryset(self):
        return Estudiante.objects.all()    