from django.shortcuts import render
from .models import Team
from cars.models import Car

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured = True)
    all_cars = Car.objects.order_by('-created_date')
    # search_field = Car.objects.values('name')
    name_search = Car.objects.values_list('name', flat=True).distinct() #**********************************recherche par nom
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        # 'search_field': search_field,
        'name_search': name_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')