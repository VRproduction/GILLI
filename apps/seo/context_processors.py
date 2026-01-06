from .models import SeoSettings


def seo(request):
    return {'seo': SeoSettings.get_settings()}
