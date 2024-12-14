from . import views
from django.urls import path

# http://127.0.0.1:8000/harcamalar/goruntule => harcamaları görüntüler

urlpatterns = [
    path("fis_ekle/", views.add_receipt, name="fis_ekle"),
    path('islemleri_goruntule/', views.show_transactions, name='islemleri_goruntule'),
]