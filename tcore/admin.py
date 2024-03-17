from django.contrib import admin
from .models import Contact

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