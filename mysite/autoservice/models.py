from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.urls import reverse
from tinymce.models import HTMLField
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


class Model(models.Model):
    make = models.CharField(verbose_name='Make', max_length=50, null=True, blank=True)
    model = models.CharField(verbose_name='Model', max_length=50, null=True, blank=True)
    desc = HTMLField(null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model}"

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Vehicle(models.Model):
    model = models.ForeignKey(to='Model', on_delete=models.CASCADE)
    plate = models.CharField(verbose_name='Plate number', max_length=50, null=True, blank=True)
    vin = models.CharField(verbose_name='VIN number', max_length=50, null=True, blank=True)
    client = models.CharField(verbose_name='Client', max_length=50, null=True, blank=True)
    cover = models.ImageField('Cover', upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f"{self.model}({self.plate}). VIN: {self.vin}. Owner: {self.client}"

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class Order(models.Model):
    date = models.DateField(verbose_name='Date', auto_now=True, null=True, blank=True)
    vehicle = models.ForeignKey(to='Vehicle', on_delete=models.CASCADE)
    total = models.FloatField(verbose_name='Total', null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    return_due = models.DateField(verbose_name="Return due", null=True, blank=True)

    ORDER_STATUS = (
        ('r', 'Received'),
        ('c', 'Confirmed'),
        ('ip', 'In-progress'),
        ('co', 'Complete'),
    )

    order_status = models.CharField(max_length=2, choices=ORDER_STATUS, blank=True, default='r', help_text='Order status')
    def __str__(self):
        return f"({self.date}) - {self.vehicle}. Order price: {self.total}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def is_overdue(self):
        if self.return_due and date.today() > self.return_due:
            return True
        return False

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.pk)])


class OrderLine(models.Model):
    service = models.ForeignKey(to='Service', on_delete=models.CASCADE)
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE)
    amount = models.FloatField(verbose_name='Amount', null=True, blank=True)
    service_price = models.FloatField(verbose_name='Service price', null=True, blank=True)

    def __str__(self):
        return f"{self.service} ({self.amount}) - {self.service_price}"

    class Meta:
        verbose_name = 'OrderLine'
        verbose_name_plural = 'OrderLines'


class Service(models.Model):
    name = models.CharField(verbose_name='Service name', max_length=500, null=True, blank=True)
    service_price = models.FloatField(verbose_name='Service price', null=True, blank=True)

    def __str__(self):
        return f"Service: {self.name}. Price: {self.service_price}"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Comment(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    content = models.TextField('Comment', max_length=1000)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-date_created']
