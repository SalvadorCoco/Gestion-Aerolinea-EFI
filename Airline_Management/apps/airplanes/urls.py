from django.urls import path

from apps.airplanes.views import (
    AirplaneCreate,
    AirplaneDelete,
    AirplaneDetail, 
    AirplaneList,
    AirplaneEdit,
)

urlpatterns = [
    path(
        route='airplane_list/',
        view=AirplaneList.as_view(),
        name='airplane_list'
    ),
    path(
        route='airplane_create/',
        view=AirplaneCreate.as_view(),
        name='airplane_create'
    ),
    path(
        route='airplane_detail/<int:airplane_id>/',
        view=AirplaneDetail.as_view(),
        name='airplane_detail'
    ),
    path(
        route='airplane_delete/<int:airplane_id>/',
        view=AirplaneDelete.as_view(),
        name='airplane_delete'
    ),
    path(
        route='airplane_update/<int:airplane_id>/',
        view=AirplaneEdit.as_view(),
        name='airplane_update'
    )
]