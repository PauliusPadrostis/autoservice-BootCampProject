from django.db import models


# Create your models here.
class Model(models.Model):
    make = models.CharField(verbose_name='Make', max_length=50, null=True, blank=True)
    model = models.CharField(verbose_name='Model', max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Make/Model: {self.make} - {self.model}"


class Vehicle(models.Model):
    model = models.ForeignKey(to='Model', on_delete=models.CASCADE)
    plate = models.CharField(verbose_name='Plate number', max_length=50, null=True, blank=True)
    vin = models.CharField(verbose_name='VIN number', max_length=50, null=True, blank=True)
    client = models.CharField(verbose_name='VIN number', max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.model}({self.plate}). VIN: {self.vin}. Owner: {self.client}"


class Order(models.Model):
    date = models.DateField(verbose_name='Date', auto_now=True, null=True, blank=True)
    vehicle = models.ForeignKey(to='Vehicle', on_delete=models.CASCADE)
    total = models.FloatField(verbose_name='Total', null=True, blank=True)

    def __str__(self):
        return f"({self.date}) - {self.vehicle}. Order price: {self.total}"


class OrderLine(models.Model):
    service = models.ForeignKey(to='Service', on_delete=models.CASCADE)
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE)
    amount = models.FloatField(verbose_name='Amount', null=True, blank=True)
    service_price = models.FloatField(verbose_name='Service price', null=True, blank=True)

    def __str__(self):
        return f"{self.service} ({self.amount}) - {self.service_price}"


class Service(models.Model):
    name = models.CharField(verbose_name='Service name', max_length=500, null=True, blank=True)
    service_price = models.FloatField(verbose_name='Service price', null=True, blank=True)

    def __str__(self):
        return f"Service: {self.name}. Price: {self.service_price}"
