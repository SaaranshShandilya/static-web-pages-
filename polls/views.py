from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html",{'name':'Saaransh'})

def add(request):
    val1=int(request.POST['n1'])
    val2=int(request.POST['n2'])
    c = val1 + val2
    return render(request, "result.html",{'b':c})

# Create your views here.
