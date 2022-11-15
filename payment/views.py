from django.shortcuts import render, redirect
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    if request.method == 'POST':
        product_name = request.POST.get('name')
        product_price = int(request.POST.get('price'))
        product_quantity = int(request.POST.get('quantity'))
        total_price = product_price * product_quantity
        mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='arbre6373f11aa43c5', sslc_store_pass='arbre6373f11aa43c5@ssl')
        mypayment.set_urls(success_url='http://127.0.0.1:8000/success/', fail_url='http://127.0.0.1:8000/fail/', cancel_url='http://127.0.0.1:8000/cancel/', ipn_url='http://127.0.0.1:8000/')
        mypayment.set_product_integration(total_amount=Decimal(total_price), currency='BDT', product_category='clothing', product_name=product_name, num_of_item=1, shipping_method='YES', product_profile='None')
        mypayment.set_customer_info(name='sabbir ahemd', email='sabbirdev45@email.com', address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')
        mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')
        response_data = mypayment.init_payment()
        print(response_data)

        return redirect(response_data['GatewayPageURL'])

        redirect('payment:home')
    return render(request, 'index.html')


@csrf_exempt
def success(request):
    if request.method == "post" or request.method == "POST":
        data = request.POST
        print(data)
    return render(request, "success.html")

@csrf_exempt
def fail(request):
    if request.method == "post" or request.method == "POST":
        data = request.POST
        print(data)
    return render(request, "fail.html")


@csrf_exempt
def cancel(request):
    if request.method == "post" or request.method == "POST":
        data = request.POST
        print(data)
    return render(request, "cancel.html")
