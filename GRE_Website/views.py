from django.shortcuts import render, redirect
from .forms import UniversityForm
from django.contrib import messages
from .models import Country, University, Courses
from pymongo import MongoClient
from django.shortcuts import render
from .getcoursedetails import CourseDetails
import pprint

try:
    client = MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.7x4oe.mongodb.net/test")
    db = client['sample_training']
    courseCollection = db['college']
    uniCollection = db['country_unis']

except Exception as e:
    print("Error in MongoDB")


# universityList = Student.objects.all().values_list('university', flat=True).distinct
# courseNameList = list(db.college.find_one({'name': 'cornell'})['courses'].keys())


# Create your views here.
def home(request):
    return render(request, 'GRE_Website/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'GRE_Website/about.html', {'title': 'About'})


def universityform(request):
    # country_code = request.POST.get('country')
    # if country_code == "United States of America":
    #     country_code = "US"
    # universities = db.country_unis.find_one({'country_code': country_code})
    # pprint.pprint(universities.unis)
    # university_name = request.POST.get('university')
    # courses = db.college.find_one({'courses': university_name})
    # pprint.pprint(courses)
    #
    # context = {
    #     'university': universities,
    #     'courses': courses,
    # }

    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Form Filled Successfully!')
            return redirect('course-details')

    else:
        form = UniversityForm()
    return render(request, 'GRE_Website/universityform.html',
                  {'title': 'University Form',
                   'form': form})


def coursedetails(request):
    About, Expenses, Exams = CourseDetails.getcoursedetails(
        "https://studyabroad.shiksha.com/usa/universities/harvard-university/master-of-science-in-data-science")
    return render(request, 'GRE_Website/courseDetails.html', {'About': About, 'Expenses': Expenses, 'Exams': Exams})
