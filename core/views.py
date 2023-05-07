from django.shortcuts import render, redirect
from .models import Mascota, Raza
from django.contrib import messages
# Create your views here.
def home(request):
    lista = ["Borgoña","Batman","Completo"]
    contexto = {"mascotas": lista}
    return render(request,'core/home.html',contexto)

def borgona(request):
    contexto = {"nombreMascota": "*Borgoña*","Edad":"3 años"}
    return render(request,'core/borgona.html',contexto)

def batman(request):
    contexto = {"nombreMascota": "Batman","Edad": "2 años"}
    return render(request,'core/batman.html',contexto)

def listado(request):
    mascotas = Mascota.objects.all() #generando un select * from de la tabla mascota
    contexto = {"mascota":mascotas}
    return render(request,'core/ListadoMascotas.html',contexto)

def listar_razas(request):
    razas = Raza.objects.all() #me trae todos los registros de esa tabla (select * from)
    contexto = {"raza_m":razas}
    return render(request,'core/formulario.html',contexto)

def registrar_mascota(request):
    chip_m = request.POST['chip']
    nombre_m = request.POST['nombre']
    edad_m = request.POST['edad']
    raza_m = request.POST['raza']
    img_foto = request.FILES['foto_m']
    #obtener el registro completo de la raza
    raza_c = Raza.objects.get(codigo = raza_m)

    #insert
    Mascota.objects.create(codigoChip = chip_m, nombreMascota = nombre_m, edadMascota = edad_m, foto = img_foto , raza = raza_c) 

    messages.success(request,'Mascota Registrada')

    return redirect('formulario')

def eliminar_mascota(request, id):
    mascota1 = Mascota.objects.get(codigoChip = id)
    mascota1.delete() #elimina el registro
    messages.success(request,'Mascota Eliminada')

    return redirect('listado')


def modificar_mascota(request, id):
    mascota1 = Mascota.objects.get(codigoChip = id) # obtengo los datos de la mascota
    raza1 = Raza.objects.all() #obtener todas las razas para llenar el combobox

    contexto = {
        "mascota" : mascota1,
        "razas" : raza1
    }

    return render(request,'core/modificar_mascota.html',contexto)

def modificar(request):
    chip = request.POST['chip']
    nombre_m = request.POST['nombre']
    edad_m = request.POST['edad']
    raza_m = request.POST['raza']

    mascota = Mascota.objects.get(codigoChip = chip) #el registro original
    #comienzo a reemplazar los valores en ese registro original
    mascota.nombreMascota = nombre_m
    mascota.edadMascota = edad_m

    raza_m2 = Raza.objects.get(codigo = raza_m)

    mascota.raza = raza_m2
    mascota.save() #update

    messages.success(request, 'Mascota Modificada')
    return redirect('listado')

    



