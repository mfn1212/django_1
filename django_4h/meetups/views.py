from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    meetups = [
        {
            "title": "first meetup",
            "address": "Paris",
            "slug": "a-first-meetup",
        },
        {
            "title": "second meetup",
            "address": "New York",
            "slug": "a-secend-meetup",
        },
    ]
    context = {
        "meetups": meetups,
        "show_meetups":  True,
    }
    return render(request, "meetups/index.html", context=context)
