from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import SeoSettings
from apps.product.models import Product, Blog


def robots_txt(request):
    seo = SeoSettings.get_settings()
    content = seo.robots_txt or "User-agent: *\nAllow: /"
    return HttpResponse(content, content_type='text/plain')


def sitemap_xml(request):
    """Tam dinamik sitemap.xml"""
    
    seo = SeoSettings.get_settings()
    
    # Ana səhifələr
    static_urls = [
        {'loc': request.build_absolute_uri('/'), 'priority': '1.0', 'changefreq': 'daily'},
        {'loc': request.build_absolute_uri('/about/'), 'priority': '0.8', 'changefreq': 'monthly'},
        {'loc': request.build_absolute_uri('/shop/'), 'priority': '0.9', 'changefreq': 'weekly'},
        {'loc': request.build_absolute_uri('/contact/'), 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': request.build_absolute_uri('/blogs/'), 'priority': '0.8', 'changefreq': 'weekly'},
        {'loc': request.build_absolute_uri('/gallery/'), 'priority': '0.6', 'changefreq': 'monthly'},
    ]
    
    # Məhsullar (əgər aktiv edilmişsə)
    product_urls = []
    if seo.sitemap_include_products:
        for product in Product.objects.all():
            product_urls.append({
                'loc': request.build_absolute_uri(product.get_absolute_url()),
                'priority': '0.7',
                'changefreq': 'weekly'
            })
    
    # Bloglar (əgər aktiv edilmişsə)
    blog_urls = []
    if seo.sitemap_include_blogs:
        for blog in Blog.objects.all():
            blog_urls.append({
                'loc': request.build_absolute_uri(blog.get_absolute_url()),
                'priority': '0.6',
                'changefreq': 'monthly',
                'lastmod': blog.updated.strftime('%Y-%m-%d')
            })
    
    # XML yaradılması
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Statik səhifələr
    for url in static_urls:
        sitemap_content += f'''    <url>
        <loc>{url['loc']}</loc>
        <lastmod>{timezone.now().strftime('%Y-%m-%d')}</lastmod>
        <changefreq>{url['changefreq']}</changefreq>
        <priority>{url['priority']}</priority>
    </url>
'''
    
    # Məhsullar
    for url in product_urls:
        sitemap_content += f'''    <url>
        <loc>{url['loc']}</loc>
        <lastmod>{timezone.now().strftime('%Y-%m-%d')}</lastmod>
        <changefreq>{url['changefreq']}</changefreq>
        <priority>{url['priority']}</priority>
    </url>
'''
    
    # Bloglar
    for url in blog_urls:
        lastmod = url.get('lastmod', timezone.now().strftime('%Y-%m-%d'))
        sitemap_content += f'''    <url>
        <loc>{url['loc']}</loc>
        <lastmod>{lastmod}</lastmod>
        <changefreq>{url['changefreq']}</changefreq>
        <priority>{url['priority']}</priority>
    </url>
'''
    
    sitemap_content += '</urlset>'
    
    return HttpResponse(sitemap_content, content_type='application/xml')
