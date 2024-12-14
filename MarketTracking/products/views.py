from django.shortcuts import render
from anasayfa.models import Products
# Create your views here.

def show_products(request):
    product_list = Products.objects.all()

    return render(request, "products/goruntule.html", {'product_list': product_list})