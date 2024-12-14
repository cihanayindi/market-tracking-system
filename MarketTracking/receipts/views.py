from django.shortcuts import render, redirect
from .forms import ReceiptForm

# Create your views here.
def add_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else: 
        form = ReceiptForm()

    return render(request, "receipts/fis_ekle.html", {'form': form})

def show_transactions(request):
    return render(request, "receipts/islemleri_goruntule.html")