from django.contrib import admin
from .models import *


# Class Inlines

# AdminClasses
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'vehicle', 'total')


# Register your models here.
admin.site.register(Model)
admin.site.register(Vehicle)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
admin.site.register(Service)
