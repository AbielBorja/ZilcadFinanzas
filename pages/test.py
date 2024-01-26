import json
from pprint import pprint

with open('ZilcadFinanzas\pages\static\BaseGeneral.json', encoding='utf-8-sig') as d:
    data = json.load(d)

# Lista para almacenar los elementos con campos seleccionados
json_modificado = []

# Iterar sobre cada elemento en el JSON original
for elemento in data:
    # Crear un nuevo diccionario con los campos seleccionados
    elemento_modificado = {
        "tipo": elemento.get("TIPO", ""),
        "folio": elemento.get("FOLIO", ""),
        "fecha_de_atencion": elemento.get("FECHA DE ATENCION", ""),
        "cliente": elemento.get("CLIENTE", ""),
        "sitio": elemento.get("SITIO", ""),
        "site_id_telmex": elemento.get("SITE ID TELMEX", ""),
        "ciudad": elemento.get("CIUDAD", ""),
        "estado": elemento.get("ESTADO", ""),
        "proveedor_IDC": elemento.get("PROVEEDOR IDC's", ""),
        "coordinador_IDC": elemento.get("COORDINADOR IDC", ""),
        "hora_llegada_a_sitio": elemento.get("HORA LLEGADA A SITIO", ""),
        "hora_de_ingreso_a_sucursal": elemento.get("HORA DE INGRESO A SUCURSAL", ""),
        "hora_frente_equipo": elemento.get("HORA FRENTE EQUIPOS", ""),
        "hora_de_salida": elemento.get("HORA DE SALIDA", ""),
        "tiempo_en_sitio": elemento.get("TIEMPO EN SITIO", ""),
        "status": elemento.get("STATUS", ""),
        "costo_servicio": elemento.get("Costo servicio", ""),
        "costo_recoleccion": elemento.get("Costo recoleccion", ""),
        "retiro": elemento.get("Retiro", ""),
        "viaticos": elemento.get("VIATICOS", ""),
        "costo_herramienta": elemento.get("Costo herramienta", ""),
        "total": elemento.get("TOTAL", ""),
        "servicio_pagado": elemento.get("SERVICIO PAGADO", ""),
        "viatico_pagado": elemento.get("VIATICO PAGADO", ""),
        "recoleccion_pagada": elemento.get("RECOLECCION PAGADA", ""),
        "herramienta": elemento.get("HERRAMIENTA", ""),
        "total_pagado": elemento.get("TOTAL PAGADO", ""),
        "penalizacion": elemento.get("PENALIZACION", ""),
        "observaciones": elemento.get("OBSERVACIONES", ""),
        "cuenta_por_pagar": elemento.get("POR PAGAR", "")
    }

    # Agregar el nuevo elemento a la lista
    json_modificado.append(elemento_modificado)

# Imprimir el nuevo JSON
print(json.dumps(json_modificado, indent=2))