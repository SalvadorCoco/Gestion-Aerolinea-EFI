from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from apps.reservations.models import Reservation
from apps.reservations.forms import ReservationForm
from apps.flights.models import Flight
from apps.passengers.models import Passenger
from apps.airplanes.models import Seating

class ReservationCreate(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/create.html'
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = Flight.objects.all()
        context['passengers'] = Passenger.objects.all()

        flight_id = self.request.GET.get('flight_id') or self.request.POST.get('flight_id')
        if flight_id:
            flight = Flight.objects.get(id=flight_id)
            context['seatings'] = Seating.objects.filter(airplane_id=flight.airplane_id, state=False)
        else:
            context['seatings'] = Seating.objects.filter(state=False)

        return context

class ReservationListView(ListView):
    model = Reservation
    template_name = "reservations/list.html"
    context_object_name = "reservations"

class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservations/update.html"
    success_url = reverse_lazy("list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = Flight.objects.all()
        context['passengers'] = Passenger.objects.all()
        return context

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = "reservations/delete.html"
    success_url = reverse_lazy("list")

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = "reservations/detail.html"
    context_object_name = "reservation"

def get_all_seatings(request):
    seatings = Seating.objects.all()
    data = [
        {
            'id': seating.id,
            'name': str(seating),
            'state': seating.state,
            'airplane_id': seating.airplane_id_id
        }
        for seating in seatings
    ]
    return JsonResponse({'seatings': data})

