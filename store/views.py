from django.shortcuts import render, get_object_or_404
from . models import *
from django.http import JsonResponse
import json
import datetime
from . utils import cookieCart, guestOrder
import logging


logger = logging.getLogger(__name__)


def store(request):
    logger.info('Calling httpbin')
    if request.user.is_authenticated:
        customer = request.user.customer  
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:  
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    logger.info('Recieved the response')
    return render(request, 'store/store.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)


def search_products(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        results = Product.objects.filter(name__icontains=searched)
        context = {'results': results, 'searched': searched}
        return render(request, 'store/search_products.html', context)
    else:
        return render(request, 'store/search_products.html', {})



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer  
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items  
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    context = {'items':items, 'order':order, 'cartItems': cartItems} 
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer  
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']  
    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)  

  
def updateItem(request):  
    data = json.loads(request.body)
    productId = data['productId']  
    action = data['action']
    print('Action:', action)  
    print('productId:', productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)  


def processOrder(request):
    transaction_id =  datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
    else:
        order, created = guestOrder(request, data)
        total = float(data['form']['total'])
        order.transation_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True

        order.save()  
              
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
                )
    return JsonResponse('payment submitted..', safe=False)




