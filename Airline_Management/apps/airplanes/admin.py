from django.contrib import admin
from apps.airplanes.models import Airplane,Seating

# Register your models here.
@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display =  ("id", "model", "capacity", "rows", "columns")
    list_filter = ("model", "capacity")
    search_fields = ("model", "capacity")

@admin.register(Seating)
class SeatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'row', 'column', 'type', 'state')
    list_filter = ('number', 'type', 'state')
    search_fields = ('type', 'state')