from django import forms
from . models import Consulta

class ClinicaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
