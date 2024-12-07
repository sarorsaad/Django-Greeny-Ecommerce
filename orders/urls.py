from django.urls import path
from .views import add_to_cart , order_list , checkout

app_name='orders'

urlpatterns = [
    path('' , order_list, name='order_list'),
    path('checkout' , checkout, name='checkout'),
    path('add-to-cart' , add_to_cart,name='add_to_cart'),

]

