import json

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView, View, TemplateView
from core import encuesta

from core.security.mixins import PermissionMixin, ModuleMixin
from core.security.models import *
from core.encuesta.models import *
from core.encuesta.forms import EncuestaForm


class encuestaAddView(CreateView):
    model = Encuesta
    template_name = 'encuesta/create.html'
    form_class = EncuestaForm
    success_url = reverse_lazy('encuesta_aviso')
    permission_required = 'add_encuesta'

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'correo':
                if Encuesta.objects.filter(correo=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo Registro'
        context['action'] = 'add'
        return context

