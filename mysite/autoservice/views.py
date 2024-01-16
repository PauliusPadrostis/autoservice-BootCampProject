from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
from django.http import HttpResponse


# Services amount, orders done, vehicle amount
def index(request):

    service_num = Service.objects.all().count()
    orders_done = Order.objects.filter(order_status__exact='co').count()
    vehicle_amount = Vehicle.objects.count()

    context = {
        'service_num': service_num,
        'orders_done': orders_done,
        'vehicle_amount': vehicle_amount,
    }

    return render(request, 'index.html', context=context)


def vehicles(request):
    paginator = Paginator(Vehicle.objects.all(), 8)
    page_number = request.GET.get('page')
    paged_vehicles = paginator.get_page(page_number)
    context = {
        'vehicles': paged_vehicles
    }
    return render(request, 'vehicles.html', context=context)


def vehicle(request, vehicle_id):
    single_vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'vehicle.html', {'vehicle': single_vehicle,})


def services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services.html', context=context)


def service(request, service_id):
    single_service = get_object_or_404(Service, pk=service_id)
    return render(request, 'service.html', {'service': single_service,})


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 2
    template_name = 'order_list.html'


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'


def search(request):
    query = request.GET.get('query')
    search_results = Vehicle.objects.filter(Q(client__icontains=query) | Q(model__make__icontains=query) | Q(model__model__icontains=query) | Q(plate__icontains=query)| Q(vin__icontains=query))
    return render(request, 'search.html', {'vehicles': search_results, 'query': query})


