from django.contrib import admin
from .models import *

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    fields = ["name", "lastname", "age"]
    list_display = ["name", "lastname", "age"]

class PatientAdmin(admin.ModelAdmin):
    fields = ["name", "lastname", "age"]
    list_display = ["name", "lastname", "age"]

class RendezvousAdmin(admin.ModelAdmin):
    fields = ["date", "is_active", "doctor", "patient"]
    list_display = ["date", "is_active"]
    readonly_fields = ["date"]

class DoctorsInline(admin.TabularInline):
    model = Department.doctors.through
    extra = 3

class DepartmentAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]
    inlines = [DoctorsInline]

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Rendezvous, RendezvousAdmin)
admin.site.register(Department, DepartmentAdmin)
