from django.db import models
from django.contrib.auth.models import User

class Specialization(models.Model):

    title=models.CharField(max_length=200)

    @property
    def doctor(self):
        return self.doctor_set.all()

    def __str__(self):
        return self.title

class Doctor(models.Model):

    name=models.CharField(max_length=200)
    specialization=models.ForeignKey(Specialization, on_delete=models.CASCADE)
    age=models.IntegerField()
    image=models.ImageField(upload_to="doctor",default="doctor/default.jpeg")
    experience=models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booking_date=models.DateField()
    created_date=models.DateTimeField(auto_now_add=True)
    booking_no=models.IntegerField()
    is_active=models.BooleanField(default=True)