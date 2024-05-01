from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    items = Product.objects.all()
    context = {
        'items':items,
        
    }
    
    return render(request, "shop/index.html",context)


def indexItem(request, product_id):
    item = Product.objects.get(id = product_id)
    context = {
        'item':item
    }
    return render(request, "shop/detail.html",context=context)

def addItem(request):
    if request.method == "POST":
       name =  request.POST.get("name")
       price =  request.POST.get("price")
       description =  request.POST.get("description")
       image = request.FILES['upload']
       item = Product(name = name, price = price, description = description, image = image)
       item.save()
    return render(request, "shop/additem.html")
    



