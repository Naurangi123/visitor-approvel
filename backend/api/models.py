from django.db import models
from datetime import datetime



class Doctor(models.Model):
    doctor_name= models.CharField(max_length=50)
    specialization= models.CharField(max_length=50)
    contact_number= models.CharField(max_length=10)
    gender= models.CharField(max_length=10)
    
    def __str__(self):
        return self.doctor_name
    

    

class Patient(models.Model):
    patient_name= models.CharField(max_length=50)
    address=models.TextField(max_length=100,null=True)
    gender= models.CharField(max_length=10)
    contact=models.CharField(max_length=15)
    age = models.DateTimeField(auto_now_add=True)
    blood= models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.patient_name}"


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=True)
    reason= models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.patient} appoint to {self.doctor} for {self.reason}"

class React(models.Model):
    name=models.CharField(max_length=50)
    detail=models.CharField(max_length=50)