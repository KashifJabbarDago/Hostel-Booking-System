from django.db import models

# Create your models here.

class SignUp(models.Model):
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

class BookVacancy(models.Model):
    name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    cnic = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    #for hostel storage 
    location = models.CharField(max_length=150)
    rent = models.CharField(max_length=150)
    room = models.CharField(max_length=150)
    vacancy = models.CharField(max_length=150)

class RegisterHostel(models.Model):
    name = models.CharField(max_length=150)
    cnic = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/media/')
    location = models.CharField(max_length=150)
    vacancy = models.CharField(max_length=150)
    rent = models.CharField(max_length=150)
    message = models.CharField(max_length=1000)

class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email  = models.EmailField()
    message = models.CharField(max_length=1000)


