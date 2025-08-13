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

# views.py
class ReservationCreate(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/create.html'
    success_url = reverse_lazy('reservation_list')

    def get_form_kwargs(self):
        return super().get_form_kwargs()





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