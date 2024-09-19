from django.contrib import admin
from .models import Contact, About, Service, Slider, Category, Blog, Settings
from modeltranslation.admin import TranslationAdmin
from ckeditor.widgets import CKEditorWidget
from .admin_mixins import CommonMedia
from django.utils.translation import gettext_lazy as _


class BaseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'message')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('full_name', 'phone', 'email', 'message')
        }),
        ('Additional Info', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    verbose_name = "İletişim" 


@admin.register(About)
class AboutAdmin(TranslationAdmin, CommonMedia, BaseAdmin):
    list_display = ('title',)
    verbose_name = "Hakkımızda"


@admin.register(Service)
class ServiceAdmin(TranslationAdmin, CommonMedia):
    list_display = ('title',)
    verbose_name = _("Hizmetlerim")

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    verbose_name = "Slider"

@admin.register(Category)
class CategoryAdmin(TranslationAdmin, CommonMedia):
    list_display = ('name',)
    verbose_name = "Kategori"


@admin.register(Blog)
class BlogAdmin(TranslationAdmin, CommonMedia):
    list_display = ('title', 'category', 'views', 'created_at', 'update_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at', 'update_at')
    date_hierarchy = 'created_at'
    verbose_name = "Blog"

@admin.register(Settings)
class SettingsAdmin(TranslationAdmin, CommonMedia, BaseAdmin):
    list_display = ('title', 'dest', 'keywords')
    verbose_name = "Ayarlar"