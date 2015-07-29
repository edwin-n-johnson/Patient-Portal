from django.contrib import admin

# Register your models here.
from .models import Patient,Physician,Appointment,Message

admin.site.register(Patient)
admin.site.register(Physician)
admin.site.register(Appointment)
admin.site.register(Message)
