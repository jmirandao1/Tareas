"""Home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
"from django.views.generic.base import View"
"from Apps.home.views import Estudiante"
from django.urls import path, include
from .views import CrearClienteView, HomeView, EstudianteView, AdministradoresView, AcercaDeView,ListarEstudiante
app_name='home'
urlpatterns = [
    path('index/', HomeView.as_view(), name='home'),
   
    path('crear/', CrearClienteView.as_view(), name='crear'),

    path('estudiantes/', EstudianteView.as_view(), name='estudiantes'),
    path('administradores/', AdministradoresView.as_view(), name='administradores'),
    path('acercade/',AcercaDeView.as_view(), name='acercade'),
    path('listest/',ListarEstudiante.as_view(), name='listar_est'),

]
