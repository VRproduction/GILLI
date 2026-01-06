from django.core.management.base import BaseCommand
from apps.product.models import Product, Blog


class Command(BaseCommand):
    help = 'Mövcud slug-ları yoxlayır'

    def handle(self, *args, **options):
        self.stdout.write("=== MƏHSUL SLUG-LARI ===")
        for product in Product.objects.all():
            self.stdout.write(f"ID: {product.pk} | Title: '{product.title}' | Slug: '{product.slug}'")
        
        self.stdout.write("\n=== BLOG SLUG-LARI ===")
        for blog in Blog.objects.all():
            self.stdout.write(f"ID: {blog.pk} | Title: '{blog.title}' | Slug: '{blog.slug}'")
        
        self.stdout.write(f"\nCəmi: {Product.objects.count()} məhsul, {Blog.objects.count()} blog")