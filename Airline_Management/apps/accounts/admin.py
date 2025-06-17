from django.contrib import admin
from .models import Account
from .models import Role

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role_id')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
