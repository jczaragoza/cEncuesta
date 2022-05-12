from django.urls import path
from core.encuesta.views.views import *

urlpatterns = [
    path('add/', encuestaAddView.as_view(), name='encuesta_add'),
    path('aviso/', TemplateView.as_view(template_name="encuesta/aviso.html"), name='encuesta_aviso'),    
]

