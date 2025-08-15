# Airline Management — Documentación Técnica

## Resumen
Aplicación Django para gestión de aerolínea: aviones, vuelos, pasajeros y reservas. Incluye autenticación y CRUD básico en varias apps.

## Estructura principal
- Archivo principal de gestión: [manage.py](manage.py)  
- Configuración del proyecto: [`Airline_Management.settings`](Airline_Management/Airline_Management/settings.py)  
- Ruteo global: [`Airline_Management.urls`](Airline_Management/Airline_Management/urls.py)

Apps principales:
- accounts — autenticación y home (vista principal: [`apps.accounts.views.HomeView`](apps/accounts/views.py), plantilla: [apps/accounts/templates/index.html](apps/accounts/templates/index.html))
- airplanes — modelo y asientos: [`apps.airplanes.models.Airplane`](apps/airplanes/models.py), [`apps.airplanes.models.Seating`](apps/airplanes/models.py), vistas: [`apps.airplanes.views.AirplaneList`](apps/airplanes/views.py)
- flights — vuelos: [`apps.flights.models.Flight`](apps/flights/models.py), vistas: [`apps.flights.views.FlightList`](apps/flights/views.py)
- passengers — pasajeros: [`apps.passengers.models.Passenger`](apps/passengers/models.py), vistas: [`apps.passengers.views.PassengerListView`](apps/passengers/views.py)
- reservations — reservas y tickets: [`apps.reservations.models.Reservation`](apps/reservations/models.py), formulario: [`apps.reservations.forms.ReservationForm`](apps/reservations/forms.py), vistas: [`apps.reservations.views.ReservationCreate`](apps/reservations/views.py) y función AJAX [`apps.reservations.views.available_seats`](apps/reservations/views.py)

Plantilla base: [apps/home/templates/base.html](apps/home/templates/base.html)


## Rutas importantes
- Home / index: ruta raíz definida en [`apps.accounts.urls`](apps/accounts/urls.py)  
- App Airplanes: prefijo `/airplanes/` (ver [`Airline_Management.urls`](Airline_Management/Airline_Management/urls.py))  
- App Flights: prefijo `/flights/`  
- App Reservations: prefijo `/reservations/` (incluye endpoint AJAX `/reservations/available-seats/` manejado por [`apps.reservations.views.available_seats`](apps/reservations/views.py))

## Notas de implementación relevantes
- Generación automática de asientos al crear un avión: lógica en [`apps.airplanes.models.create_seatings` / post_save receiver](apps/airplanes/models.py).
- Al reservar, el asiento se marca como ocupado en el método `save()` de [`apps.reservations.models.Reservation`](apps/reservations/models.py) y se libera en `delete()`.
- El formulario [`apps.reservations.forms.ReservationForm`](apps/reservations/forms.py) filtra asientos disponibles según vuelo y valida precio mínimo con `flight.base_price`.
- La vista de creación de reservas ofrece un dropdown de asientos cargado por AJAX llamando a [`apps.reservations.views.available_seats`](apps/reservations/views.py) y la plantilla [apps/reservations/templates/reservations/create.html](apps/reservations/templates/reservations/create.html) contiene el script.

## Media y estáticos
- MEDIA_URL = `/media/` y MEDIA_ROOT configurados en [`Airline_Management.settings`](Airline_Management/Airline_Management/settings.py).
- En modo DEBUG, el servidor sirve media: configuración añadida en [`Airline_Management.urls`](Airline_Management/Airline_Management/urls.py).

## Migraciones y base de datos
- Migraciones incluidas por app en `apps/*/migrations/`. Mantenerlas en control de versiones.
- Comandos:
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  ```
---
