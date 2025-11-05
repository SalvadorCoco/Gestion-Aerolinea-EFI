from django.urls import path
from .views.views_accounts import (
    AccountListCreateView,
    AccountRetrieveUpdateDestroyView,
)
from .views.views_airplanes import (
    AirplaneListCreateView,
    AirplaneRetrieveUpdateDestroyView
)
from .views.views_flights import (
    FlightListCreateView,
    FlightRetrieveUpdateDestroyView,
)
from .views.views_passengers import (
    PassengerListCreateView,
    PassengerRetrieveUpdateDestroyView,
)
from .views.views_reservations import (
    ReservationListCreateView,
    ReservationRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('accounts/', AccountListCreateView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountRetrieveUpdateDestroyView.as_view(), name='account-detail'),

    path('airplanes/', AirplaneListCreateView.as_view(), name='airplane-list'),
    path('airplanes/<int:pk>/', AirplaneRetrieveUpdateDestroyView.as_view(), name='airplane-detail'),

    path('flights/', FlightListCreateView.as_view(), name='flight-list'),
    path('flights/<int:pk>/', FlightRetrieveUpdateDestroyView.as_view(), name='flight-detail'),
    
    path('passengers/', PassengerListCreateView.as_view(), name='passenger-list'),
    path('passengers/<int:pk>/', PassengerRetrieveUpdateDestroyView.as_view(), name='passenger-detail'),

    path('reservations/', ReservationListCreateView.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-detail'),
]