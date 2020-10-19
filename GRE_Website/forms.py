from . import views
from .models import Student
from django import forms
from django.utils.translation import ugettext_lazy as _


class UniversityForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname', 'email', 'collegename', 'country', 'university', 'cgpa', 'examname', 'examscore', 'fees']
        labels = {
            'fullname': _('Full Name')
        }
        widgets = {
            'fullname': forms.TextInput(
                attrs={'placeholder': 'Full name', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'collegename': forms.TextInput(
                attrs={'placeholder': 'College Name', 'class': 'form-control'}),
            'country': forms.TextInput(
                attrs={'class': 'form-control'}),
            'university': forms.TextInput(
                attrs={'class': 'form-control'}),
            'cgpa': forms.TextInput(
                attrs={'placeholder': 'Current CGPA', 'class': 'form-control'}),
            'examname': forms.TextInput(
                attrs={'class': 'form-control'}),
            'examscore': forms.TextInput(
                attrs={'placeholder': 'Score', 'class': 'form-control'}),
            'fees': forms.TextInput(
                attrs={'placeholder': 'Fees', 'class': 'form-control'})
        }
