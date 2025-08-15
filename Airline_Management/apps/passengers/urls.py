from django.urls import path
from .views import (
    PassengerListView,
    PassengerDetailView,
    PassengerCreateView,
    PassengerUpdateView,
    PassengerDeleteView
)

urlpatterns = [
    path('', PassengerListView.as_view(), name='passengerList'), 
    path('nuevo/', PassengerCreateView.as_view(), name='passengerCreate'), 
    path('<int:pk>/', PassengerDetailView.as_view(), name='passengerDetail'), 
    path('<int:pk>/editar/', PassengerUpdateView.as_view(), name='passengerUpdate'),
    path('<int:pk>/eliminar/', PassengerDeleteView.as_view(), name='passengerDelete'),
]