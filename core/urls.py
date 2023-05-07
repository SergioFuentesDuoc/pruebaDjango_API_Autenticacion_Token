from django.contrib import admin
from django.urls import path, include
from .views import home,borgona,batman, listado, listar_razas, registrar_mascota, eliminar_mascota, modificar_mascota, modificar

urlpatterns = [
    path('', home, name="home"),
    path('borgona',borgona,name="borgona"),
    path('batman', batman, name="batman"),
    path('listado',listado,name="listado"),
    path('formulario', listar_razas, name="formulario"),
    path('registro', registrar_mascota, name="registro"),
    path('eliminar/<int:id>',eliminar_mascota, name="eliminar_mascota"),
    path('modificar_mascota/<int:id>', modificar_mascota, name="modificar_mascota"),
    path('modificar', modificar, name="modificar"),
]