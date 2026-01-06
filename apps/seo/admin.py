from django.contrib import admin
from .models import SeoSettings


@admin.register(SeoSettings)
class SeoSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Meta Tags', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_description', 'og_image')
        }),
        ('Analytics', {
            'fields': ('google_analytics_id', 'google_tag_manager_id')
        }),
        ('Sitemap', {
            'fields': ('sitemap_include_products', 'sitemap_include_blogs')
        }),
        ('Robots', {
            'fields': ('robots_txt',)
        }),
    )
    
    def has_add_permission(self, request):
        return not SeoSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
