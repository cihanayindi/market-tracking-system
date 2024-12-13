from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import ReceiptForm

# Create your views here.

def index(request):
    return render(request, "anasayfa/index.html")

def add_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else: 
        form = ReceiptForm()

    return render(request, "anasayfa/fis_ekle.html", {'form': form})