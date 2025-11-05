from django.urls import path
from .views.views_accounts import (
    AccountListCreateView,
    AccountRetrieveUpdateDestroyView,
)
from .views.views_airplanes import (
    AirplaneListCreateView,
    AirplaneRetrieveUpdateDestroyView
)

urlpatterns = [
    path('accounts/', AccountListCreateView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountRetrieveUpdateDestroyView.as_view(), name='account-detail'),

    path('airplanes/', AirplaneListCreateView.as_view(), name='airplane-list'),
    path('airplanes/<int:pk>/', AirplaneRetrieveUpdateDestroyView.as_view(), name='airplane-detail'),
]