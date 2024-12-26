from urllib import request
from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart , CartDetail , Order , OrderDetail , Coupon
from django.shortcuts import get_object_or_404
from django.utils.timezone import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required(login_url='/accounts/login/')
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user,status='inprogress')
        
        cart_detail,created = CartDetail.objects.get_or_create(
            cart = cart , 
            product = product
        )
        cart_detail.quantity= int(quantity)
        cart_detail.price = product.price
        cart_detail.total = int(quantity) * product.price 
        cart_detail.save()
        
        
        
      
@login_required(login_url='/accounts/login/')
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'orders/orders.html',{'orders':orders})


@login_required(login_url='/accounts/login/')
def checkout(request):
    cart = Cart.objects.get(user=request.user,status='inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    
    today_date = datetime.today().date()
    delivery_cost = 50
    
    if request.method == 'POST':
        code = request.POST['coupon_code']
        coupon_code = get_object_or_404(Coupon,code=code)
        if coupon_code and coupon_code.quantity > 0:
            if today_date >= coupon_code.from_date and today_date <= coupon_code.to_date:
                code_value = cart.get_total() /100 * coupon_code.value
                total = cart.get_total() - code_value
                total = total + delivery_cost
                
                
                html = render_to_string('include/summery.html',{'sub_total':cart.get_total(),'total':total,'delivery_cost':delivery_cost,'code_value':code_value, 'request':request})
                return JsonResponse({'result':html})        
    
    else:
        code_value = 0
        total = round(cart.get_total() + delivery_cost,2)
        return render(request,'orders/checkout.html',{'cart':cart ,'total':total,'sub_total':cart.get_total(),'delivery_cost':delivery_cost,'code_value':code_value, 'cart_detail':cart_detail})