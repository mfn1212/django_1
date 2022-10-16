from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    meetups = [
        {
            "title": "first meetup",
            "grade": 12,
        },
        {
            "title": "second meetup",
            "grade": 4,
        },
    ]
    context = {
        "meetups": meetups,
        "show_meetups":  True,
    }
    return render(request, "meetups/index.html", context=context)
