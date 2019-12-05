from django.shortcuts import render
from accounts.models import Profile


def home(request):
    return render(request, 'work/home.html')

def start(request):
    return render(request, 'work/start-work.html')

def working(request):
    profile = Profile.objects.all()

    return render(request, 'work/working.html', {
        'profile' : profile,

    })
