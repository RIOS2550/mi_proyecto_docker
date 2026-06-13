from django.shortcuts import render
from .models import Mascota

def lista_mascotas(request):
    todas_las_mascotas = Mascota.objects.all().order_by('-fecha_registro')

    contexto = {
        'mascotas': todas_las_mascotas
    }

    return render(request, 'mascotas/lista_mascotas.html', contexto)