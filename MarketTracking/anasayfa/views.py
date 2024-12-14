from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Products, Receipts, Expenses

# Create your views here.

def index(request):
    return render(request, "anasayfa/index.html")

def show_transactions(request):
    # products = [
    #     {'name': 'Domates', 'type': 'vegetable', 'unit_type': 'kg'},  # Domates, sebze, kilogram ile satılacak
    #     {'name': 'Elma', 'type': 'fruit', 'unit_type': 'piece'},  # Elma, meyve, adet ile satılacak
    #     {'name': 'Yumuşatıcı', 'type': 'cleaning', 'unit_type': 'piece'},  # Yumuşatıcı, temizlik ürünü, adet ile satılacak
    # ]

    # # Ürünleri sisteme ekleyelim
    # for product in products:
    #     new_product = Products(
    #         name=product['name'],
    #         type=product['type'],
    #         unit_type=product['unit_type'],
    #         price=None  # Fiyatı başlangıçta boş bırakıyoruz
    #     )
    #     new_product.save()
    return render(request, "anasayfa/islemleri_goruntule.html")

def show_products(request):
    return render(request, "anasayfa/urunleri_goruntule.html")