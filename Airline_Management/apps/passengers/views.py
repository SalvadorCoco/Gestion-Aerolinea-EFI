# apps/passengers/views.py

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Passenger      # <-- Importa el modelo 'Passenger'
from .forms import PassengerForm   # <-- Importa el formulario 'PassengerForm'

# READ: Lista de pasajeros
class PassengerListView(ListView):
    model = Passenger
    template_name = 'passengers/pasajeroList.html' # Asegúrate que la ruta de la plantilla es correcta
    context_object_name = 'passengers' # Nombre de la variable en la plantilla para la lista
    paginate_by = 10 # Opcional: paginación

# READ: Detalle de un pasajero
class PassengerDetailView(DetailView):
    model = Passenger
    template_name = 'passengers/pasajeroDetail.html' # Asegúrate que la ruta de la plantilla es correcta
    context_object_name = 'pasajero' # Nombre de la variable en la plantilla para el objeto individual

# CREATE: Crear un nuevo pasajero
class PassengerCreateView(CreateView):
    model = Passenger
    form_class = PassengerForm # Usa el formulario 'PassengerForm'
    template_name = 'passengers/pasajeroForm.html' # Asegúrate que la ruta de la plantilla es correcta
    success_url = reverse_lazy('passengerList') # Redirige a la lista después de crear. Asegúrate que este nombre de URL existe en tu urls.py

# UPDATE: Actualizar un pasajero existente
class PassengerUpdateView(UpdateView):
    model = Passenger
    form_class = PassengerForm # Usa el formulario 'PassengerForm'
    template_name = 'passengers/pasajeroForm.html' # Asegúrate que la ruta de la plantilla es correcta
    context_object_name = 'pasajero' # Nombre de la variable en la plantilla para el objeto individual
    # success_url se obtiene automáticamente de getAbsoluteUrl del modelo si existe,
    # o puedes definirlo explícitamente como reverse_lazy('passengerDetail', kwargs={'pk': self.object.pk})
    # Si quieres que redirija al detalle del pasajero después de actualizar, agrega:
    # def get_success_url(self):
    #     return reverse_lazy('passengerDetail', kwargs={'pk': self.object.pk})


# DELETE: Eliminar un pasajero
class PassengerDeleteView(DeleteView):
    model = Passenger
    template_name = 'passengers/pasajeroConfirmDelete.html' # Asegúrate que la ruta de la plantilla es correcta
    context_object_name = 'pasajero' # Nombre de la variable en la plantilla para el objeto individual
    success_url = reverse_lazy('passengerList') # Redirige a la lista después de eliminar. Asegúrate que este nombre de URL existe en tu urls.py