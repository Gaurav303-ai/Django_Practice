# HttpResponse is used to return simple text 
# response to the browser, while render() is used to return an HTML template with context data. 
# Render is a shortcut that internally uses HttpResponse.
from django.shortcuts import render
from django.http import HttpResponse
from student.models import Profile
def home(request):
    return HttpResponse("Hello Gaurav,")
# Create your views here.
def start(request):
    coursename = {'cname': 'python'}
    return render(request,'student/home.html', context=coursename)
def learn_Django(req):
    return render(req,'student/base.html')
def all_data(req):
    all_student = Profile.objects.all()
    print(all_student)
    return render(req,'student/all.html',{'student': all_student})
