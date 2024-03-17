from django.db import models

class  Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    phone= models.CharField(max_length=15, verbose_name="Telefon Numarası")
    email = models.EmailField(verbose_name="Email Adresi")
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")

    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişim"
