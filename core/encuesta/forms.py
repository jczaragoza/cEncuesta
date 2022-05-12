from datetime import datetime

from django import forms
from django.forms import CharField, ModelForm, TextInput

from core.encuesta.models import Encuesta

# %TEMP%
from crum import get_current_request
from django.contrib.auth import update_session_auth_hash


class EncuestaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Encuesta
        fields = '__all__'

        # widgets = {
        #     'clavesp': forms.TextInput(attrs={'placeholder': 'Ingrese Clave de Servidor Público'}),
        #     'rfc': forms.TextInput(attrs={'placeholder': 'Ingrese su RFC'}),
        #     'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese un Nombre'}),
        #     'apaterno': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido Paterno'}),
        #     'amaterno': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido Materno'}),
            
        #     'fecha_alta': forms.TextInput(
        #         attrs={
        #             'type': 'date',
        #             'class': 'form-control  datetimepicker',
        #             'min': '1922-01-01',
        #             'max': '2024-01-01',
        #         }
        #     ),
        #     'fecha_nacimiento': forms.TextInput(
        #         attrs={
        #             'type': 'date',
        #             'class': 'form-control  datetimepicker',
        #             'min': '1960-01-01',
        #             'max': '2003-01-01',
        #         }
        #     ),
        #     # 'fecha_baja': forms.TextInput(
        #     #     attrs={
        #     #         'type': 'date',
        #     #         'class': 'form-control  datetimepicker',
        #     #     }
        #     # ), 
        #    'num_plaza': forms.TextInput(attrs={'placeholder': 'Ingrese su Número de Plaza'}),
        #    'cuip': forms.TextInput(attrs={'placeholder': 'Ingrese su CUIP'}),
        #    'curp': forms.TextInput(attrs={'placeholder': 'Ingrese su CURP', 'maxlength':'18'}),
        #    'calle': forms.TextInput(attrs={'placeholder': 'Ingrese su Calle'}),
        #    'exterior': forms.TextInput(attrs={'placeholder': 'Número Exterior'}),
        #    'interior': forms.TextInput(attrs={'placeholder': 'Interior'}),
        #    'cp': forms.TextInput(attrs={'placeholder': 'Ingrese su Código Postal'}),
        #    'municipio': forms.Select(attrs={
        #         'class': 'custom-select select2',
        #         # 'style': 'width: 100%'
        #     }),
        # #     'colonia': forms.Select(attrs={
        # #         'class': 'custom-select select2',
        # #         # 'style': 'width: 100%'
        # #     }),
        #}
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

