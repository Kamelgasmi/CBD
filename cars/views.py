from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,  PageNotAnInteger, Paginator
# Create your views here.,
def cars(request):
    car = Car.objects.all()
    # paginator = Paginator(car, 3)
    # page = request.GET.get('page')
    # paged_car = paginator.get_page(page)
    name_search = Car.objects.values_list('name', flat=True).distinct() #**********************************recherche par nom

    data = {
        'car':car,
        'name_search': name_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car':single_car,
    }
    return render(request, 'cars/car-detail.html', data)

def search(request):
    car = Car.objects.order_by('-created_date')
    name_search = Car.objects.values_list('name', flat=True).distinct() #**********************************recherche par nom
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            car = car.filter(name__icontains=keyword)
        
    # if 'name' in request.GET:
    #     name = request.GET['name']
    #     if name:
    #         car = car.filter(name__iexact=name)
            
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            car = car.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'car':car,
        'name_search': name_search,
    }
    return render(request, 'cars/search.html', data)