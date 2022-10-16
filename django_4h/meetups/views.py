from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request) :
    meetups = [
        {"title" : "first meetup"},
        {"title" : "second meetup"},
    ]
    context = {
        "meetups" : meetups
    }
    return render(request,"meetups/index.html",context=context) 

