from . import views
from .models import Student
from django import forms
from django.utils.translation import ugettext_lazy as _
from django_countries import countries
import floppyforms.widgets as floppy_widgets

COUNTRY_CHOICES = tuple(countries)
collegeList = Student.objects.all().values_list('collegename', flat=True).distinct
universityList = Student.objects.all().values_list('university', flat=True).distinct


class UniversityForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ('date_filled',)
        labels = {
            'fullname': _('Full Name :'),
            'email': _('Email Address :'),
            'collegename': _('College Name :'),
            'country': _('Country :'),
            'university': _('University Name :'),
            'courses': _('Course Name :'),
            'cgpa': _('CGPA :'),
            'examname': _('Exam Name :'),
            'examscore': _('Exam Score :'),
            'fees': _('Max Affordable Fees :'),
        }
        widgets = {
            'fullname': forms.TextInput(
                attrs={'placeholder': 'Full name', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'collegename': floppy_widgets.Input(
                datalist=collegeList,
                attrs={'placeholder': 'Your College Name', 'class': 'form-control'}),
            'country': forms.Select(
                choices=COUNTRY_CHOICES,
                attrs={'placeholder': 'Your Country Choice', 'class': 'form-control'}),
            'university': floppy_widgets.Input(
                datalist=universityList,
                attrs={'placeholder': 'Your University Choice', 'class': 'form-control'}),
            'courses': floppy_widgets.Input(
                attrs={'placeholder': 'Your Course Choice', 'class': 'form-control'}),
            'cgpa': forms.TextInput(
                attrs={'placeholder': 'Current CGPA', 'class': 'form-control'}),
            'examname': forms.TextInput(
                attrs={'placeholder': 'Exam Name', 'class': 'form-control'}),
            'examscore': forms.TextInput(
                attrs={'placeholder': 'Score', 'class': 'form-control'}),
            'fees': forms.TextInput(
                attrs={'placeholder': 'Fees in INR', 'class': 'form-control'}),
        }
        help_texts = {
            'fullname': 'First Name + Last Name',
            'email': 'E.g. abc@company.com',
            'collegename': 'College from where you Graduated',
            'country': 'Your Destination Country',
            'university': 'Your preferred University Name',
            'courses': 'Your choice of Course',
            'cgpa': 'Your Current/Final CGPA',
            'examname': 'Examination Through which you got into Current College',
            'examscore': 'Score Achieved in above Exam',
            'fees': 'Annual Maximum Affordable Fees',
        }
