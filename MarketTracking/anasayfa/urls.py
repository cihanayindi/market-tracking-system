from . import views
from django.urls import path

# http://127.0.0.1:8000/ => index

urlpatterns = [
    path("", views.index, name="index"),
    path('fis_ekle/', views.add_receipt, name='fis_ekle'),
]