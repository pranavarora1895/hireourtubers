from django.shortcuts import render
from .models import Slider, Team, About
from youtubers.models import Youtuber
from contacttubers.models import Contactinfo

# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    onboard_youtubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'onboard_youtubers': onboard_youtubers,
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    teams = Team.objects.all()
    about = About.objects.all()[0]
    data = {
        'teams': teams,
        'about': about,
    }
    return render(request, 'webpages/about.html', data)


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    contact_info = Contactinfo.objects.all()[0]
    data = {
        'contact_info': contact_info
    }
    return render(request, 'webpages/contact.html', data)
