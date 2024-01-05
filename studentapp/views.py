from django.shortcuts import render
from .models import Student

# Create your views here.


def allstudents(req):
    studentdata = Student.objects.all()
    context = {"studentdata": studentdata}
    return render(req, "allstudents.html", context)


def studentdetails(req, studentid):
    studentrecord = Student.objects.get(studentid=studentid)
    context = {"studentrecord": studentrecord}
    return render(req, "studentdetails.html", context)
