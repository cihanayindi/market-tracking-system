from django.shortcuts import render

# Create your views here.

def show_products(request):
    return render(request, "products/goruntule.html")