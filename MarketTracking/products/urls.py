from . import views
from django.urls import path

# http://127.0.0.1:8000/harcamalar/goruntule => harcamaları görüntüler

urlpatterns = [
    path("goruntule/", views.show_products, name="urunleri_goruntule")
]