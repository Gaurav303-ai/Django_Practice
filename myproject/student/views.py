from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("Hello Gaurav,")
# Create your views here.
def start(request):
    coursename = {'cname': 'python'}
    return render(request,'student/home.html', context=coursename)
def learn_Django(req):
    return render(req,'student/django.html')