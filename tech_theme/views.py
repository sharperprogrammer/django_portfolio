from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tech_theme/home.html')

def about(request):
    return render(request, 'tech_theme/about.html')

def projects(request):
    return render(request, 'tech_theme/projects.html')

def contact(request):
    return render(request, 'tech_theme/contact.html')
