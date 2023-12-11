from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['dia_reserva', 'hora_reserva', 'cliente']  # Ajusta los campos según tu modelo

    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        # Personaliza el formulario si es necesario
