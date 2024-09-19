from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class  Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("Ad Soyad"))
    phone= models.CharField(max_length=15, verbose_name=_("Telefon Numarası"))
    email = models.EmailField(verbose_name=_("Email Adresi"))
    message = models.TextField(verbose_name=_("Mesaj"))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Oluşturulma Tarihi"))

    class Meta:
        verbose_name = _("İletişim")
        verbose_name_plural = _("İletişim")


class About(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    content = RichTextField(verbose_name=_("İçerik"), config_name='extends')

    class Meta:
        verbose_name = _("Hakkımızda")
        verbose_name_plural = _("Hakkımızda")

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Hizmet Adı"))
    content = RichTextField(verbose_name=_("İçerik"), config_name='extends')
    slug = models.SlugField(max_length=200, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Hizmetlerim")
        verbose_name_plural = _("Hizmetlerim")

class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    image = models.ImageField(upload_to='slider/', verbose_name=_("Resim"))


    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Kategori Adı"))
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Kategori")
        verbose_name_plural = _("Kategoriler")


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    image = models.ImageField(upload_to='blog/', verbose_name=_("Resim"))
    content = RichTextField(verbose_name=_("İçerik"), config_name='extends')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Oluşturulma Tarihi"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("GÜncelleme Tarihi"))
    slug = models.SlugField(max_length=200, unique=True ,blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

class Settings(models.Model):
    logo_1 = models.ImageField(upload_to='dimg/', null=True ,verbose_name="Logo")
    logo_2 = models.ImageField(upload_to='dimg/', null=True ,verbose_name="Logo 2")
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    dest = models.TextField(verbose_name="Açıklama")
    keywords = models.CharField(max_length=255, verbose_name=_("Anahtar Kelimeler"))
    phone = models.CharField(max_length=15, verbose_name=_("Telefon Numarası"))
    email = models.EmailField(verbose_name=_("Email Adresi"))
    city = models.CharField(max_length=50, verbose_name=_("İl"))
    district = models.CharField(max_length=200, verbose_name=_("İlçe"))
    address = models.TextField(verbose_name=_("Adres"))
    facebook = models.URLField(verbose_name="Facebook")
    twitter = models.URLField(verbose_name="Twitter")
    instagram = models.URLField(verbose_name="Instagram")
    linkedin = models.URLField(verbose_name="Linkedin")
    youtube = models.URLField(verbose_name="Youtube")

    class Meta:
        verbose_name = _("Ayarlar")
        verbose_name_plural = _("Ayarlar")