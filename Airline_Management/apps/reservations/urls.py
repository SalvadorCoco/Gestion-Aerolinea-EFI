from django.urls import path
from .views import (
    ReservationCreate,
    ReservationListView,
    ReservationUpdateView,
    ReservationDeleteView,
    ReservationDetailView,
    get_all_seatings,
)

urlpatterns = [
    path('', ReservationListView.as_view(), name='list'),
    path('create/', ReservationCreate.as_view(), name='create'),
    path('<int:pk>/update/', ReservationUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ReservationDeleteView.as_view(), name='delete'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='detail'),
    path('ajax/all_seatings/', get_all_seatings, name='all_seatings'),
]