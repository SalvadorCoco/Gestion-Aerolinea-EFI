from django.urls import path
from .views import (
    ReservationCreate,
    ReservationListView,
    ReservationUpdateView,
    ReservationDeleteView,
    ReservationDetailView,
)

urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation_list'),
    path('create/', ReservationCreate.as_view(), name='reservation_create'),
    path('<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),  # CORRECCIÓN: coincide con template
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
]
