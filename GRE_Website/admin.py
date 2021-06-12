from django.contrib import admin
from .models import Country, University, Courses, Student

# Register your models here.
admin.site.register(Country)
admin.site.register(University)
admin.site.register(Courses)
admin.site.register(Student)
