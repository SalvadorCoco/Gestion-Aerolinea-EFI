from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView
    )
from apps.reservations.models import Reservation
from apps.reservations.forms import ReservationForm
from apps.airplanes.models import Airplane, Seating
from apps.flights.models import Flight
from apps.passengers.models import Passenger
import random, string

class ReservationCreate(CreateView):
    model = Reservation
    queryset = Reservation.objects.all()   # <- explícito para evitar el error
    form_class = ReservationForm
    template_name = 'reservations/create.html'
    success_url = reverse_lazy('reservation_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Si quieres filtrar asientos por avión, pasalo al formulario
        airplane = Airplane.objects.first()
        kwargs['airplane'] = airplane
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        airplane = Airplane.objects.first()
        context['airplane'] = airplane

        # Asegurarnos de que todos los asientos existen en la BD
        seatings = []
        for row in range(1, airplane.rows + 1):
            for col in range(1, airplane.columns + 1):
                number = (row - 1) * airplane.columns + col
                seat_obj, created = Seating.objects.get_or_create(
                    airplane_id=airplane,
                    row=row,
                    column=col,
                    defaults={
                        'number': number,
                        'type': 'Normal',
                        'state': False
                    }
                )
                seatings.append(seat_obj)

        context['seatings'] = seatings
        context['flights'] = Flight.objects.all()
        context['passengers'] = Passenger.objects.all()
        return context

    def form_invalid(self, form):
        # imprime errores en consola (útil en desarrollo)
        print("FORM ERRORS:", form.errors)
        for field, errs in form.errors.items():
            messages.error(self.request, f"{field}: {errs}")
        return super().form_invalid(form)



class ReservationListView(ListView):
    model = Reservation
    template_name = "reservations/reservation_list.html"
    context_object_name = "reservations"


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = "reservations/reservation_detail.html"
    context_object_name = "reservation"


class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = "reservations/reservation_confirm_delete.html"
    success_url = reverse_lazy("reservation_list")

class ReservationUpdateView(UpdateView):
    model = Reservation
    template_name = "reservations/reservation_update.html"
    success_url = reverse_lazy("reservation_list")