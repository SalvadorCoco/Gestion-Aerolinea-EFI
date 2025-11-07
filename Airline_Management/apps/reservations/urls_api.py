from django.urls import path
from . import api_views

urlpatterns = [
    path('create/', api_views.create_reservation_api, name='api_create_reservation'),
]