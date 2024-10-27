from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

#home

    path('',views.home, name="homepage"),
    path('patientdirectreg/',views.patientdirectreg, name="patientdirectreg"),
    path('patientdirectregsave/',views.patientdirectregsave, name="patientdirectregsave"),

#login

    path('billingadminlogin/',views.billingadminlogin, name="billingadminlogin"),
    path('patientlogin/',views.patientlogin, name="patientlogin"),
    path('doctorlogin/',views.doctorlogin, name="doctorlogin"),
    path('hadminlogin/',views.hadminlogin, name="hadminlogin"),
    
#hadmin
    
    path('hadmincheck/',views.hadmincheck, name="hadmincheck"),
    path('hadmindashboard/',views.hadmindashboard, name="hadmindashboard"),
    path('hadminprofile/',views.hadminprofile, name="hadminprofile"),    
    path('hadminpatientlist/',views.hadminpatientlist, name="hadminpatientlist"),
    path('hadmindoctorlist/',views.hadmindoctorlist, name="hadmindoctorlist"),
    path('hadminmedicinelist/',views.hadminmedicinelist, name="hadminmedicinelist"),
    path('hadmindepartmentlist/',views.hadmindepartmentlist, name="hadmindepartmentlist"),


#doctor
    
    path('doctorcheck/',views.doctorcheck, name="doctorcheck"),
    path('doctordashboard/',views.doctordashboard, name="doctordashboard"),
    path('doctorprofile/',views.doctorprofile, name="doctorprofile"),
    path('patientlist/',views.patientlist, name="patientlist"),
    path('medicinelist/',views.medicinelist, name="medicinelist"),
    path('prescription/',views.prescription, name="prescription"),
    path('prescriptionsave/',views.prescriptionsave, name="prescriptionsave"),
    path('dbookinglist/',views.dbookinglist, name="dbookinglist"),
    

#patient
    
    path('patientcheck/',views.patientcheck, name="patientcheck"),
    path('patientdashboard/',views.patientdashboard, name="patientdashboard"),
    path('patientprofile/',views.patientprofile, name="patientprofile"),
    path('bookingpage/',views.bookingpage, name="bookingpage"),    
    path('bookinglist/',views.bookinglist, name="bookinglist"),
    path('bookingsave/',views.bookingsave, name="bookingsave"),
    
    

#billingadmin

    
    path('billingadmincheck/',views.billingadmincheck, name="billingadmincheck"),
    path('billingadmindashboard/',views.billingadmindashboard, name="billingadmindashboard"),
    path('billingadminprofile/',views.billingadminprofile, name="billingadminprofile"),
    path('bill/',views.bill, name="bill"),
    
    


#register

    path('patientreg/',views.patientreg, name="patientreg"),
    path('patientregsave/',views.patientregsave, name="patientregsave"),

    path('doctorreg/',views.doctorreg, name="doctorreg"),
    path('doctorregsave/',views.doctorregsave, name="doctorregsave"),

    path('billingadminreg/',views.billingadminreg, name="billingadminreg"),
    path('billingadminregsave/',views.billingadminregsave, name="billingadminregsave"),

    path('departmentreg/',views.departmentreg, name="departmentreg"),
    path('departmentsave/',views.departmentsave, name="departmentsave"),

    path('medicinereg/',views.medicinereg, name="medicinereg"),
    path('medicinesave/',views.medicinesave, name="medicinesave"),
    
#edit

    path('edith/',views.edith, name="edith"),
    path('edithsave/',views.edithsave, name="edithsave"),

    path('editd/',views.editd, name="editd"),
    path('editdsave/',views.editdsave, name="editdsave"),

    path('editp/',views.editp, name="editp"),
    path('editpsave/',views.editpsave, name="editpsave"),

    path('editb/',views.editb, name="editb"),
    path('editbsave/',views.editbsave, name="editbsave"),


#delete    

    path('delete_bookinglist/<id>',views.delete_bookinglist, name="delete_bookinglist"),

#java

    path('fetch_doctor/<int:doctorId>/',views.fetch_doctor, name="fetch_doctor"),
    path('fetch_medicine/<int:patientId>/', views.fetch_medicine, name='fetch_medicine'),
    path('fetch_patients/', views.fetch_patients, name='fetch_patients'),
    path('fetch_purchases/',views.fetch_purchases, name='fetch_purchases'),
    path('save_purchase/<int:patient_id>/',views.save_purchase, name='save_purchase'),
     path('check_slot_availability/', views.check_slot_availability, name='check_slot_availability'),
    

#logout

    path('hadminlogout/',views.hadminlogout, name="hadminlogout"),
    path('doctorlogout/',views.doctorlogout, name="doctorlogout"),
    path('patientlogout/',views.patientlogout, name="patientlogout"),
    path('billingadminlogout/',views.billingadminlogout, name="billingadminlogout"),

#report

    path('reportview/',views.reportview, name="reportview"),
    


]