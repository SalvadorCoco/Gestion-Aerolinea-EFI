# apps/passengers/views.py

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy, reverse
from .models import Passenger
from .forms import PassengerForm

class PassengerListView(ListView):
    model = Passenger
    template_name = 'passengers/List.html'
    context_object_name = 'passengers'
    paginate_by = 10

class PassengerDetailView(DetailView):
    model = Passenger
    template_name = 'passengers/Detail.html'
    context_object_name = 'pasajero'

class PassengerCreateView(CreateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'passengers/Create.html'
    success_url = reverse_lazy('passengerList')

class PassengerUpdateView(UpdateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'passengers/Create.html'
    context_object_name = 'pasajero'
    
    def get_success_url(self):
        return reverse('passengerDetail', kwargs={'pk': self.object.pk})

class PassengerDeleteView(DeleteView):
    model = Passenger
    template_name = 'passengers/Delete.html'
    context_object_name = 'pasajero'
    success_url = reverse_lazy('passengerList')
