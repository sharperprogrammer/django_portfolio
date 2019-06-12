from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tech_home'),
    path('about', views.about, name='tech_about'),
    path('projects', views.projects, name='tech_projects'),
    path('contact', views.contact, name='tech_contact'),
]
