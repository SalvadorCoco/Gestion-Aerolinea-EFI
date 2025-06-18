from django import forms
from apps.airplanes.models import Airplane, Seating

class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airplane
        fields = ['model', 'capacity', 'rows', 'columns']
        widgets = {
            'model' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el modelo'
                }
            ),
            'capacity' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la capacidad'
                }
            ),
            'rows' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Numero de filas'
                }
            ),
            'columns' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Numero de columnas'
                }
            ),
        } 

        

class SeatingForm(forms.ModelForm):
    class Meta:
        model = Seating
        fields = ['airplane_id', 'number', 'row', 'column', 'type', 'state']
        widgets = {
            'airplane_id': forms.Select(),
            'number': forms.NumberInput(),
            'row': forms.NumberInput(),
            'column': forms.NumberInput(),
            'type': forms.TextInput(),
            'state': forms.CheckboxInput(),
        }