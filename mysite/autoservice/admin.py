from django.contrib import admin
from .models import *


# Class Inlines
class OrderInLine(admin.TabularInline):
    model = OrderLine
    extra = 0


# AdminClasses
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'vehicle', 'total')
    inlines = [OrderInLine]

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('client', 'model', 'plate', 'vin')


# Register your models here.
admin.site.register(Model)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
admin.site.register(Service)
