from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField()
    collegename = models.CharField(max_length=100)
    country = models.CharField(max_length=56)
    university = models.CharField(max_length=150, blank=True)
    courses = models.CharField(max_length=50, default="Masters")
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    examname = models.CharField(max_length=30)
    examscore = models.DecimalField(max_digits=5, decimal_places=2)
    fees = models.BigIntegerField()
    fees_extra = models.BooleanField(default=False)
    date_filled = models.DateField(default=timezone.now)

    def __str__(self):
        return self.fullname
