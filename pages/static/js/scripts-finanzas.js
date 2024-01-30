// Función para convertir cadena de hora (HH:mm:ss) a milisegundos
function convertirHoraAMilisegundos(hora) {
    var partes = hora.split(':');
    var horas = parseInt(partes[0], 10) || 0;
    var minutos = parseInt(partes[1], 10) || 0;
    var segundos = parseInt(partes[2], 10) || 0;

    return horas * 3600000 + minutos * 60000 + segundos * 1000;
}

function convertirMilisegundosAHora(milisegundos) {
    // Si el valor es una cadena (formato de hora), devolverla tal cual
    if (typeof milisegundos === 'string' && milisegundos.includes(':')) {
        return milisegundos;
    }

    var horas = Math.floor(milisegundos / 3600000);
    var minutos = Math.floor((milisegundos % 3600000) / 60000);
    var segundos = Math.floor((milisegundos % 60000) / 1000);

    return `${String(horas).padStart(2, '0')}:${String(minutos).padStart(2, '0')}:${String(segundos).padStart(2, '0')}`;
}
var intervaloIdEnEdicion;

function manejarKendoTimeDurationPicker(id, valorInicial) {
    if ($("#" + id).data("kendoTimeDurationPicker")) {
        // Si ya existe una instancia, solo actualizamos su valor
        $("#" + id).data("kendoTimeDurationPicker").value(convertirHoraAMilisegundos(valorInicial));
    } else {
        // Si no existe, inicializamos una nueva instancia
        $("#" + id).kendoTimeDurationPicker({
            columns: [
                { name: "hours", format: "## Hora", min: 0, max: 24 },
                { name: "minutes", format: "## Minutos", min: 0, max: 50, step: 5 },
                { name: "seconds", format: "## Segundos", min: 0, max: 60, step: 1 }
            ],
            // Puedes ajustar los shortcuts según tus necesidades
            value: convertirHoraAMilisegundos(valorInicial)  // Convierte la cadena a milisegundos
        });
    }
}

function editarIntervalo(intervaloId) {
    // Hacer una solicitud AJAX para obtener los datos del intervalo
    $.ajax({
        url: `/api/intervalo-tiempo-detail/${intervaloId}/`,
        method: 'GET',
        success: function (data) {
            // Llenar el formulario con los datos recibidos
            $('#id_hora_inicio_edit').val(data.hora_inicio);
            $('#id_hora_fin_edit').val(data.hora_fin);
            $('#id_costo_servicio_edit').val(data.costo_servicio);

            console.log("Datos al momento de boton editar")
            console.log(data.hora_inicio)
            console.log(data.hora_fin)
            console.log(data.costo_servicio)

            // Abrir el modal de edición
            $('#modalEdit').modal('show');

            intervaloIdEnEdicion = intervaloId
            console.log(intervaloId);

            // Manejar kendoTimeDurationPicker para los campos de hora de inicio y fin
            manejarKendoTimeDurationPicker('id_hora_inicio_edit', data.hora_inicio);
            manejarKendoTimeDurationPicker('id_hora_fin_edit', data.hora_fin);

        },
        error: function (error) {
            console.error('Error al obtener datos del intervalo:', error);
        }
    });
}

function guardarEdicionIntervalo(intervaloId) {
    // Obtener los datos del formulario de edición
    var horaInicio = $('#id_hora_inicio_edit').val();
    var horaFin = $('#id_hora_fin_edit').val();
    var costoServicio = $('#id_costo_servicio_edit').val();

    // Convertir milisegundos a formato de hora
    var horaInicio = convertirMilisegundosAHora(horaInicio);
    var horaFin = convertirMilisegundosAHora(horaFin);

    console.log("Datos al momento de enviar")
    console.log(horaInicio)
    console.log(horaFin)

    // Crear un objeto con los datos del formulario
    var datosEdicion = {
        hora_inicio: horaInicio,
        hora_fin: horaFin,
        costo_servicio: costoServicio
    };

    if (intervaloIdEnEdicion !== undefined && intervaloIdEnEdicion !== null) {
        // Hacer lo que necesitas con intervaloIdEnEdicion
        console.log('ID del intervalo en edición:', intervaloIdEnEdicion);
        // Hacer una solicitud AJAX para actualizar el intervalo
        $.ajax({
            url: `/api/intervalo-tiempo-detail/${intervaloIdEnEdicion}/`,
            method: 'PUT',
            data: datosEdicion,
            success: function (data) {
                console.log('Intervalo actualizado con éxito:', data);

                // Cerrar todos los modales usando Bootstrap 5
                $('#modalEdit').modal('hide');
                $('#modalEdit2').modal('hide');

                // Obtener la referencia a la alerta de éxito
                var alertaExito = $('#mensajeExito');

                // Añadir clases de Bootstrap para la alerta de éxito
                alertaExito.addClass('alert-success');

                // Mostrar la alerta de éxito
                alertaExito.fadeIn().delay(2300).fadeOut();

                // Recargar la página después de 2.3 segundos
                setTimeout(function () {
                    location.reload();
                }, 2300);
            },
            error: function (error) {
                console.error('Error al actualizar el intervalo:', error);
            }
        });
    }
}
function eliminarIntervalo(intervaloId) {
    // Hacer la solicitud AJAX para eliminar el intervalo
    $.ajax({
        url: `/api/intervalo-tiempo-detail/${intervaloId}/`,
        method: 'DELETE',
        success: function (data) {
            // Obtener la referencia a la alerta de éxito
            var alertaExito = $('#mensajeBorrar');

            // Añadir clases de Bootstrap para la alerta de éxito
            alertaExito.addClass('alert-danger');

            // Mostrar la alerta de éxito
            alertaExito.fadeIn().delay(2300).fadeOut();

            // Cerrar el modal
            $('#modalBorrar').modal('hide');

            // Recargar la página después de 2.3 segundos
            setTimeout(function () {
                location.reload();
            }, 2300);
        },
        error: function (error) {
            console.error('Error al eliminar el intervalo:', error);
        }
    });
}

