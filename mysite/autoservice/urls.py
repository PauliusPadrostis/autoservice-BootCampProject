from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .models import *

urlpatterns = [
    path('', views.index, name='index'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/<int:vehicle_id>', views.vehicle, name='vehicle'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>', views.service, name='service'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('search/', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('myorders/', views.VehiclesByClientListView.as_view(), name='my_orders'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('myorders/new', views.OrderByUserCreateView.as_view(), name = 'new_user_order'),
    path('order/<int:pk>/update', views.OrderByUserUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete', views.OrderByUserDeleteView.as_view(), name='order_delete'),
]