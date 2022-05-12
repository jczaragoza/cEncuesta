from django.db import models
from django.forms.models import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
#from smart_selects.db_fields import ChainedForeignKey

#from core.kardex.choices import *
from datetime import date, datetime


#encuesta
class Encuesta(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre(s)')
    apaterno = models.CharField(max_length=255, verbose_name='Apellido Paterno')
    amaterno = models.CharField(max_length=255, verbose_name='Apellido Materno')
    correo = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Correo Electrónico')
    telefono_movil = models.CharField(max_length=10, blank=True, null=True, verbose_name='Teléfono Móvil')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre 
    
    def get_full_name(self):
        return '{} {} {}'.format(self.nombre, self.apaterno, self.amaterno)

    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        self.apaterno = self.apaterno.upper()
        self.amaterno = self.amaterno.upper()
        super(Encuesta, self).save()
    
    def toJSON(self):
        item['full_name'] = self.get_full_name()
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Encuesta'
        ordering = ['id']

