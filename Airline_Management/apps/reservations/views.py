from django.shortcuts import render, get_object_or_404
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
    form_class = ReservationForm
    template_name = 'reservations/create.html'
    success_url = reverse_lazy('reservation_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        airplane = Airplane.objects.first()

        # Genero todos los asientos
        seatings = []
        for row in range(1, airplane.rows + 1):
            for col in range(1, airplane.columns + 1):
                seat_obj = Seating.objects.filter(airplane_id=airplane, row=row, column=col).first()
                if seat_obj:
                    seatings.append(seat_obj)
                else:
                    seatings.append(
                        Seating(
                            airplane_id=airplane,
                            number=(row - 1) * airplane.columns + col,
                            row=row,
                            column=col,
                            type='Normal',
                            state=False
                        )
                    )

        context['airplane'] = airplane
        context['seatings'] = seatings
        context['flights'] = Flight.objects.all()
        context['passengers'] = Passenger.objects.all()
        return context

    def form_valid(self, form):
        form.instance.reservation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        response = super().form_valid(form)

        seat = get_object_or_404(Seating, id=form.instance.seating_id.id)
        seat.state = True
        seat.save()

        return response



class ReservationListView(ListView):
    model = Reservation
    template_name = "reservations/reservation_list.html"
    context_object_name = "reservation"


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