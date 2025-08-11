from apps.airplanes.models import Airplane, Seating

def generate_seats_for_airplane(airplane_id):
    airplane = Airplane.objects.get(id=airplane_id)

    # Eliminar asientos existentes para evitar duplicados
    Seating.objects.filter(airplane_id=airplane).delete()

    seats = []
    for row in range(1, airplane.rows + 1):
        for col in range(1, airplane.columns + 1):
            number = (row - 1) * airplane.columns + col
            seat = Seating(
                airplane_id=airplane,
                number=number,
                row=row,
                column=col,
                type='Normal',
                state=False
            )
            seats.append(seat)

    Seating.objects.bulk_create(seats)
    print(f"Generados {len(seats)} asientos para el avión {airplane.model} (ID {airplane.id})")
