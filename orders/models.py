from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utils.generate_code import generate_code
from products.models import Product




STATUS_CHOICES = (
    ('inprogress' , 'inprogress'),
    ('completed','completed'),
)

class Cart(models.Model):
    code = models.CharField(max_length=8 , default=generate_code)
    user = models.ForeignKey(User,related_name='user_cart',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

    def __str__(self):
        return self.code
    
    def get_total(self):
        total = 0
        for product in self.cart_detail.all():
            total += product.total
        return total



class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL , null=True,blank=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    total = models.FloatField(default=0)
    
    
    def __str__(self):
        return str(self.cart)



STATUS_CHOICES = (
    ('receieved' , 'receieved'),
    ('processed','processed'),
    ('shiped','shiped'),
    ('delivered','delivered'),
)

class Order(models.Model):
    code = models.CharField(max_length=8 , default=generate_code)
    user = models.ForeignKey(User,related_name='user_order',on_delete=models.SET_NULL,null=True,blank=True)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

    def __str__(self):
        return self.code



class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL , null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    
    
    def __str__(self):
        return str(self.order)
    
    
    
class Coupon(models.Model):
    code = models.CharField(max_length=20)
    quantity = models.IntegerField()
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    value = models.FloatField()
    is_valid = models.BooleanField(default=True)
    
    def __str__(self):
        return self.code