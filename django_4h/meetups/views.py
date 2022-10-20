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

    meetup = {
        "title": "first meetup",
        "address": "Paris",
        "slug": "a-first-meetup",
    }
    context = {
        'meetup': meetup,
        'slug': meetup_slug,
    }
    return render(request, "meetups/meetup_details.html", context=context)
