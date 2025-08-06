from django.urls import path

from apps.flights.views import (
    FlightCreate,
    FlightDelete,
    FlightDetail, 
    FlightList,
)

urlpatterns = [
    path(
        route='flight_list/',
        view=FlightList.as_view(),
        name='flight_list'
    ),
    path(
        route='flight_create/',
        view=FlightCreate.as_view(),
        name='flight_create'
    ),
    path(
        route='flight_detail/<int:flight_id>/',
        view=FlightDetail.as_view(),
        name='flight_detail'
    ),
    path(
        route='flight_delete/<int:flight_id>/',
        view=FlightDelete.as_view(),
        name='flight_delete'
    ),
]