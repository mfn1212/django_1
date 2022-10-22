from this import d
from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    context = {
        "meetups": meetups,
        "show_meetups":  True,
    }
    return render(request, "meetups/index.html", context=context)


def meetup_details(request, meetup_slug):

    try:
        selected_meetup = Meetup.objects.get(slug = meetup_slug)
        meetup_found = True     
        context = {
            'title': selected_meetup.title,
            'desciption': selected_meetup.desciption,
            'meetup_found':meetup_found
        }
        
    except Exception as exp :
        meetup_found = False     
        context = {
            'meetup_found':meetup_found
        }
    return render(request, "meetups/meetup_details.html", context=context)
    context = {
        'title': selected_meetup.title,
        'desciption': selected_meetup.desciption,
        'meetup_found':meetup_found
    }
    return render(request, "meetups/meetup_details.html", context=context)
