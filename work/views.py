from django.shortcuts import render

def home(request):
    return render(request, 'work/home.html')

