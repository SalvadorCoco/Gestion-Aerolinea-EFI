from django.shortcuts import render

from apps.airplanes.models import Airplane, Seating
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from apps.airplanes.forms import AirlineForm
# Create your views here.

class AirplaneList(ListView):
    model = Airplane
    template_name = 'airplanes/list.html'
    context_object_name = 'airplanes'

class AirplaneDetail(DetailView):
    model = Airplane
    template_name = 'airplanes/detail.html'
    context_object_name = 'airplane'
    pk_url_kwarg = 'airplane_id'

class AirplaneDelete(DeleteView):
    model = Airplane
    template_name = 'airplanes/delete.html'
    pk_url_kwarg = 'airplane_id'
    success_url = reverse_lazy('airplane_list')

class AirplaneCreate(CreateView):
    form_class = AirlineForm
    template_name = 'airplanes/create.html'
    success_url = reverse_lazy('airplane_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creador_de_aviones'] = 'Creador de Aviones'
        return context
    
class AirplaneEdit(UpdateView):
    model = Airplane
    form_class = AirlineForm
    template_name = 'airplanes/edit.html'
    pk_url_kwarg = 'airplane_id'
    success_url = reverse_lazy('airplane_list')


