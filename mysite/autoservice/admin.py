from django.contrib import admin
from .models import *


# Class Inlines
class OrderInLine(admin.TabularInline):
    model = OrderLine
    extra = 0


# AdminClasses
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'vehicle', 'total', 'client', 'return_due')
    inlines = [OrderInLine]


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('client', 'model', 'plate', 'vin')
    list_filter = ('client', 'model')
    search_fields = ('plate', 'vin')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_price')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('order', 'commenter', 'date_created', 'content')


# Register your models here.
admin.site.register(Model)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)