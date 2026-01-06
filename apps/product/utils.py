try:
    from slugify import slugify as python_slugify
    # Test edək ki, düzgün işləyir
    test_result = python_slugify("ə")
    if test_result == "e":
        SLUGIFY_AVAILABLE = True
    else:
        SLUGIFY_AVAILABLE = False
except ImportError:
    SLUGIFY_AVAILABLE = False

if SLUGIFY_AVAILABLE:
    def custom_slugify(text):
        """Unicode hərfləri dəstəkləyən slug yaradır"""
        return python_slugify(text, lowercase=True, separator='-')
else:
    # Əgər python-slugify yoxdursa və ya düzgün işləmirsə
    from django.utils.text import slugify as django_slugify
    
    def azerbaijani_to_latin(text):
        """Azərbaycan hərflərini Latin hərflərinə çevirir"""
        replacements = {
            'ə': 'e', 'Ə': 'E',
            'ı': 'i', 'I': 'I', 
            'ö': 'o', 'Ö': 'O',
            'ü': 'u', 'Ü': 'U',
            'ç': 'c', 'Ç': 'C',
            'ğ': 'g', 'Ğ': 'G',
            'ş': 's', 'Ş': 'S'
        }
        for az_char, latin_char in replacements.items():
            text = text.replace(az_char, latin_char)
        return text
    
    def custom_slugify(text):
        """Azərbaycan hərflərini dəstəkləyən slug yaradır"""
        return django_slugify(azerbaijani_to_latin(text))