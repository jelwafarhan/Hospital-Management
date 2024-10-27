from django.contrib import admin
from .models import hadmin,doctor,billingadmin,patient,department,medicine,pprescription,booking,purchase
# Register your models here.

class doctorAdmin(admin.ModelAdmin):
    list_display=['id','name']    

class departmentAdmin(admin.ModelAdmin):
    list_display=['id','name']    

class patientAdmin(admin.ModelAdmin):
    list_display=['id','name']    

class medicineAdmin(admin.ModelAdmin):
    list_display=['id','name']

class pprescriptionAdmin(admin.ModelAdmin):
    list_display=['id','patientname','medicinename']

class bookingAdmin(admin.ModelAdmin):
    list_display=['id','name']

admin.site.register(hadmin)
admin.site.register(doctor)
admin.site.register(billingadmin)
admin.site.register(patient)
admin.site.register(department)
admin.site.register(medicine,medicineAdmin)
admin.site.register(pprescription,pprescriptionAdmin)
admin.site.register(booking)
admin.site.register(purchase)
