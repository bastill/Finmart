from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.home, name='index'),
    path('about-us', views.about_us, name='aboutus'),
    path('events', views.events, name='event'),
    path('contactus', views.contact_us, name='contactus'),
]