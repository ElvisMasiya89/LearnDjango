from django.contrib import admin
from .models import Patient

# # Register your models here.
# admin.site.register(Patient)


# How to customise the Admin Form with more Detail
class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
                  ("Patient Details", {'fields': ['first_name', 'age', 'last_name']}),
                  ("Patient Health", {'fields': ['heartrate']})
                 ]


admin.site.register(Patient, PatientAdmin)
