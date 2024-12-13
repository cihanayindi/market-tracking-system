from django.db import models

# Create your models here.

class Receipts(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='receipt_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fiş {self.id}"
    