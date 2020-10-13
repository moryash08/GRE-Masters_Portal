from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'GRE_Website/home.html', {'title': 'Home'})


def register(request):
    return render(request, 'GRE_Website/register.html', {'title': 'Registration'})


def login(request):
    return render(request, 'GRE_Website/login.html', {'title': 'Login'})


def about(request):
    return render(request, 'GRE_Website/about.html', {'title': 'About'})