function verificarConfirmacionBaja(intervaloId) {
    // Verificar si la casilla de confirmación está marcada
    if ($('#confirmarBajaCheck').prop('checked')) {
        // Casilla de verificación marcada, proceder con la eliminación
        eliminarIntervalo(intervaloId);
    } else {
        // Obtener la referencia a la alerta de éxito
        var alertaExito = $('#mensajeCasilla');

        // Añadir clases de Bootstrap para la alerta de éxito
        alertaExito.addClass('alert-warning');

        // Mostrar la alerta de éxito
        alertaExito.fadeIn().delay(2000).fadeOut();
    }
}
function verificarSuperposicion(intervaloId) {
    // Convertir las horas a milisegundos si no están en ese formato
    var horaInicio = $('#id_hora_inicio_edit').val();
    var horaFin = $('#id_hora_fin_edit').val();

    horaInicio = (typeof horaInicio === 'string' && horaInicio.includes(':')) ? convertirHoraAMilisegundos(horaInicio) : horaInicio;
    horaFin = (typeof horaFin === 'string' && horaFin.includes(':')) ? convertirHoraAMilisegundos(horaFin) : horaFin;

    // Hacer una solicitud AJAX para verificar superposición
    $.ajax({
        url: `/api/intervalo-tiempo-superpuesto/${intervaloIdEnEdicion}/?hora_inicio=${horaInicio}&hora_fin=${horaFin}`,
        method: 'GET',
        success: function (data) {
            if (data.superpuesto) {
                // Mostrar un mensaje de error o tomar la acción que consideres apropiada
                // Obtener la referencia a la alerta de éxito
                var alerta = $('#mensajeSuperpone');

                // Añadir clases de Bootstrap para la alerta de éxito
                alerta.addClass('alert-warning');

                // Mostrar la alerta de éxito
                alerta.fadeIn().delay(2000).fadeOut();
                console.error('Error: El intervalo se superpone con otro existente.');
            } else {
                // Proceder con la solicitud de creación o edición
                guardarEdicionIntervalo();
            }
        },
        error: function (error) {
            console.error('Error al verificar superposición edición:', error);
        }
    });
}

function verificarSuperposicionCreacion() {
    // Lógica para verificar superposiciones con AJAX
    // Ejemplo de datos a enviar al servidor, puedes ajustar según tus necesidades
    var horaInicio = $('#id_hora_inicio_add').val();
    var horaFin = $('#id_hora_fin_add').val();

    horaInicio = (typeof horaInicio === 'string' && horaInicio.includes(':')) ? convertirHoraAMilisegundos(horaInicio) : horaInicio;
    horaFin = (typeof horaFin === 'string' && horaFin.includes(':')) ? convertirHoraAMilisegundos(horaFin) : horaFin;


    console.log("Momentos antes de creación")
    console.log(horaInicio)
    console.log(horaFin)

    $.ajax({
        url: `api/intervalo-tiempo-superpuesto_crear/?hora_inicio=${horaInicio}&hora_fin=${horaFin}`,
        method: 'GET',
        success: function (data) {
            if (!data.superpuesto) {
                // Si no hay superposiciones, procede a la creación del intervalo
                crearIntervalo();
            } else {
                // Mostrar un mensaje de error o tomar la acción que consideres apropiada
                // Obtener la referencia a la alerta de éxito
                var alerta = $('#mensajeSuperpone');

                // Añadir clases de Bootstrap para la alerta de éxito
                alerta.addClass('alert-warning');

                // Mostrar la alerta de éxito
                alerta.fadeIn().delay(2000).fadeOut();
                console.error('Error: El intervalo se superpone con otro existente.');

            }
        },
        error: function (error) {
            console.error('Error al verificar superposición Creacion:', error);
        }
    });
}

function crearIntervalo() {
    // Datos a enviar al servidor para la creación del intervalo
    var horaInicio = $('#id_hora_inicio_add').val();
    var horaFin = $('#id_hora_fin_add').val();
    var costoServicio = $('#id_costo_servicio_add').val();

    var horaInicio = convertirMilisegundosAHora(horaInicio);
    var horaFin = convertirMilisegundosAHora(horaFin);

    // Puedes ajustar la ruta de la API según tu configuración en Django
    $.ajax({
        url: '/api/intervalo-tiempo-list/',
        method: 'POST',
        data: {
            hora_inicio: horaInicio,
            hora_fin: horaFin,
            costo_servicio: costoServicio
        },
        success: function (data) {
            // Aquí puedes realizar acciones después de crear el intervalo
            console.log('Intervalo creado con éxito:', data);

            // Obtener la referencia a la alerta de éxito
            var alertaExito = $('#mensajeCrear');

            // Añadir clases de Bootstrap para la alerta de éxito
            alertaExito.addClass('alert-success');

            // Mostrar la alerta de éxito
            alertaExito.fadeIn().delay(2300).fadeOut();

            // Recargar la página después de 2.3 segundos
            setTimeout(function () {
                location.reload();
            }, 2300);

            // Cerrar el modal
            $('#modalCrear').modal('hide');
        },
        error: function (error) {
            console.error('Error al crear el intervalo:', error);
        }
    });
}