from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .controler import dataTableFinanzas
from .models import IntervaloTiempo
from .forms import EditarIntervaloTiempoForm, CrearIntervaloTiempoForm
from datetime import timedelta

def finanzas(request):
    data = dataTableFinanzas(request)
    # Transforma las claves con espacios en claves con guiones bajos
    
    intervalos_tiempo = IntervaloTiempo.objects.all()
    crear_form = CrearIntervaloTiempoForm()
    editar_form = EditarIntervaloTiempoForm()

    # Lógica para manejar la edición de intervalo de tiempo
    if request.method == 'POST':
        print("Entre aqui 1")
        if 'editar_intervalo_id' in request.POST:
            intervalo_id = request.POST['editar_intervalo_id']
            intervalo_editar = IntervaloTiempo.objects.get(id=intervalo_id)
            editar_form = EditarIntervaloTiempoForm(request.POST, instance=intervalo_editar)
            if editar_form.is_valid():
                editar_form.save()
        else:
            print("Entre aqui 2")
            print(request.POST)

            # Guardar datos sin pasar por el formulario
            hora_inicio_milisegundos = int(request.POST['hora_inicio'])
            hora_fin_milisegundos = int(request.POST['hora_fin'])
            costo_servicio = float(request.POST['costo_servicio'])

            # Validar manualmente
            if hora_inicio_milisegundos >= hora_fin_milisegundos:
                # Limpiar los errores previos de ese campo
                crear_form.fields['hora_inicio'].error_messages = {'invalid': None}
                # Agregar el nuevo error
                crear_form.add_error('hora_inicio', 'La hora de inicio debe ser menor que la hora de fin.')
            else:
                # Convertir milisegundos a segundos y luego a timedelta
                hora_inicio = timedelta(seconds=hora_inicio_milisegundos / 1000)
                hora_fin = timedelta(seconds=hora_fin_milisegundos / 1000)

                # Crear y guardar el objeto IntervaloTiempo
                intervalo_tiempo = IntervaloTiempo(
                    hora_inicio=hora_inicio,
                    hora_fin=hora_fin,
                    costo_servicio=costo_servicio
                )
                intervalo_tiempo.save()



    return render(request, 'finanzas.html', {'intervalos_tiempo': intervalos_tiempo, 'crear_form': crear_form, 'editar_form': editar_form})
    return render(request, 'finanzas.html', {'data': data, 'intervalos_tiempo': intervalos_tiempo, 'crear_form': crear_form, 'editar_form': editar_form})


def editar_intervalo_tiempo(request, pk):
    intervalo = get_object_or_404(IntervaloTiempo, pk=pk)

    if request.method == 'POST':
        form = EditarIntervaloTiempoForm(request.POST, instance=intervalo)
        if form.is_valid():
            nuevo_intervalo = form.save(commit=False)

            # Verifica que el nuevo intervalo no se superponga con otros
            superpuestos = IntervaloTiempo.objects.filter(
                hora_inicio__lt=nuevo_intervalo.hora_fin,
                hora_fin__gt=nuevo_intervalo.hora_inicio
            ).exclude(pk=nuevo_intervalo.pk)

            if not superpuestos.exists():
                nuevo_intervalo.save()
                return redirect('tu_vista_de_intervalos')  # Reemplaza con la vista donde se muestran los intervalos
            else:
                form.add_error(None, 'El intervalo se superpone con otro existente.')

    else:
        form = EditarIntervaloTiempoForm(instance=intervalo)

    return render(request, 'tu_template_de_edicion.html', {'form': form})

def crear_intervalo_tiempo(request):
    if request.method == 'POST':
        form = CrearIntervaloTiempoForm(request.POST)
        if form.is_valid():
            nuevo_intervalo = form.save(commit=False)

            # Verifica que el nuevo intervalo no se superponga con otros
            superpuestos = IntervaloTiempo.objects.filter(
                hora_inicio__lt=nuevo_intervalo.hora_fin,
                hora_fin__gt=nuevo_intervalo.hora_inicio
            )

            if not superpuestos.exists():
                nuevo_intervalo.usuario = request.user
                nuevo_intervalo.save()
                return redirect('tu_vista_de_intervalos')  # Reemplaza con la vista donde se muestran los intervalos
            else:
                form.add_error(None, 'El intervalo se superpone con otro existente.')

    else:
        form = CrearIntervaloTiempoForm()

    return render(request, 'tu_template_de_creacion.html', {'form': form})


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

def error_404 (request):
    return render(request, '404.html')

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