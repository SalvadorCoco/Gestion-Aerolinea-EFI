# apps/passengers/urls.py

from django.urls import path
from .views import (
    PassengerListView,
    PassengerDetailView,
    PassengerCreateView,
    PassengerUpdateView,
    PassengerDeleteView
)

urlpatterns = [
    # La URL para la lista de pasajeros debería ser solo la base de la app
    path('', PassengerListView.as_view(), name='passengerList'), # <-- Cambiado de 'pasajeros/' a ''
    path('nuevo/', PassengerCreateView.as_view(), name='passengerCreate'), # <-- Cambiado de 'pasajeros/nuevo/' a 'nuevo/'
    path('<int:pk>/', PassengerDetailView.as_view(), name='passengerDetail'), # <-- Cambiado
    path('<int:pk>/editar/', PassengerUpdateView.as_view(), name='passengerUpdate'), # <-- Cambiado
    path('<int:pk>/eliminar/', PassengerDeleteView.as_view(), name='passengerDelete'), # <-- Cambiado
]