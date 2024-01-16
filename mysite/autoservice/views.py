from django.shortcuts import render
from .models import *

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