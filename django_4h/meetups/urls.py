from django.urls import path
from .import views


urlpatterns = [
    path('index/', views.index , name = 'home-page'),
    path('index/<slug:meetup_slug>', views.meetup_details , name = 'meetup_details'),

]
