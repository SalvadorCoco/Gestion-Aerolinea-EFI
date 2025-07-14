from django.shortcuts import render
from apps.flights.models import Flight
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
)

from apps.flights.forms import FlightForm

class FlightList(ListView):
    model = Flight
    template_name = 'flights/list.html'
    context_object_name = 'flights'

class FlightDetail(DetailView):
    model = Flight
    template_name = 'flights/detail.html'
    context_object_name = 'flight'
    pk_url_kwarg = 'flight_id'

class FlightDelete(DeleteView):
    model = Flight
    template_name = 'flights/delete.html'
    pk_url_kwarg = 'flight_id'
    success_url = reverse_lazy('flight_list')

class FlightCreate(CreateView):
    form_class = FlightForm
    template_name = 'flights/create.html'
    success_url = reverse_lazy('flight_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creador_de_vuelos'] = 'Creador de Vuelos'
        return context