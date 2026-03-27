# HttpResponse is used to return simple text 
# response to the browser, while render() is used to return an HTML template with context data. 
# Render is a shortcut that internally uses HttpResponse.
from django.shortcuts import render
from django.http import HttpResponse
from student.models import Profile
from student.forms import Registration, detail, Address
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
def reg(req):
    fm = Registration() #we can use inside () like auto_id='wrte her to customise id', by default it set to (id_%s)
                        #know about label_suffix=' '
                        #know about  initial={'email': 'example@.com, 'roll': '2155'}
                        # use field_order={'write order in which you want your   forms look like'fo ex 'email', 'city', roll..}
    return render(req, 'student/registration.html',{'form':fm}) 
def address(req):
    ad = Address()
    ln = detail()
    return render(req,'student/login.html', {'login':ad, 'details':ln})