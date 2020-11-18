from django.contrib import admin
from .models import ReservationForm

class AdminReservationForm(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date']

admin.site.register(ReservationForm, AdminReservationForm)