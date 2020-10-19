from django.shortcuts import render, redirect
from .forms import UniversityForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'GRE_Website/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'GRE_Website/about.html', {'title': 'About'})


def universityform(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Form Filled Successfully')
            return redirect('GRE_Website-home')

    else:
        form = UniversityForm()
    return render(request, 'GRE_Website/universityform.html', {'title': 'University Form', 'form': form})
