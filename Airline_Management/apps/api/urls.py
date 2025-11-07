from django.urls import path
from .views.views_accounts import (
    AccountListCreateView,
    AccountRetrieveUpdateDestroyView,
)
from .views.views_airplanes import (
    AirplaneListCreateView,
    AirplaneRetrieveUpdateDestroyView,
    AirplaneLayoutView,  # nueva vista para layout y disponibilidad
)
from .views.views_flights import (
    FlightListCreateView,
    FlightRetrieveUpdateDestroyView,
    FlightPassengersListView,
    FlightReserveView,
)
from .views.views_flights import FlightSeatsView, FlightSeatDetailView
from .views.views_passengers import (
    PassengerListCreateView,
    PassengerRetrieveUpdateDestroyView,
    PassengerActiveReservationsView,
)
from .views.views_reservations import (
    ReservationListCreateView,
    ReservationRetrieveUpdateDestroyView,
    ReservationStatusUpdateView,
    TicketGenerateView,
    TicketRetrieveView,
)

urlpatterns = [
    path('accounts/', AccountListCreateView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountRetrieveUpdateDestroyView.as_view(), name='account-detail'),

    path('airplanes/', AirplaneListCreateView.as_view(), name='airplane-list'),
    path('airplanes/<int:pk>/', AirplaneRetrieveUpdateDestroyView.as_view(), name='airplane-detail'),
    path('airplanes/<int:pk>/layout/', AirplaneLayoutView.as_view(), name='airplane-layout'),

    path('flights/', FlightListCreateView.as_view(), name='flight-list'),
    path('flights/<int:pk>/', FlightRetrieveUpdateDestroyView.as_view(), name='flight-detail'),
    path('flights/<int:pk>/passengers/', FlightPassengersListView.as_view(), name='flight-passengers'),
    path('flights/<int:pk>/reserve/', FlightReserveView.as_view(), name='flight-reserve'),
    path('flights/<int:pk>/seats/', FlightSeatsView.as_view(), name='flight-seats'),
    path('flights/<int:pk>/seats/<int:seat_number>/', FlightSeatDetailView.as_view(), name='flight-seat-detail'),

    path('passengers/', PassengerListCreateView.as_view(), name='passenger-list'),
    path('passengers/<int:pk>/', PassengerRetrieveUpdateDestroyView.as_view(), name='passenger-detail'),
    path('passengers/<int:pk>/reservations/', PassengerActiveReservationsView.as_view(), name='passenger-active-reservations'),

    path('reservations/', ReservationListCreateView.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-detail'),
    path('reservations/<int:pk>/status/', ReservationStatusUpdateView.as_view(), name='reservation-status'),
    path('reservations/<int:pk>/ticket/', TicketGenerateView.as_view(), name='reservation-ticket'),

    path('tickets/<str:code>/', TicketRetrieveView.as_view(), name='ticket-detail'),
]