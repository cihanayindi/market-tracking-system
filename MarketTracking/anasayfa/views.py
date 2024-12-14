from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Products, Receipts, Expenses

# Create your views here.

def index(request):
    return render(request, "anasayfa/index.html")
