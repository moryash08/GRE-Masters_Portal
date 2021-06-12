from django.db import models
from django.utils import timezone


# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=56)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country


class University(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    university = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.university


class Courses(models.Model):
    # country = models.ForeignKey('Country', on_delete=models.CASCADE)
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    course = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course


class Student(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField()
    collegename = models.CharField(max_length=100)
    country = models.CharField(max_length=56)
    university = models.CharField(max_length=150, blank=True)
    courses = models.CharField(max_length=200, default="Masters")
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    examname = models.CharField(max_length=30)
    examscore = models.DecimalField(max_digits=5, decimal_places=2)
    fees = models.BigIntegerField()
    fees_extra = models.BooleanField(default=False)
    date_filled = models.DateField(default=timezone.now)

    def __str__(self):
        return self.fullname
