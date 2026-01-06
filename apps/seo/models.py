from django.db import models


class SeoSettings(models.Model):
    meta_title = models.CharField(max_length=70, blank=True, verbose_name='Meta Title')
    meta_description = models.CharField(max_length=160, blank=True, verbose_name='Meta Description')
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name='Meta Keywords')
    og_title = models.CharField(max_length=70, blank=True, verbose_name='OG Title')
    og_description = models.CharField(max_length=200, blank=True, verbose_name='OG Description')
    og_image = models.ImageField(upload_to='seo/', blank=True, verbose_name='OG Image')
    google_analytics_id = models.CharField(max_length=50, blank=True, verbose_name='Google Analytics ID')
    google_tag_manager_id = models.CharField(max_length=50, blank=True, verbose_name='Google Tag Manager ID')
    robots_txt = models.TextField(blank=True, verbose_name='robots.txt içeriği')
    
    # Sitemap ayarları
    sitemap_include_products = models.BooleanField(default=True, verbose_name='Məhsulları sitemap-ə daxil et')
    sitemap_include_blogs = models.BooleanField(default=True, verbose_name='Blogları sitemap-ə daxil et')
    
    class Meta:
        verbose_name = 'SEO Ayarları'
        verbose_name_plural = 'SEO Ayarları'
    
    def __str__(self):
        return 'SEO Ayarları'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
