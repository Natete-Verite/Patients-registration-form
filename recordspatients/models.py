from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    male = models. BooleanField()
    female = models.BooleanField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    diabetes = models.BooleanField()
    no_diabetes = models.BooleanField()
    unknown = models.BooleanField()
    