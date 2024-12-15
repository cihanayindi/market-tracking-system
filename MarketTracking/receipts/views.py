from django.shortcuts import render, redirect
from .forms import ReceiptForm
from anasayfa.models import Receipts, Expenses, Products

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
    # Fiş ID'si 1 olacak
    receipt = Receipts.objects.get(id=1)  # Fişi bir kez al
    
    # 2. Ürün
    expense2 = Expenses.objects.create(
        product=Products.objects.get(id=2),  # İkinci ürün
        receipt=receipt,  # Fiş 1
        quantity=5,
        price_per_piece=15.0,
        price=75.0
    )
    
    # 3. Ürün
    expense3 = Expenses.objects.create(
        product=Products.objects.get(id=3),  # Üçüncü ürün
        receipt=receipt,  # Fiş 1
        quantity=2,
        price_per_piece=20.0,
        price=40.0
    )
    
    # 4. Ürün
    expense4 = Expenses.objects.create(
        product=Products.objects.get(id=2),  # Dördüncü ürün
        receipt=receipt,  # Fiş 1
        quantity=7,
        price_per_piece=8.0,
        price=56.0
    )
    
    # 5. Ürün
    expense5 = Expenses.objects.create(
        product=Products.objects.get(id=3),  # Beşinci ürün
        receipt=receipt,  # Fiş 1
        quantity=10,
        price_per_piece=12.0,
        price=120.0
    )
    
    return render(request, "receipts/islemleri_goruntule.html")
