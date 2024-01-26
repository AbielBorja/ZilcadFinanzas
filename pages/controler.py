import json
from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime



def dataTableFinanzas(request):
    with open('pages\static\BaseGeneral.json', encoding='utf-8-sig') as d:
        data = json.load(d)

    for item in data:
        item.update({key.replace(' ', '_'): value for key, value in item.items()})
        item['Costo_servicio'] = calcular_costo_servicio(item['HORA_FRENTE_EQUIPOS'], item['HORA_DE_SALIDA'])

    return data
    # return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False},)

def calcular_costo_servicio(hora_frente_equipos, hora_de_salida):
    # Verifica si las horas son vacías
    if not hora_frente_equipos or not hora_de_salida:
        return 0  # O devuelve el valor que desees para estos casos
    
    try:
        # Calcula la diferencia en horas
        hora_frente_equipos = datetime.strptime(hora_frente_equipos, "%H:%M:%S")
        hora_de_salida = datetime.strptime(hora_de_salida, "%H:%M:%S")
        diferencia_horas = (hora_de_salida - hora_frente_equipos).seconds / 3600

        # Define los umbrales de costo de servicio
        umbral_1 = 6
        umbral_2 = 10

        # Asigna el costo de servicio según la duración
        if diferencia_horas <= umbral_1:
            return 550
        elif umbral_1 < diferencia_horas <= umbral_2:
            return 1100
        else:
            return 1375
    except ValueError:
        return 0  # O devuelve el valor que desees en caso de error en el formato de hora