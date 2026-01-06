from django.core.management.base import BaseCommand
from apps.seo.models import SeoSettings


class Command(BaseCommand):
    help = 'SEO ayarlarını yaradır'

    def handle(self, *args, **options):
        try:
            seo = SeoSettings.objects.get(pk=1)
            
            # Boş alanları güncelle
            updated = False
            
            if not seo.meta_title:
                seo.meta_title = 'Gilli - Premium Məhsullar'
                updated = True
                
            if not seo.meta_description:
                seo.meta_description = 'Gilli ilə keyfiyyətli və premium məhsulları kəşf edin. Ən yaxşı qiymətlərlə, etibarlı xidmət.'
                updated = True
                
            if not seo.meta_keywords:
                seo.meta_keywords = 'gilli, premium, məhsul, keyfiyyət, onlayn alış-veriş'
                updated = True
                
            if not seo.og_title:
                seo.og_title = 'Gilli - Premium Məhsullar'
                updated = True
                
            if not seo.og_description:
                seo.og_description = 'Gilli ilə keyfiyyətli və premium məhsulları kəşf edin. Ən yaxşı qiymətlərlə, etibarlı xidmət.'
                updated = True
                
            if not seo.robots_txt:
                seo.robots_txt = '''User-agent: *
Allow: /
Disallow: /admin/
Disallow: /ckeditor/

Sitemap: https://yourdomain.com/sitemap.xml'''
                updated = True
            
            if updated:
                seo.save()
                self.stdout.write(
                    self.style.SUCCESS('SEO ayarları uğurla yeniləndi.')
                )
            else:
                self.stdout.write(
                    self.style.WARNING('Bütün SEO sahələri artıq doludur.')
                )
                
        except SeoSettings.DoesNotExist:
            # Yoksa oluştur
            seo = SeoSettings.objects.create(
                pk=1,
                meta_title='Gilli - Premium Məhsullar',
                meta_description='Gilli ilə keyfiyyətli və premium məhsulları kəşf edin. Ən yaxşı qiymətlərlə, etibarlı xidmət.',
                meta_keywords='gilli, premium, məhsul, keyfiyyət, onlayn alış-veriş',
                og_title='Gilli - Premium Məhsullar',
                og_description='Gilli ilə keyfiyyətli və premium məhsulları kəşf edin. Ən yaxşı qiymətlərlə, etibarlı xidmət.',
                robots_txt='''User-agent: *
Allow: /
Disallow: /admin/
Disallow: /ckeditor/

Sitemap: https://yourdomain.com/sitemap.xml'''
            )
            self.stdout.write(
                self.style.SUCCESS('SEO ayarları uğurla yaradıldı.')
            )