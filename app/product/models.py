from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class GeneralSettings(models.Model):
    site_title = models.CharField(
        max_length=200, verbose_name="Saytın başlığı")
    adress = models.CharField(max_length=1500, verbose_name="Ünvan", null=True, blank=True)
    email = models.EmailField(blank = True)
    g_adress = models.CharField(
        max_length=1500, verbose_name="Google Map linki", null=True, blank=True)
    g_adress_iframe = models.TextField(
        verbose_name="Google Map Iframe linki", null=True, blank=True)
    
    logo = models.FileField(verbose_name="logo(171x38)",
                            blank=True, upload_to="general_settings_logo")
    mobile_logo = models.FileField(verbose_name="Mobile logo(172x38)",
                                   help_text="Mobile logo", blank=True, null=True, upload_to="general_settings_mobile_logo")
    favicon = models.FileField(verbose_name="favicon(100x100)",
                               blank=True, null=True, upload_to="general_settings_favicon")
    footer_logo = models.FileField(help_text="Footer logo", blank=True, null=True, upload_to="general_settings_footer_logo")
    footer_slogan = models.TextField(null = True, blank = True)
    footer_slogan_2 = models.TextField(null = True, blank = True)
    copyright_title = models.CharField(max_length = 100, blank = True)
    copyright_link = models.TextField(null = True, blank = True)
    facebook = models.CharField(
        max_length=200, verbose_name="Facebook", blank=True)
    instagram = models.CharField(
        max_length=200, verbose_name="Instagram", blank=True)
    youtube = models.CharField(
        max_length=200, verbose_name="Youtube", blank=True)
    tiktok = models.CharField(
        max_length=200, verbose_name="TikTok", blank=True)
    
    def __str__(self):
        return ('%s') % (self.site_title)

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "General Settings"

class PhoneNumber(models.Model):
    number = models.CharField(max_length=200, blank=True, null = True)
    setting = models.ForeignKey(GeneralSettings, on_delete = models.CASCADE, related_name = 'numbers', null = True, blank = True)
    is_main = models.BooleanField(default = False)

    def __str__(self):
        return ('%s') % (self.number)

    class Meta:
        verbose_name = "Nömrə"
        verbose_name_plural = "Nömrələr"

class IndexSlider(models.Model):
    image = models.ImageField(upload_to = 'index-slider', null = True, blank = True)
    title_small = models.CharField(max_length = 100, null = True, blank = True)
    title_big = models.CharField(max_length = 100, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return 'Slayder'
    
    class Meta:
        verbose_name = 'Slayder'
        verbose_name_plural = 'Ana səhifə | Slayder'

class IndexVideo(models.Model):
    image = models.ImageField(upload_to = 'index-video', null = True, blank = True)
    iframe_link = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return 'Video'
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Ana səhifə | Video'

class About(models.Model):
    title = models.CharField(max_length = 500)
    description = RichTextUploadingField(null = True, blank = True)
    image = models.ImageField(upload_to = 'about', verbose_name = "image(497x643)px")

    def __str__(self):
        return "Haqqımızda"
    
    class Meta:
        verbose_name = 'Haqqımızda'
        verbose_name_plural = 'Haqqımızda'

class Category(models.Model):
    title = models.CharField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

class Product(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()
    image = models.ImageField(upload_to = 'product')
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'products')
    link = models.URLField(null = True, blank = True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'
    
    def get_absolute_url(self):
        return reverse("product-detail", args=[str(self.pk)])
    
class WhyChooseUs(models.Model):
    image = models.ImageField(upload_to = 'choose_section', null = True, blank = True) 

    def __str__(self):
        return 'Niyə bizi seçməlisiniz'
    
    class Meta:
        verbose_name = 'Niyə bizi seçməlisiniz'
        verbose_name_plural = 'Niyə bizi seçməlisiniz'

class WhyChooseUsPunkt(models.Model):
    whyChooseUs = models.ForeignKey(WhyChooseUs, on_delete = models.CASCADE, null = True, blank = True, related_name = 'punkts')
    image = models.ImageField(upload_to = 'choose_section_punkts')
    title = models.CharField(max_length = 500)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Punkt'
        verbose_name_plural = 'Punktlar'

class FAQ(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()

    def __str__(self):
        return ('%s') % (self.title)

    class Meta:
        verbose_name = "Sual"
        verbose_name_plural = "Suallar"

class Comment(models.Model):
    image = models.ImageField(upload_to = 'comment')
    full_name = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return ('%s') % (self.full_name)

    class Meta:
        verbose_name = "Rəy"
        verbose_name_plural = "Rəylər"

class Blog(models.Model):
    title = models.CharField(max_length = 500)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to = 'blogs')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    is_main_page  = models.BooleanField(default = False, verbose_name = "Əsas səhifədə görünsün?")

    def __str__(self):
        return ('%s') % (self.title)

    class Meta:
        verbose_name = "Bloglar"
        verbose_name_plural = "Bloglar"

    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.pk)])
    
class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    number = models.CharField(max_length = 50, null = True, blank = True)
    subject = models.CharField(max_length = 200, null = True, blank = True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return ('%s') % (self.name)

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"