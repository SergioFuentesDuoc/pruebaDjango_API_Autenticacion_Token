from django.urls import path
from rest_api.views import lista_mascotas,vista_mascota_mod
from rest_api.viewsLogin import login

urlpatterns =[
    path('lista_mascotas/',lista_mascotas,name="lista_mascotas"),
    path('datos_mascota/<id>',vista_mascota_mod,name="modif_mascota"),
    path('login/',login,name="login"),
]