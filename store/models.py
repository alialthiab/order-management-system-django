from audioop import reverse
from pyexpat import model
from statistics import mode
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Supplier(models.Model):
    CompanyName = models.CharField(max_length=100)
    ContractName = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Fax = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)

    def __str__(self):
        return str(self.pk)



class Product(models.Model):
    ProductName = models.CharField(max_length=100)
    SupplierId = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    UnitPrice = models.FloatField( validators=[MinValueValidator(0.0),],)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('store-products',)


class Customer(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    phone = models.CharField(max_length=14, unique=True)
    
    def __str__(self):
        return str(self.pk)


class Order(models.Model):
    OrderDate = models.DateTimeField(default=timezone.now,) #adding date for only current created feilds
    OrderNumber = models.IntegerField(unique=True)
    CustomerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    TotalAmount = models.FloatField( validators=[MinValueValidator(0.0),],)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('store-orders',)
    


class OrderItem(models.Model):
    OrderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    UnitPrice = models.FloatField( validators=[MinValueValidator(0.0),],)
    Quantity = models.FloatField( validators=[MinValueValidator(0.0),],)
