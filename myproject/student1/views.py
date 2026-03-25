from django.shortcuts import render
def django (req):
    return render(req, 'student1/django.html')

def python (req):
    return render(req, 'student1/python.html')
# Create your views here.
