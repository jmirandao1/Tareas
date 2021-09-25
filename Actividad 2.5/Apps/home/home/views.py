from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Estudiante
# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

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