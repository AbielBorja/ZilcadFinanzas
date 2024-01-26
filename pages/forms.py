from django import forms
from .models import IntervaloTiempo

class CrearIntervaloTiempoForm(forms.ModelForm):
    hora_inicio = forms.DurationField(widget=forms.TimeInput(attrs={'class': 'time-duration-picker'}))
    hora_fin = forms.DurationField(widget=forms.TimeInput(attrs={'class': 'time-duration-picker'}))

    class Meta:
        model = IntervaloTiempo
        fields = ['hora_inicio', 'hora_fin', 'costo_servicio']

class EditarIntervaloTiempoForm(forms.ModelForm):
    hora_inicio = forms.DurationField(widget=forms.TimeInput(attrs={'class': 'time-duration-picker'}))
    hora_fin = forms.DurationField(widget=forms.TimeInput(attrs={'class': 'time-duration-picker'}))

    class Meta:
        model = IntervaloTiempo
        fields = ['hora_inicio', 'hora_fin', 'costo_servicio']
        labels = {
            'hora_inicio': 'Hora de inicio',
            'hora_fin': 'Hora de fin',
            'costo_servicio': 'Costo de servicio',
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Agrega un campo para seleccionar el intervalo de tiempo a editar
            self.fields['intervalo_a_editar'] = forms.ModelChoiceField(
                queryset=IntervaloTiempo.objects.all(),
                label='Selecciona un intervalo para editar',
                empty_label=None  # Elimina la opción vacía
            )
            