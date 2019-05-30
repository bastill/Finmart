from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/index.html', {})


def about_us(request):
    return render(request, 'core/about.html', {})



def events(request):
    return render(request, 'core/events.html', {})


def contact_us(request):
    return render(request, '', {})


def auth(request):
    return render(request, '', {})





