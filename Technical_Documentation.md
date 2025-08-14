# Airline Management - Documentación Técnica

## Descripción General

**Airline Management** es una aplicación web desarrollada en Django para la gestión integral de una aerolínea. Permite administrar aviones, vuelos, pasajeros, reservas y usuarios, facilitando la operación y el control de los procesos internos. El sistema está orientado a cubrir las necesidades de registro, consulta y edición de información relevante para la gestión de vuelos y pasajeros.

## Estructura del Proyecto

```
Airline_Management/
│   db.sqlite3
│   manage.py
│
├── Airline_Management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/
│   ├── accounts/      # Gestión de usuarios y autenticación
│   ├── airplanes/     # Gestión de aviones
│   ├── flights/       # Gestión de vuelos
│   ├── home/          # Página principal y base
│   ├── passengers/    # Gestión de pasajeros
│   └── reservations/  # Gestión de reservas y tickets
│
├── docs/              # Documentación adicional
└── media/             # Archivos multimedia (imágenes de aviones y destinos)
```

- **settings.py**: Configuración global del proyecto.
- **templates/**: Plantillas HTML organizadas por app.
- **static/**: Archivos estáticos (CSS, imágenes).
- **apps/**: Cada app representa una funcionalidad principal.

## Modelos y Relaciones

El sistema utiliza modelos para representar entidades clave:

- **Airplane**: Modelo de avión (capacidad, filas, columnas, imagen).
- **Flight**: Vuelo (origen, destino, fechas, avión asociado, responsable).
- **Passenger**: Pasajero (datos personales y de contacto).
- **Reservation**: Reserva (vuelo, pasajero, asiento, precio, estado).
- **Ticket**: Ticket asociado a una reserva.
- **Account**: Usuario del sistema (roles, autenticación).

### Diagrama ER (simplificado)

```
Account ---< Flight >--- Airplane
Passenger ---< Reservation >--- Flight
Reservation --- Ticket
```

- Un **Flight** está asociado a un **Airplane**.
- Un **Passenger** puede tener varias **Reservation**.
- Cada **Reservation** está asociada a un **Flight** y genera un **Ticket**.

## Rutas y Vistas

Las URLs están organizadas por app. Ejemplo:

- `/airplanes/`  
  - Listar: `AirplaneList`
  - Crear: `AirplaneCreate`
  - Detalle: `AirplaneDetail`
  - Editar: `AirplaneUpdate`
  - Eliminar: `AirplaneDelete`

- `/flights/`  
  - Listar: `FlightList`
  - Crear: `FlightCreate`
  - Detalle: `FlightDetail`
  - Editar: `FlightUpdate`
  - Eliminar: `FlightDelete`

- `/passengers/`  
  - Listar: `PassengerListView`
  - Crear: `PassengerCreateView`
  - Detalle: `PassengerDetailView`
  - Editar: `PassengerUpdateView`
  - Eliminar: `PassengerDeleteView`

Las vistas utilizan clases basadas en Django (`ListView`, `DetailView`, `CreateView`, `DeleteView`).

## Formularios y Validaciones

Cada app tiene formularios personalizados usando `ModelForm`:

- Validaciones de campos obligatorios, formatos y unicidad.
- Ejemplo: [`RegisterForm`](apps/accounts/forms.py) valida usuario, email y contraseñas.
- Los formularios se renderizan en las plantillas y gestionan la entrada del usuario.

## Plantillas

- Herencia desde `base.html` (estructura común).
- Cada funcionalidad tiene su propia plantilla (`list.html`, `create.html`, `edit.html`, etc.).
- El flujo de renderizado utiliza bloques para personalizar títulos, contenido y navegación.

## Requisitos de Instalación y Despliegue

1. **Clonar el repositorio**
   ```sh
   git clone https://github.com/tuusuario/Gestion-Aerolinea-EFI.git
   cd Gestion-Aerolinea-EFI/Airline_Management
   ```

2. **Instalar dependencias**
   ```sh
   pip install -r requirements.txt
   ```

3. **Migrar la base de datos**
   ```sh
   python manage.py migrate
   ```

4. **Crear superusuario**
   ```sh
   python manage.py createsuperuser
   ```

5. **Ejecutar el servidor**
   ```sh
   python manage.py runserver
   ```

## Ejemplos de Uso

- **Crear**: Accede a la lista y haz clic en "Crear" (requiere autenticación de administrador).
- **Listar**: Las listas muestran todos los registros disponibles.
- **Editar**: Desde la lista, selecciona "Editar" en el registro deseado.
- **Eliminar**: Desde la lista, selecciona "Eliminar" y confirma la acción.

Las acciones están protegidas por permisos; solo los administradores pueden crear, editar o eliminar.

---

Para más detalles, revisa los archivos de cada app y sus plantillas asociadas.