from django.core.management.base import BaseCommand
from apps.product.models import Product, Blog
from apps.product.utils import custom_slugify


class Command(BaseCommand):
    help = 'Məhsul və blog slug-larını yenidən yaradır'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Mövcud slug-ları da yenilə',
        )

    def handle(self, *args, **options):
        force = options['force']
        
        # Əvvəlcə statistika göstər
        total_products = Product.objects.count()
        total_blogs = Blog.objects.count()
        products_with_slug = Product.objects.exclude(slug__isnull=True).exclude(slug='').count()
        blogs_with_slug = Blog.objects.exclude(slug__isnull=True).exclude(slug='').count()
        
        self.stdout.write(f"Cəmi məhsul: {total_products}")
        self.stdout.write(f"Slug-ı olan məhsul: {products_with_slug}")
        self.stdout.write(f"Cəmi blog: {total_blogs}")
        self.stdout.write(f"Slug-ı olan blog: {blogs_with_slug}")
        self.stdout.write("---")
        
        # Product slug-larını yenilə
        products_updated = 0
        for product in Product.objects.all():
            old_slug = product.slug
            should_update = force or not old_slug
            
            if should_update:
                base_slug = custom_slugify(product.title)
                
                if not base_slug:
                    base_slug = f"product-{product.pk}"
                
                # Unique slug yarat
                slug = base_slug
                counter = 1
                while Product.objects.filter(slug=slug).exclude(pk=product.pk).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                
                product.slug = slug
                product.save()
                products_updated += 1
                self.stdout.write(f"Product: '{product.title}' -> '{slug}'")
        
        # Blog slug-larını yenilə
        blogs_updated = 0
        for blog in Blog.objects.all():
            old_slug = blog.slug
            should_update = force or not old_slug
            
            if should_update:
                base_slug = custom_slugify(blog.title)
                
                if not base_slug:
                    base_slug = f"blog-{blog.pk}"
                
                # Unique slug yarat
                slug = base_slug
                counter = 1
                while Blog.objects.filter(slug=slug).exclude(pk=blog.pk).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                
                blog.slug = slug
                blog.save()
                blogs_updated += 1
                self.stdout.write(f"Blog: '{blog.title}' -> '{slug}'")
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Tamamlandı! {products_updated} məhsul və {blogs_updated} blog slug-u yeniləndi.'
            )
        )