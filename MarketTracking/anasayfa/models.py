from django.db import models

# Create your models here.

class Receipts(models.Model):
    """
    Bu tablo sisteme harcamaları kaydetmek için kullanılacak tablodaki sütunlar şunları ifade ediyor:
    
    id = klasik id sistemi, primary key ve otomatik artar
    image = fişin resmini tutan sütun
    uploaded_at = bu fişin eklendiği tarihi belirtir
    """
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='receipt_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fiş {self.id}"
    
class Products(models.Model):
    """
    Bu tablo sisteme ürünleri kaydetmek için kullanılacak tablodaki sütunlar şunları ifade ediyor:

    id = klasik id sistemi, primary key ve otomatik artar
    name = ürünün adını saklayan sütun, text olarak tutulur, aynı üründen başka olamaz bu yüzden unique olmalıdır
    type = ürünün tipini belirtir, bu arada duruma göre tipler arttırılabilir ama şu anda şu tipler olacak -> meyve, sebze, temizlik...
    price = ürünün sistemde son bilinen fiyatını saklar
    unit_type = ürünün hangi birimle satıldığını belirler, örneğin: 'adet', 'kg'
    uploaded_at = ürünün sisteme hangi tarihte eklendiğini tutar
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)  # Ürün adı, unique olacak
    type = models.CharField(max_length=100, choices=[  # Ürün türü, enum tarzı
        ('fruit', 'Meyve'),
        ('vegetable', 'Sebze'),
        ('cleaning', 'Temizlik'),
        ('others', 'Diğer')
    ], null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Ürün fiyatı
    unit_type = models.CharField(max_length=10, choices=[  # Satış birimi (adet, kg vb.)
        ('piece', 'Adet'),
        ('kg', 'Kilogram')
    ], null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Ürünün sisteme eklendiği tarih

    def __str__(self):
        return f"{self.name} ({self.type})"

class Expenses(models.Model):
    """
    Bu tablo sisteme harcamaları kaydetmek için kullanılacak tablodaki sütunlar şunları ifade ediyor:
    
    id = klasik id sistemi, primary key ve otomatik artar
    product = ürünün id'sini belirtir, Products modelinden foreign key olmalıdır.
    receipt = fişin id'sini belirtir Receipts modelinden foreign key olmalıdır.
    quantity = üründen kaç adet veya kaç kilogram alındığını belirtir. Ürün türüne göre 'adet' ya da 'kilo' cinsinden değer alabilir.
    price_per_piece = ürünün adet veya kilo başı fiyatı
    price = toplam fiyat
    uploaded_at = bu harcamanın eklendiği tarihi belirtir
    """
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)  # İlgili ürün
    receipt = models.ForeignKey(Receipts, on_delete=models.CASCADE)  # İlgili fiş
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Ürün adedi veya kilosu
    price_per_piece = models.DecimalField(max_digits=10, decimal_places=2)  # Adet veya kilo başı fiyat
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Toplam fiyat (quantity * price_per_piece)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Harcamanın eklendiği tarih

    def __str__(self):
        return f"Harcanan {self.product.name} için {self.quantity} adet / kg"

    def save(self, *args, **kwargs):
        # Toplam fiyatı hesaplayalım
        self.price = self.quantity * self.price_per_piece
        super().save(*args, **kwargs)


