from django.shortcuts import render,HttpResponse
from .models import Product
from django.http import JsonResponse
# Create your views here.


# Create your views here.
def index(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        product = Product(product_name = product_name,price = price,quantity = quantity)
        product.save()
    products = Product.objects.all().order_by("-id")
    return render(request,'index.html',{'products':products})

def update_data(request):
    id = request.POST.get('id','')
    type = request.POST.get('type','')
    value = request.POST.get('value','')
    #Get Record
    e=Product.objects.get(id=id)
    if type=='product_name' and value!='':
        e.product_name =value
    elif type=='price' and value!='':
        e.price=value
    elif type=='quantity' and value!='':
        e.quantity=value
    else:
        print('Something went Wrong')
    e.save()
    return JsonResponse({"success": "Work Fine"})