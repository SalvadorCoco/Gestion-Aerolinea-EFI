from django.urls import path
from apps.reservations.views import (
    ReservationCreate,
    ReservationListView,
    ReservationDetailView,
    ReservationDeleteView,
    ReservationUpdateView
    )

urlpatterns = [
    path(
        route='reservation_create/',
        view=ReservationCreate.as_view(),
        name='reservation_create'
    ),
    path(
        route='', 
        view=ReservationListView.as_view(),
        name='reservation_list'
        ),
    path(
        route='<int:pk>/',
        view=ReservationDetailView.as_view(),
        name='reservation_detail'
        ),
    path(
        route='<int:pk>/delete/', 
        view=ReservationDeleteView.as_view(), 
        name='reservation_delete'
        ),
    path(
        route='<int:pk>/update/', 
        view=ReservationUpdateView.as_view(), 
        name='reservation_update'
        ),
]
