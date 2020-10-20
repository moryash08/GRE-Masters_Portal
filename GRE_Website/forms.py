from . import views
from .models import Student
from django import forms
from django.utils.translation import ugettext_lazy as _
from django_countries import countries
import floppyforms.widgets as floppy_widgets

COUNTRY_CHOICES = tuple(countries)
collegeList = Student.objects.all().values_list('collegename', flat=True)
universityList = Student.objects.all().values_list('university', flat=True)


class UniversityForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ('date_filled',)
        labels = {
            'fullname': _('Full Name')
        }
        widgets = {
            'fullname': forms.TextInput(
                attrs={'placeholder': 'Full name', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'collegename': floppy_widgets.Input(
                datalist=collegeList,
                attrs={'placeholder': 'College Name', 'class': 'form-control'}),
            'country': forms.Select(
                choices=COUNTRY_CHOICES,
                attrs={'placeholder': 'Select Country', 'class': 'form-control'}),
            'university': floppy_widgets.Input(
                datalist=universityList,
                attrs={'placeholder': 'University Name', 'class': 'form-control'}),
            'cgpa': forms.TextInput(
                attrs={'placeholder': 'Current CGPA', 'class': 'form-control'}),
            'examname': forms.TextInput(
                attrs={'placeholder': 'Exam Name', 'class': 'form-control'}),
            'examscore': forms.TextInput(
                attrs={'placeholder': 'Score', 'class': 'form-control'}),
            'fees': forms.TextInput(
                attrs={'placeholder': 'Fees', 'class': 'form-control'})
        }
