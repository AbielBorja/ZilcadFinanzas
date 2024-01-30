from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .controler import dataTableFinanzas
from .models import IntervaloTiempo
from .forms import EditarIntervaloTiempoForm, CrearIntervaloTiempoForm
from datetime import datetime, timedelta, time
from django.contrib import messages
from rest_framework import generics
from .models import IntervaloTiempo
from .serializers import IntervaloTiempoSerializer
from django.views.decorators.http import require_GET

def finanzas(request):
    data = dataTableFinanzas(request)
    # Transforma las claves con espacios en claves con guiones bajos
    
    intervalos_tiempo = IntervaloTiempo.objects.all()            

    return render(request, 'finanzas.html', {'intervalos_tiempo': intervalos_tiempo})
    return render(request, 'finanzas.html', {'data': data, 'intervalos_tiempo': intervalos_tiempo, 'crear_form': crear_form, 'editar_form': editar_form})

@require_GET
def verificar_superposicion(request, intervalo_id):
    try:
        hora_inicio_milisegundos = int(request.GET.get('hora_inicio'))
        hora_fin_milisegundos = int(request.GET.get('hora_fin'))

        # Convertir milisegundos a timedelta
        hora_inicio = timedelta(seconds=hora_inicio_milisegundos / 1000)
        hora_fin = timedelta(seconds=hora_fin_milisegundos / 1000)

        # Crear objetos de tiempo para hora_inicio y hora_fin
        hora_inicio_obj = time(hour=hora_inicio.seconds // 3600, minute=(hora_inicio.seconds // 60) % 60)
        hora_fin_obj = time(hour=hora_fin.seconds // 3600, minute=(hora_fin.seconds // 60) % 60)

        # Obtener el intervalo existente para comparar
        intervalo_existente = IntervaloTiempo.objects.exclude(id=intervalo_id).filter(
            hora_inicio__lt=hora_fin_obj,
            hora_fin__gt=hora_inicio_obj
        )

        superpuesto = intervalo_existente.exists()

        return JsonResponse({'superpuesto': superpuesto})

    except ValueError:
        # Manejar errores de conversión de tipo de datos
        return JsonResponse({'error': 'Invalid input data'})
    

@require_GET
def verificar_superposicion_crear(request):
    try:
        hora_inicio_milisegundos = int(request.GET.get('hora_inicio'))
        hora_fin_milisegundos = int(request.GET.get('hora_fin'))

        # Convertir milisegundos a timedelta
        hora_inicio = timedelta(seconds=hora_inicio_milisegundos / 1000)
        hora_fin = timedelta(seconds=hora_fin_milisegundos / 1000)

        # Crear objetos de tiempo para hora_inicio y hora_fin
        hora_inicio_obj = time(hour=hora_inicio.seconds // 3600, minute=(hora_inicio.seconds // 60) % 60)
        hora_fin_obj = time(hour=hora_fin.seconds // 3600, minute=(hora_fin.seconds // 60) % 60)

        # Obtener todos los intervalos existentes para comparar
        todos_los_intervalos = IntervaloTiempo.objects.all()
        superpuesto = any(
            intervalo.hora_inicio < hora_fin_obj < intervalo.hora_fin or
            intervalo.hora_inicio < hora_inicio_obj < intervalo.hora_fin
            for intervalo in todos_los_intervalos
        )

        return JsonResponse({'superpuesto': superpuesto})

    except ValueError:
        # Manejar errores de conversión de tipo de datos
        return JsonResponse({'error': 'Invalid input data'})



class IntervaloTiempoList(generics.ListCreateAPIView):
    queryset = IntervaloTiempo.objects.all()
    serializer_class = IntervaloTiempoSerializer

class IntervaloTiempoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IntervaloTiempo.objects.all()
    serializer_class = IntervaloTiempoSerializer

def light(request):
    return render(request, 'layout-sidenav-light.html')

def charts(request):
    return render(request, 'charts.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def error_401 (request):
    return render(request, '401.html')

def error_404 (request, exception):
    return render(request, '404.html', status=404)

def error_500 (request):
    return render(request, '500.html')

def tables (request):
    return render(request, 'tables.html')

def layout (request):
    return render(request, 'layout-static.html')

def password (request):
    return render(request, 'password.html')

def index(request):
    return redirect('/finanzas')