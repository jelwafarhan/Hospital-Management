from django.db import models
from django.utils import timezone

# Create your models here.

class department(models.Model):
    name=models.CharField(max_length=246)
    bio=models.CharField(max_length=246)
    def __str__(self):
        return self.name

class doctor(models.Model):
    name=models.CharField(max_length=246)
    img= models.ImageField(default='1.jpg',blank=True) 
    email= models.CharField(max_length=246)
    password=models.CharField(max_length=246) 
    number= models.CharField(max_length=246)
    age= models.CharField(max_length=246)   
    date=models.CharField(max_length=246)
    gender=models.CharField(max_length=246)
    time=models.CharField(max_length=246)
    departments=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class patient(models.Model):
    name = models.CharField(max_length=246)
    img= models.ImageField(default='1.jpg',blank=True) 
    email=models.EmailField(max_length=246)
    password=models.CharField(max_length=246) 
    number= models.CharField(max_length=246)
    age= models.CharField(max_length=246) 
    gender=models.CharField(max_length=246)
    reg_date=models.DateTimeField(default=timezone.now)    
    def __str__(self):
        return self.name


class hadmin(models.Model):
    name=models.CharField(max_length=246)
    email=models.CharField(max_length=246)
    password=models.CharField(max_length=246) 
    number= models.CharField(max_length=246)    
    def __str__(self):
        return self.name

class billingadmin(models.Model):
    name=models.CharField(max_length=246)
    email=models.CharField(max_length=246)
    password=models.CharField(max_length=246) 
    number= models.CharField(max_length=246)    
    def __str__(self):
        return self.name

class medicine(models.Model):
    name=models.CharField(max_length=246)
    use=models.CharField(max_length=246)
    price=models.CharField(max_length=246)
    def __str__(self):
        return self.name

class pprescription(models.Model):
    patientname=models.ForeignKey(patient,on_delete=models.CASCADE)
    medicinename=models.ForeignKey(medicine,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=246)
    def __str__(self):
        return self.patientname.name

class booking(models.Model):
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    date=models.CharField(max_length=246)
    start_time = models.TimeField()  # Start time of the booking
    end_time = models.TimeField()    # End time of the booking
    def __str__(self):
        return self.patient.name
    
class purchase(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.patient.name