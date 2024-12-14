# forms.py
from django import forms
from anasayfa.models import Receipts

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipts
        fields = ['image']
